from django import forms

from home.models import Store, Baker

class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = ('businessID','storeName','storeContact','pickUpOpen','pickUpClose','aboutStore',)