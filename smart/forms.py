
from django import forms
from .models import userData1,HistoryModel,VolunteerModel,pictureModel,GalleryModel
from django.contrib.auth.hashers import make_password


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = userData1
        fields = ('username', 'mobile', 'email', 'password')
class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=128)

class pictureModelForm(forms.ModelForm):
    class Meta:
        model=pictureModel
        fields=('pic_name','pic','pic_type')

class historyModelForm(forms.ModelForm):
    class Meta:
        model=HistoryModel
        fields=('form_name','username','email','theme','cake','cradle','decoration','entertainment','balloons','date','location','guest','planner','booked_on','status','suggest')

class volunteerForm(forms.ModelForm):
    class Meta:
        model=VolunteerModel
        fields=('vname','vmobile','vemail','address','role')

class GallerModelForm(forms.ModelForm):
    class Meta:
        model=GalleryModel
        fields=('pic','pic_type')