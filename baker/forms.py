from django import forms

from home.models import Store, Baker, Cake

class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = ('businessID','storeName','storeContact','pickUpOpen','pickUpClose','aboutStore',)

class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ['cakeName', 'cakeImg', 'cakePrice', 'mini']
        widgets = {
            'cakeName' : forms.TextInput(
                # attrs={'class' : 'form-control', 'aria-label': 'cakeName', 'aria-describedby' : 'add-btn'}
                # 여기를 이용해서 꾸며야 합니다.
            )
        }