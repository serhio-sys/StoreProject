from django import forms
from .models import Comments

class FilterItems(forms.Form):
    min_price = forms.IntegerField(label='Минимальная цена',required=True,min_value=0)
    max_price = forms.IntegerField(label='Максимальная цена',required=True,min_value=0)

class SearchField(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"id":"item"}),label='Имя товара',required=True)

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 4,'class':'form-control','placeholder':'Ваш отзыв'}),max_length=150)
    class Meta:
        model = Comments
        fields = ('comment',)

class StarsForm(forms.Form):
    num = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'От 1 до 5 звёзд','class':'form-control form-control-sm'}),min_value=1,max_value=5,label='')

class AddToKorzina(forms.Form):
    def __init__(self, maxi, *args, **kwargs):
        super(AddToKorzina, self).__init__(*args, **kwargs)
        self.fields['num'] = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':f'От 1 до {maxi}','class':'form-control'}),min_value=1,max_value=maxi,label='')

    num = forms.IntegerField(label='',min_value=1)
    
    