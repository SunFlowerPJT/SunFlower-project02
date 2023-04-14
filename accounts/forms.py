from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# 회원가입 시 나타날 field
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'birthday', 'password1', 'password2', 'image')
    # 이미지 100*100 사이즈, media/profile/에 저장됨
    image = ProcessedImageField(
        upload_to='profile/',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality' : 90},
    )


# 회원정보수정 시 나타날 field
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)