from tkinter.tix import Tree
from django import forms
from .models import Comments

class FilterItems(forms.Form):
    min_price = forms.IntegerField(label='Минимальная цена',required=True,min_value=0)
    max_price = forms.IntegerField(label='Максимальная цена',required=True,min_value=0)

class SearchField(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"id":"item"}),label='Имя товара',required=True)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)
    