import stripe
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,View
from Shop.models import Item
from Users.models import Basket
from .forms import PasswordSetForm, RegistrationForm,AuthForm,ChangeIMGForm, ResetPasswordForm
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin,AccessMixin
from django.contrib.auth.models import Permission
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .utils import  email_activate_token
from django.core.mail import send_mail
from django.utils.encoding import force_str,force_bytes
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.core.paginator import Paginator

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class UnLoginMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class Mixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Магазин Копеечка"
        return context

class HomePageView(Mixin,TemplateView):
    template_name = "home.html"
    extra_context = {'form_change':ChangeIMGForm}

class LoginOrRegistrationView(UnLoginMixin,Mixin,TemplateView):
    template_name = "Users/login.html"
    extra_context = {"soname":"Регистрация или Вход","form_reg":RegistrationForm,"form_log":AuthForm}

class Registrations(UnLoginMixin,View):
    form_class = RegistrationForm
     
    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            Basket.objects.create(user=get_user_model().objects.get(email=request.POST['email']),count=0)
            return JsonResponse({'success':True},status=200)
        else:
            return JsonResponse({'error':form.errors},status=203)


class Authentication(UnLoginMixin,View):
    def post(self, request,*args, **kwargs):
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            return JsonResponse({'success':True},status=200)
        else:
            return JsonResponse({"error":'This account don`t created or invalid username or password'},status=203)

class ChangeIMG_test(LoginRequiredMixin,View):
    
    form_class = ChangeIMGForm

    def post(self,request):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            user = request.user
            user.image = request.FILES["image"]
            user.save()
            return redirect('home')
        else:
            return redirect('home')

class Logout(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        return redirect("home")

class ResetPassword_1_View(UnLoginMixin,Mixin,PasswordResetView):
    template_name = 'Users/reset_pass.html'
    form_class = ResetPasswordForm
    extra_context = {"step":"Первый шаг"}

class ResetPassword_2_View(UnLoginMixin,Mixin,PasswordResetDoneView):
    template_name = 'Users/reset_pass_confirm.html'
    extra_context = {"step":"Второй шаг",'mess':"Проверьте вашу электронную почту. И перейдите по ссылке в письме."}

class ResetPassword_3_View(UnLoginMixin,Mixin,PasswordResetConfirmView):
    template_name = 'Users/reset_pass.html'
    form_class = PasswordSetForm
    extra_context = {"step":"Третий шаг"}

class ResetPassword_4_View(UnLoginMixin,Mixin,PasswordResetCompleteView):
    template_name = 'Users/reset_pass_confirm.html'
    extra_context = {'mess':"Вы успешно восстановили пароль"}

class ActivateSendEmailView(LoginRequiredMixin,Mixin,View):

    def post(self,request):
        if request.user.activeEmail:
            return JsonResponse({'error':True},status=203)
        else:
            token = email_activate_token.make_token(request.user)
            uid64 = force_str(urlsafe_base64_encode(force_bytes(request.user.pk)))
            url = '127.0.0.1:8000' + reverse_lazy('activeEmail',kwargs={'uidb64':uid64,'token':token})

            send_mail('Активация email http://127.0.0.1:8000/',
            f"Здравствуйте {request.user.username}! Для активации акаунта перейдите по ссылке: {url}",
            "pososi@gmail.com", [request.user.email,],
            fail_silently=False    
            )
            return JsonResponse({'success':True},status=200)

class ActivateEmailView(LoginRequiredMixin,Mixin,View):

    def get(self,request,uidb64,token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(pk=uid)
        except get_user_model().DoesNotExist:
            user = None

        if user is not None and email_activate_token.check_token(user,token):
            user.activeEmail = True
            user.save()
            return render(request=request,template_name='Users/reset_pass_confirm.html',context={"mess":"Вы успешно активировали аккаунт!"})
        else:
            return redirect("home")

class BasketView(LoginRequiredMixin,Mixin,View):

    def get(self,request):
        user = request.user
        basket = Basket.objects.get(user=user)
        items = Item.objects.filter(basket=basket).select_related('cat')
        pag = Paginator(list(items),10)
        pag_num = request.GET.get('page')
        page_obj = pag.get_page(pag_num)
        return render(request=request,template_name='Users/korzina.html',context={"basket":basket,"page_obj":page_obj,"name":"Магазин Копеечка",'stripe_key':settings.STRIPE_TEST_PUBLISHABLE_KEY})

class BasketClean(LoginRequiredMixin,View):

    def get(self,request,pk):
        basket = Basket.objects.get(user=request.user)
        basket.count -= 1
        basket.save()
        itemrem = Item.objects.get(pk=pk)
        allitem = Item.objects.get(basket=None,name=itemrem.name)
        if itemrem.count == 1:
            allitem.count += 1
            allitem.save()
            itemrem.delete()
        else:
            itemrem.count -= 1
            allitem.count += 1
            allitem.save()
            itemrem.save()
        return redirect('basket') 
    
class BasketAllClean(LoginRequiredMixin,View):

    def get(self,request):
        user = request.user
        basket = Basket.objects.get(user=user)
        allitem = Item.objects.filter(basket=basket)
        for i in list(allitem):
            abstritem = Item.objects.get(basket=None,name=i.name)
            if i.count == 1:
                abstritem.count += 1
                abstritem.save()
                basket.count -= 1
                basket.save()
                i.delete()
            count = i.count
            for num in range(0,count):
                if i.count == 1:
                    abstritem.count += 1
                    basket.count -= 1
                    basket.save()
                    abstritem.save()
                    i.delete() 
                else:
                    i.count -= 1  
                    abstritem.count += 1
                    basket.count -= 1
        return redirect('basket')

def charge(request,sum):
    permission = Permission.objects.get(codename='special_status')
    u = request.user
    u.user_permissions.add(permission)

    if request.method == 'POST':
        charge = stripe.Charge.create(
        amount=sum,
        currency='usd',
        description='Django_Store',
        source=request.POST['stripeToken']
        )
        return render(request, 'charge.html',context={"mess":f"You success buy on {sum}$"})



def pageNotFound(request, exception):
    return render(request=request,template_name='404.html',status=404)