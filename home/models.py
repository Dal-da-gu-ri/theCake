from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
# from easy_thumbnails.fields import ThumbnailerImageField

class Orderer(models.Model):
    userID = models.CharField(max_length=20, verbose_name='주문자 아이디',blank=False, primary_key=True,default="")
    email = models.EmailField(max_length=128, verbose_name='주문자 이메일',blank=False,null=True)
    name = models.CharField(max_length=30,verbose_name='주문자 이름',null=True,blank=False)
    phoneNum = models.CharField(max_length=30, verbose_name='주문자 전화번호',null=True,blank=False,unique=True)
    password = models.CharField(max_length=200, verbose_name='주문자 비밀번호',null=True,blank=False)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.userID

    class Meta:
        db_table = 'Orderer'
        verbose_name = '주문자'
        verbose_name_plural = '주문자'

class checkOrderer(models.Model):
    userid = models.CharField(max_length=20, verbose_name='주문자 아이디',blank=False, primary_key=True)
    useremail = models.EmailField(max_length=128, verbose_name='주문자 이메일',blank=False,null=True)

    def __str__(self):
        return self.userid

    class Meta:
        db_table = 'checkOrderer'
        verbose_name = '주문자 가입용'
        verbose_name_plural = '주문자 가입용'

class Baker(models.Model):
    userID = models.CharField(max_length=20, verbose_name='사업자 아이디', blank=False, primary_key=True,default="")
    businessID = models.CharField(max_length=10, verbose_name='사업자 등록번호', blank=False, null=True)
    #businessName = models.CharField(max_length=40, verbose_name='사업자명', blank=False, null=True)
    email = models.EmailField(max_length=128, verbose_name='사업자 이메일', null=True, blank=False)  # unique=True,
    name = models.CharField(max_length=30, verbose_name='사업자 이름', null=True, blank=False)
    phoneNum = models.CharField(max_length=30, verbose_name='사업자 전화번호', null=True, blank=False)  # unique=True,
    password = models.CharField(max_length=200, verbose_name='사업자 비밀번호', null=True, blank=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.userID

    class Meta:
        db_table = 'Baker'
        verbose_name = '사업자'
        verbose_name_plural = '사업자'

class checkBaker(models.Model):
    userid = models.CharField(max_length=20, verbose_name='사업자 아이디', blank=False, primary_key=True,default="")
    #businessname = models.CharField(max_length=40, verbose_name='사업자명',blank=False, primary_key=True)
    businessCRN = models.CharField(max_length=10,verbose_name='사업자 등록번호',blank=False,null=True)

    def __str__(self):
        return self.userid

    class Meta:
        db_table = 'checkBaker'
        verbose_name = '사업자 가입용'
        verbose_name_plural = '사업자 가입용'

class Store(models.Model):
    TIME_CHOICES = {
        ('9:00', '9:00'), ('9:30', '9:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'),
        ('17:30', '17:30'),
        ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'),
        ('20:30', '20:30'),
        ('21:00', '21:00'), ('21:30', '21:30'), ('22:00', '22:00'), ('22:30', '22:30'),
    }
    businessID = models.CharField(max_length=10, verbose_name='사업자 등록번호', blank=False, primary_key=True)
    #manager = models.CharField(max_length=30, verbose_name='사업자이름', null=True,blank=False)
    manager = models.ForeignKey(Baker, on_delete=models.CASCADE,null=True)
    storeName = models.CharField(max_length=30, verbose_name='가게 이름', null=True, blank=True)
    location = models.CharField(max_length=200, verbose_name='가게 위치', null=True, blank=True) #나중에 blank False로 수정하기
    postcode = models.CharField(max_length=10, verbose_name='우편번호', null=True, blank=True)
    address1 = models.CharField(max_length=100, verbose_name='가게 주소', null=True, blank=True)
    address2 = models.CharField(max_length=100, verbose_name='가게 상세주소', null=True, blank=True)
    address3 = models.CharField(max_length=100, verbose_name='위치 추가정보', null=True, blank=True)
    sido = models.CharField(max_length=20, verbose_name='시/도', null=True, blank=True)
    sigugun = models.CharField(max_length=20, verbose_name='시/군/구', null=True, blank=True)
    dong = models.CharField(max_length=20, verbose_name='읍/면/동', null=True, blank=True)
    storeContact = models.CharField(max_length=30, verbose_name='가게 연락처', null=True, blank=True) #,unique=True
    pickUpOpen = models.CharField(max_length=15, verbose_name='픽업 오픈 시간',null=True, blank=True, choices=TIME_CHOICES)
    pickUpClose = models.CharField(max_length=15, verbose_name='픽업 마감 시간',null=True, blank=True, choices=TIME_CHOICES)
    aboutStore = models.TextField(verbose_name='가게 소개글', null=True, blank=True)
    storeImg = models.ImageField(verbose_name='가게 대표이미지', null=True, blank=True, default="logo_baker.png")

    def __str__(self):
        return self.businessID

    class Meta:
        db_table = 'Store'
        verbose_name = '가게'
        verbose_name_plural = '가게'


class Order(models.Model):
    MONTHS ={
        ('Jan', '1월'), ('Feb', '2월'), ('Mar', '3월'), ('Apr', '4월'), ('May', '5월'), ('Jun', '6월'),
        ('Jul', '7월'), ('Aug', '8월'), ('Sep', '9월'), ('Oct', '10월'), ('Nov', '11월'), ('Dec', '12월'),
    }
    orderNum = models.DateTimeField(auto_now_add=True,verbose_name='주문 번호',primary_key=True,blank=False)
    orderer = models.ForeignKey(Orderer,on_delete=models.CASCADE)
    pickupDate = models.CharField(max_length=30,verbose_name='희망 수령일',null=True,blank=False)
    pickupTime = models.CharField(max_length=20,verbose_name='희망 픽업 시간',null=True,blank=False)
    businessID = models.CharField(max_length=50, verbose_name='사업자 등록번호',null=True,blank=False)
    cakeName = models.CharField(max_length=200, verbose_name='케이크 이름',null=True,blank=False)
    requiredOpt = models.TextField(verbose_name='필수 선택 옵션',null=True,blank=False)
    additionalOpt = models.TextField(verbose_name='추가 선택 옵션',null=True,blank=True)
    cakeText = models.TextField(verbose_name='케이크 문구',null=True,blank=True)
    message = models.TextField(verbose_name='요청 사항',null=True,blank=True)
    price = models.IntegerField(verbose_name='가격',null=True,blank=False)
    status = models.CharField(max_length=30,verbose_name='주문 진행 상황',null=True,blank=False)

    def __str__(self):
         return self.orderNum

    class Meta:
        db_table = 'Order'
        verbose_name = '주문서'
        verbose_name_plural = '주문서'

class Review(models.Model):
    orderNum = models.CharField(max_length=20, verbose_name='주문 번호',primary_key=True) #random하게 하기
    orderer = models.ForeignKey(Orderer,on_delete=models.CASCADE)
    cakeStore = models.ForeignKey(Store,on_delete=models.CASCADE)
    taste = models.IntegerField(verbose_name='맛 평점',null=True,blank=False)
    service = models.IntegerField(verbose_name='서비스 평점',null=True,blank=False)
    design = models.IntegerField(verbose_name='디자인 평점',null=True,blank=False)
    textReview = models.TextField(verbose_name='한 줄 후기',null=True,blank=True)

    class Meta:
        db_table = 'Review'
        verbose_name = '리뷰'
        verbose_name_plural = '리뷰'

class Option(Store):
    optionName = models.CharField(max_length=30,verbose_name='옵션명',null=True,blank=False,unique=True)
    isNecessary = models.BooleanField(default=False,verbose_name='필수 여부',null=True,blank=False)
    withColor = models.BooleanField(default=False,verbose_name='색상판 유무',null=True,blank=False)
    withImage = models.BooleanField(default=False,verbose_name='이미지추가 유무',null=True,blank=False)

    class Meta:
        abstract = True


class DetailedOption(Option):
    detailName = models.CharField(max_length=50,verbose_name='옵션 세부항목명',null=True,blank=False)
    pricing = models.IntegerField(verbose_name='추가 금액',null=True,blank=False)


    class Meta:
        db_table = 'Options'
        verbose_name = '등록된 옵션'
        verbose_name_plural = '등록된 옵션'

class Cake(models.Model): #원래 Store상속받음
    crn = models.CharField(max_length=50, verbose_name='사업자 등록번호',null=True,blank=False)
    cakeName = models.CharField(max_length=200, verbose_name='케이크 이름',null=False,blank=False,unique=True,default="")
    cakeImg = models.ImageField(verbose_name='케이크 이미지',null=True,blank=True)
    cakePrice = models.IntegerField(verbose_name='1호 기준 가격',null=True,blank=False)
    #mini = models.BooleanField(default=False,verbose_name='미니사이즈 가능 여부',null=True,blank=False)
    mini = models.CharField(max_length=200, verbose_name='미니사이즈 가능 여부', null=False, blank=False, default="",
                            choices=[('가능', '가능'), ('불가', '불가능')])
    #ip = models.CharField(max_length=20,default="",verbose_name='케이크번호')

    class Meta:
        db_table = 'Cake'
        verbose_name = '케이크'
        verbose_name_plural = '케이크'