from django import forms

from home.models import Store, Baker, Cake, DetailedOption

class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = ['storeName', 'storeContact', 'pickUpOpen', 'pickUpClose', 'aboutStore']
        # bussinessID 지웠음. 더 추가하기

class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ['cakeName', 'cakeImg', 'cakePrice', 'mini']
        widgets = {
            'cakeName': forms.TextInput(
                # attrs={'class' : 'form-control', 'aria-label': 'cakeName', 'aria-describedby' : 'add-btn'}
                # 여기를 이용해서 꾸며야 합니다.
            )
        }

class DetailedOptionForm(forms.ModelForm):
    class Meta:
        model = DetailedOption
        fields = ['detailName', 'pricing', 'withColor', 'withImage']
        widgets = {
            'detailName' : forms.TextInput(
                attrs={'class': 'form-control', 'aria-label': 'cakeName'}
                # 여기를 이용해서 꾸며야 합니다.
            ),
            'pricing' : forms.TextInput(
                attrs={}
            ),
            'withColor' : forms.TextInput(
                attrs={}
            ),
            'withImage' : forms.TextInput(
                attrs={}
            )
        }