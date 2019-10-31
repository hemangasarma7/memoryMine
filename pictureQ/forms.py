from django import forms
from django.contrib.auth.models import User
from .models import Album, Photo


class DateWidget(forms.DateInput):
    input_type = 'date'


class AlbumCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AlbumCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['desc'].required = False
        self.fields['date'].required = False
        self.fields['location'].required = False

    class Meta:
        model = Album
        fields = ['title', 'desc', 'date', 'location']
        widgets = {
            'date': DateWidget(),
            'desc': forms.Textarea
        }


class PhotoCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PhotoCreateForm, self).__init__(*args, **kwargs)
        self.fields['album'].required = True
        self.fields['photo_title'].required = True
        self.fields['photo_desc'].required = False
        self.fields['photo_date'].required = False
        self.fields['photo_location'].required = False
        self.fields['image'].required = True

    class Meta:
        model = Photo
        fields = ['album', 'photo_title', 'photo_desc', 'photo_date', 'photo_location', 'image']
        widgets = {
            'photo_date': DateWidget(),
            'photo_desc': forms.Textarea(
                       attrs={'rows': 5,
                              'cols': 40}),
        }


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
