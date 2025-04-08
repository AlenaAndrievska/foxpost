from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import Textarea

from .models import Comment, ChronicleComment


class ExtendedRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'data-validate': 'requirePassword',
                                                               'placeholder': 'Введите Имя',
                                                               'maxlength': '150'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'data-validate': 'requirePassword',
                                                              'placeholder': 'Введите Фамилию',
                                                              'maxlength': '150'
                                                              }))
    username = forms.CharField(max_length=30, required=True, help_text='Username',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'data-validate': 'requirePassword',
                                                              'placeholder': 'Введите Username',
                                                              'maxlength': '150'
                                                              }))
    email = forms.EmailField(max_length=254, label='e-mail', required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'data-validate': 'requireMail',
                                                           'placeholder': 'Введите email',
                                                           'maxlength': '254'}))
    password1 = forms.CharField(max_length=30, required=True, help_text='password1',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'data-validate': 'requirePassword',
                                                             'placeholder': 'Введите пароль',
                                                             'autocomplete': 'new-password',
                                                             'maxlength': '150'
                                                             }))
    password2 = forms.CharField(max_length=30, required=True, help_text='password2',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'data-validate': 'requirePassword',
                                                             'placeholder': 'Введите пароль',
                                                             'autocomplete': 'new-password',
                                                             'maxlength': '150'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(label=u'Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'data-validate': 'requirePassword',
                                                              'placeholder': 'Введите Username',
                                                              'maxlength': '150'
                                                              }))
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'data-validate': 'requirePassword',
                                                             'placeholder': 'Введите пароль',
                                                             'autocomplete': 'new-password',
                                                             'maxlength': '150'}))

class CommentForm(forms.ModelForm):
    model = Comment

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'class': 'form-textarea',
                                    'placeholder': 'Комментарий',
                                    'id': 'comment'
                                    }
                             ),
        }
        
    
class ChronicleCommentForm(forms.ModelForm):
    model = ChronicleComment

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'class': 'form-textarea',
                                    'placeholder': 'Комментарий',
                                    'id': 'comment'
                                    }
                             ),
        }


