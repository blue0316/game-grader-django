from django import forms
from core.models import User, InviteTeam
from django.contrib.auth import password_validation
from django.utils.translation import gettext as _


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget = forms.PasswordInput)

    password=forms.CharField(widget=forms.PasswordInput(),help_text=password_validation.password_validators_help_text_html())


    class Meta:
        model = User
        fields = ['profile_pic','username','email','password','confirm_password']

        # Widgets = {
        #     'username':forms.TextInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
        #                                     'id':'input-group-1','name':'username', 'placeholder':'Enter name'}),
        #     'email':forms.TextInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
        #                                     'id':'input-group-1','name':'email', 'placeholder':'Enter email'}),
        #     'password':forms.TextInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
        #                                     'id':'password', 'name':'password', 'placeholder':'Enter password'}),
        #     'confirm_password':forms.TextInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
        #                                     'id':'password', 'name':'confirm_password', 'placeholder':'Enter confirm password'}),
        # }

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(_("The two password fields did not match."))
            password_validation.validate_password(password,None)
        return confirm_password

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

class InviteTeamForm(forms.ModelForm):
    class Meta:
        model = InviteTeam
        fields = []




        # forms.py
# class ProductForm(ModelForm):
#     class Meta:
#         model = Product
#         exclude = ('updated', 'created')

#     def __init__(self, args, *kwargs):
#         super(ProductForm, self).__init__(*args, **kwargs)
#         self.fields['description'].widget = TextInput(attrs={
#             'id': 'myCustomId',
#             'class': 'myCustomClass',
#             'name': 'myCustomName',
#             'placeholder': 'myCustomPlaceholder'})