from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# 회원가입 시 나타날 field
class CustomUserCreationForm(UserCreationForm):
    birthday = forms.DateField(
        label='',
        required=False,
        widget=forms.DateInput(
        attrs={
            'type': 'date',
        }
        )
    )
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
    username = forms.CharField(
        label='',
        widget= forms.TextInput(
        attrs={
            'placeholder' : '아이디',
        }
        )
    )

    email = forms.EmailField(
        label='',
        widget= forms.EmailInput(
        attrs={
            'placeholder' : '이메일',
        }
        )
    )

    first_name = forms.CharField(
        label='',
        widget=forms.TextInput(
        attrs={
            'placeholder' : '이름',
        }
        )
    )

    last_name = forms.CharField(
        label='',
        widget=forms.TextInput(
        attrs={
            'placeholder' : '성',
        }
        )
    )

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput({
        'placeholder' : '비밀번호'
        }
        )
    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput({
        'placeholder' : '비밀번호 확인'
        }
        )
    )


# 회원정보수정 시 나타날 field
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)


class CustomAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = get_user_model()
        fields = ('username', 'password',)
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
        attrs={
            'placeholder' : '아이디',
        }
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
        {
            'placeholder' : '비밀번호',
        }
        )
    )