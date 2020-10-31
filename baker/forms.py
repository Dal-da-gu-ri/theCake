from django import forms

from home.models import Store, Baker, Cake, DetailedOption

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['storeName', 'storeContact', 'aboutStore', 'pickUpOpen', 'pickUpClose', 'storeImg', 'sido', 'sigugun', 'dong']
        widgets = {
            'storeName': forms.TextInput(
                #label='가게 이름',
                attrs={'class': 'form-control'}
            ),
            'storeContact': forms.TextInput(
                #label='가게 연락처',
                attrs={
                    'class': 'form-control',
                    'placeholder': '예) 02-1234-5678'
                }
            ),
            'pickUpOpen': forms.Select(
                #label='픽업 오픈 시간',
                attrs={'class': 'form-control'}
            ),
            'pickUpClose': forms.Select(
                #label='픽업 마감 시간',
                attrs={'class': 'form-control'}
            ),
            'aboutStore': forms.Textarea(
                #label='가게 소개글',
                attrs={'class': 'form-control'}
            ),
            'sido': forms.Select(
                attrs={'class': 'sido'}
            ),
            'sigugun': forms.Select(
                attrs={'class': 'sigugun'}
            ),
            'dong': forms.Select(
                attrs={'class': 'dong'}
            )
        }

class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ['cakeName', 'cakeImg', 'cakePrice', 'mini']
        widgets = {
            'cakeName': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '케이크 이름'
                }
            ),
            'cakePrice': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '케이크 가격(1호 기준)'
                }
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