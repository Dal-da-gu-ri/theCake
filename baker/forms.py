from django import forms
from home.models import *
from django.forms import modelformset_factory
# class BakerForm(forms.ModelForm):
#     class Meta:
#         model = Baker
#         fields = ['userID', 'name', 'phoneNum']
#         widgets = {
#             'userID':forms.TextInput(
#                 attrs={'class':'form-control',
#                        'id': 'userID',
#                        'placeholder':'기입하였던 아이디를 입력하세요'}
#             ),
#             # 'email': forms.EmailField(
#             #     attrs={'class': 'form-control',
#             #            'id': 'email',
#             #            'placeholder': '이메일'}
#             # ),
#             'name': forms.TextInput(
#                 attrs={'class': 'form-control',
#                        'id': 'name',
#                        'placeholder': '성명'}
#             ),
#             'phoneNum': forms.TextInput(
#                 attrs={'class': 'form-control',
#                        'id': 'phoneNum',
#                        'placeholder': '예) 010-1234-5678',
#                        'pattern': "(010)-\d{3,4}-\d{4}"}
#             ),
#             # 'password': forms.PasswordInput(
#             #     attrs={'class': 'form-control',
#             #            'id': 'password',
#             #            'placeholder': '비밀번호'}
#             # )
#
#         }

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['storeImg', 'storeName', 'storeContact', 'aboutStore', 'pickUpOpen', 'pickUpClose', 'postcode', 'address1', 'address2', 'address3', 'daum_sido', 'daum_sigungu', 'daum_dong']
        widgets = {
            # label은 HTML에서 label태그를 의미
            # widget은 input이라고 생각
            # 예를 들어, TextInput은 <input type="text">를 의미
            # textarea 태그를 원하면 widget = forms.Textarea라고 설정하면 됨.
            # attrs={}안에 지정하고자 하는 class나 placeholder등을 부가적으로 설정(이 또한 HTML 엘리먼트의 속성)

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
            'postcode': forms.TextInput(
                attrs={'id':'sample6_postcode',
                       'class': 'form-control',
                       'placeholder':"우편번호"}
            ),
            'address1': forms.TextInput(
                attrs={'id': 'sample6_address',
                       'class': 'form-control',
                       'placeholder':"주소"}
            ),
            'address2': forms.TextInput(
                attrs={'id': 'sample6_detailAddress',
                       'class': 'form-control',
                       'placeholder':"상세주소"}
            ),
            'address3': forms.TextInput(
                attrs={'id': 'sample6_extraAddress',
                       'class': 'form-control',
                       'placeholder':"참고항목"}
            ),
            'daum_sido': forms.TextInput(
                attrs={'id': 'daum_sido',
                       'class': 'form-control',
                       'hidden': 'hidden'}
            ),
            'daum_sigungu': forms.TextInput(
                attrs={'id': 'daum_sigungu',
                       'class': 'form-control',
                       'hidden': 'hidden'}
            ),
            'daum_dong': forms.TextInput(
                attrs={'id': 'daum_dong',
                       'class': 'form-control',
                       'hidden': 'hidden'}
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
            ),
            'mini': forms.RadioSelect()
        }

class OpenDaysForm(forms.ModelForm):
    class Meta:
        model = OpenDays
        fields = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        widgets = {
            'monday': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '월요일 주문가능수량'
                }
            ),
            'tuesday': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '화요일 주문가능수량'
                }
            ),
            'wednesday': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '수요일 주문가능수량'
                }
            ),
            'thursday': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '목요일 주문가능수량'
                }
            ),
            'friday': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '금요일 주문가능수량'
                }
            ),
            'saturday': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '토요일 주문가능수량'
                }
            ),
            'sunday': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '일요일 주문가능수량'
                }
            )
        }

class DailyAmountForm1(forms.ModelForm):
    class Meta:
        model = DailyAmount
        fields = ['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10','day11','day12','day12','day13','day14','day15','day16','day17','day18','day19','day20','day21','day22','day23','day24','day25','day26','day27','day28','day29','day30']
        widgets = {
            'day1': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day1'
                }
            ),
            'day2': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day2'
                }
            ),
            'day3': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day3'
                }
            ),
            'day4': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day4'
                }
            ),
            'day5': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day5'
                }
            ),
            'day6': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3"
                    ,
                    'id': 'day6'
                }
            ),
            'day7': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day7'

                }
            ),
            'day8': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day8'
                }
            ),
            'day9': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day9'
                }
            ),
            'day10': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day10'
                }
            ),
            'day11': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day11'
                }
            ),
            'day12': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day12'
                }
            ),
            'day13': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day13'
                }
            ),
            'day14': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day14'
                }
            ),
            'day15': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day15'
                }
            ),
            'day16': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day16'
                }
            ),
            'day17': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day17'
                }
            ),
            'day18': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day18'
                }
            ),
            'day19': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day19'
                }
            ),
            'day20': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day20'
                }
            ),
            'day21': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day21'
                }
            ),
            'day22': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day22'
                }
            ),
            'day23': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day23'
                }
            ),
            'day24': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day24'
                }
            ),
            'day25': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day25'
                }
            ),
            'day26': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day26'
                }
            ),
            'day27': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day27'
                }
            ),
            'day28': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day28'
                }
            ),
            'day29': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day29'
                }
            ),
            'day30': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day30'
                }
            )

        }

