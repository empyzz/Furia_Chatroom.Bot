from django import forms
from .models import *
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    profile_image = forms.ImageField(required=False)

    def save(self, request):
        user = super().save(request)
        user.profile_image = self.cleaned_data.get('profile_image')
        user.save()
        return user


class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name', 'description', 'theme']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-bordered w-full', 'placeholder': 'Nome da Sala', 'autocomplete': "off"}),
            'description': forms.Textarea(attrs={'class': 'textarea textarea-bordered w-full', 'rows': 3, 'placeholder': 'Descrição da Sala', 'autocomplete': "off"}),
            'theme': forms.Select(attrs={'class': 'select select-bordered w-full'}),
        }
