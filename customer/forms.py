from django import forms
from home.models import *

class OrdererForm(forms.ModelForm):
    class Meta:
        model = Orderer
        fields = ['userID', 'name', 'phoneNum']
        widgets = {
            'userID':forms.TextInput(
                attrs={'class':'form-control',
                       'id': 'userID',
                       'placeholder':'기입하였던 아이디를 입력하세요'}
            ),
            # 'email': forms.EmailField(
            #     attrs={'class': 'form-control',
            #            'id': 'email',
            #            'placeholder': '이메일'}
            # ),
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'id': 'name',
                       'placeholder': '성명'}
            ),
            'phoneNum': forms.TextInput(
                attrs={'class': 'form-control',
                       'id': 'phoneNum',
                       'placeholder': '예) 010-1234-5678',
                       'pattern': "(010)-\d{3,4}-\d{4}"}
            ),
            # 'password': forms.PasswordInput(
            #     attrs={'class': 'form-control',
            #            'id': 'password',
            #            'placeholder': '비밀번호'}
            # )

        }