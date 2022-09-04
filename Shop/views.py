from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import View,DetailView
from Shop.models import Category, Item
from Users.models import Basket
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from .form import FilterItems, SearchField

def ajax_results(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        res = None
        item = request.POST['item']
        items = Item.objects.filter(name__icontains=item)
        if len(items) > 0 and len(item) > 0:
            names=list()
            for i in list(items):
                names.append(i.name) 
            res = names
        else:
            res = 'Ничего не найдено'
        print(items)
        return JsonResponse({'data':res})
    return JsonResponse({})

class ResultSearchView(View):
    def get(self,request):
        err = None
        if 'name' in request.GET:
            items = Item.objects.filter(name__icontains=request.GET.get('name')).select_related('cat')
            if len(list(items)) >= 1:
                pass
            else:
                err = 'Ничего не найдено'
        else:
            items = Item.objects.all().select_related('cat')
        if err is not None:
            return render(request=request,template_name='Shop/search.html',context={'error':err,'name':"Магазин Копеечка","form_ser":SearchField(request.GET)})
        pag = Paginator(list(items),10)
        pag_num = request.GET.get('page',1)
        page_obj = pag.get_page(pag_num)
        return render(request=request,template_name='Shop/search.html',context={'items':page_obj,'name':"Магазин Копеечка","form_ser":SearchField()})

class ShopPageView(View):
    def get(self,request):
        form = FilterItems()
        min_val = int(request.GET.get('min_price',0))
        max_val = int(request.GET.get('max_price',99999))
        items = Item.objects.filter(
            Q(basket=None),
            Q(cost__gte=min_val),
            Q(cost__lte=max_val)
        ).select_related('cat')
        pag = Paginator(list(items),10)
        pag_num = request.GET.get('page')
        page_obj = pag.get_page(pag_num)
        cats = Category.objects.all()
        return render(request=request,template_name="Shop/home.html",context={'page_obj':page_obj,'name':"Магазин Копеечка",'form_filt':form,'cats':cats})

class AddToBasket(LoginRequiredMixin,View):
    def post(self,request,pk):
        item = Item.objects.get(pk=pk)
        basket = Basket.objects.get(user=request.user)
        basket.count += 1
        basket.save()
        Item.objects.create(name=item.name,img=item.img,cost=item.cost,desk=item.desk,cat=item.cat,count=1,basket=basket)
        item.count -= 1
        item.save()
        return redirect('home2')

class CategoryListView(View):
    def get(self,request,pk):
        form = FilterItems()
        cat_sel = Category.objects.get(pk=pk)
        if 'min_price' and 'max_price' in request.GET:
            min_val = int(request.GET.get('min_price',0))
            max_val = int(request.GET.get('max_price',99999))
            items = Item.objects.filter(
                Q(basket=None),
                Q(cat=cat_sel),
                Q(cost__gte=min_val),
                Q(cost__lte=max_val)
            ).select_related('cat')
        else:
            items = Item.objects.filter(
                Q(basket=None),
                Q(cat=cat_sel)
            ).select_related('cat')
        pag = Paginator(list(items),10)
        pag_num = request.GET.get('page')
        page_obj = pag.get_page(pag_num)
        cats = Category.objects.all()
        return render(request=request,template_name="Shop/catlist.html",context={'page_obj':page_obj,'name':"Магазин Копеечка",'form_filt':form,'cats':cats,'cat_sel':cat_sel})

class ItemDetailView(DetailView):
    model = Item
    template_name = "Shop/detail.html"
    context_object_name = 'item'
    extra_context = {'name':"Магазин Копеечка",'form_s':''}