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

        }

class OrderOptionForm(forms.ModelForm):
    class Meta:
        model = OrderOption
        fields = ['image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['taste', 'service', 'design','textReview']
        widgets = {
            'taste': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '맛 평가',
                    'max': 5,
                    'min': 1
                }
            ),
            'service': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '서비스 평가',
                    'max': 5,
                    'min': 1
                }
            ),
            'design': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '디자인 평가',
                    'max': 5,
                    'min': 1
                }
            ),
            'textReview': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '텍스트 리뷰'
                }
            ),
        }