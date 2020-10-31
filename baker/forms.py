from django import forms

from home.models import Store, Baker, Cake, DetailedOption

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['storeName', 'storeContact', 'aboutStore', 'pickUpOpen', 'pickUpClose', 'storeImg', 'location']
        widgets = {
            'storeName': forms.TextInput(
                #label='가게 이름',
                attrs={'class': 'form-control'}
            ),
            'storeContact': forms.TextInput(
                #label='가게 연락처',
                attrs={'class': 'form-control'}
            ),
            'pickUpOpen': forms.TextInput(
                #label='픽업 오픈 시간',
                attrs={'class': 'form-control'}
            ),
            'pickUpClose': forms.TextInput(
                #label='픽업 마감 시간',
                attrs={'class': 'form-control'}
            ),
            'aboutStore': forms.Textarea(
                #label='가게 소개글',
                attrs={'class': 'form-control'}
            ),
            'location': forms.TextInput(
                #label='가게 위치',
                attrs={'class': 'form-control'}
            )
        }

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