class DailyAmountForm(forms.ModelForm):
    class Meta:
        model = DailyAmount
        fields = ['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10','day11','day12','day12','day13','day14','day15','day16','day17','day18','day19','day20','day21','day22','day23','day24','day25','day26','day27','day28','day29','day30','day31',
                  'day32','day33','day34','day35','day36','day37','day38','day39','day40','day41','day42','day43','day44','day45','day46','day47','day48','day49','day50','day51','day52','day53','day54','day55','day56','day57','day58','day59','day60','day61','day62']
        widgets = {
            'day1': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day1'
                }
            ),
            'day2': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day2'
                }
            ),
            'day3': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day3'
                }
            ),
            'day4': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day4'
                }
            ),
            'day5': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day5'
                }
            ),
            'day6': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3"
                    ,
                    'id': 'day6'
                }
            ),
            'day7': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day7'

                }
            ),
            'day8': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day8'
                }
            ),
            'day9': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day9'
                }
            ),
            'day10': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day10'
                }
            ),
            'day11': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day11'
                }
            ),
            'day12': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day12'
                }
            ),
            'day13': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day13'
                }
            ),
            'day14': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day14'
                }
            ),
            'day15': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day15'
                }
            ),
            'day16': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day16'
                }
            ),
            'day17': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day17'
                }
            ),
            'day18': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day18'
                }
            ),
            'day19': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day19'
                }
            ),
            'day20': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day20'
                }
            ),
            'day21': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day21'
                }
            ),
            'day22': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day22'
                }
            ),
            'day23': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day23'
                }
            ),
            'day24': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day24'
                }
            ),
            'day25': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day25'
                }
            ),
            'day26': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day26'
                }
            ),
            'day27': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day27'
                }
            ),
            'day28': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day28'
                }
            ),
            'day29': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day29'
                }
            ),
            'day30': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day30'
                }
            ),
            'day31': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day31'
                }
            ),
            'day32': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day32'
                }
            ),
            'day33': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day33'
                }
            ),
            'day34': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day34'
                }
            ),
            'day35': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day35'
                }
            ),
            'day36': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day36'
                }
            ),
            'day37': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day37'

                }
            ),
            'day38': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day38'
                }
            ),
            'day39': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day39'
                }
            ),
            'day40': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day40'
                }
            ),
            'day41': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day41'
                }
            ),
            'day42': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day42'
                }
            ),
            'day43': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day43'
                }
            ),
            'day44': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day44'
                }
            ),
            'day45': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day45'
                }
            ),
            'day46': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day46'
                }
            ),
            'day47': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day47'
                }
            ),
            'day48': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day48'
                }
            ),
            'day49': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day49'
                }
            ),
            'day50': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day50'
                }
            ),
            'day51': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day51'
                }
            ),
            'day52': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day52'
                }
            ),
            'day53': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day53'
                }
            ),
            'day54': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day54'
                }
            ),
            'day55': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day55'
                }
            ),
            'day56': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day56'
                }
            ),
            'day57': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day57'
                }
            ),
            'day58': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day58'
                }
            ),
            'day59': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day59'
                }
            ),
            'day60': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day60'
                }
            ),
            'day61': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day61'
                }
            ),
            'day62': forms.NumberInput(
                attrs={
                    'class': "text-center form-group col-12 col-md-10 mt-3",
                    'id': 'day62'
                }
            )

        }
    

class OptionForm(forms.ModelForm):

    class Meta:
        model = Option
        fields = ['optionName', 'isNecessary', 'withColor', 'withImage']
        labels = {
            'optionName': 'Option Name',
            'isNecessary':'Necessary?',
            'withColor':'Color?',
            'withImage':'Image?'
        }
        widgets = {
            'optionName' : forms.TextInput(
                attrs={
                    'placeholder': '옵션명(10자리 이하)'
                }
            ),
            'isNecessary' : forms.CheckboxInput,
            'withColor' : forms.CheckboxInput,
            'withImage' : forms.CheckboxInput
        }


# OptionFormset = formset_factory(BookForm)
OptionFormset = modelformset_factory(
    Option,
    fields=['optionName', 'isNecessary', 'withColor', 'withImage'],
extra=1,
    widgets={
        'optionName': forms.TextInput(
            attrs={
                'placeholder': '옵션명(10자리 이하)'
            }
        ),
        'isNecessary': forms.CheckboxInput,
        'withColor': forms.CheckboxInput,
        'withImage': forms.CheckboxInput
    }
)

DetailedOptionFormset = modelformset_factory(
    DetailedOption,
    fields=('detailName', 'pricing', ),
    extra=1,
    widgets={'detailName' : forms.TextInput(
                attrs={
                    'placeholder': '세부항목(10자리 이하)'
                }
            ),
            'pricing' : forms.NumberInput(
                attrs={
                    'placeholder': '숫자만 입력해주세요.'
                }
            )
    }
)

class CakeOptionForm(forms.ModelForm):
    class Meta:
        model = CakeOption
        fields = ['isSelected']
        widgets = {
            'isSelected' : forms.CheckboxInput
        }