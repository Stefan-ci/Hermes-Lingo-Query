from django import forms
from accounts.models import User



class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        )
    )






class CreateUserForm(forms.Form):
    username = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "pattern": "^[a-zA-Z0-9]{4,}$",
            }
        )
    )
    
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(
            attrs={ 
                "class": "form-control",
                "pattern": "^[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$"
            }
        )
    )
    
    first_name = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    
    last_name = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    
    password = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "pattern": "^(?=.*[a-z])(?=.*[A-Z]).{8,}$",
            }
        )
    )
    
    confirm_password = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "pattern": "^(?=.*[a-z])(?=.*[A-Z]).{8,}$",
            }
        )
    )
    
    class Meta:
        model = User
        fields = ["username", "email", "password", "last_name", "first_name"]

    
    def clean(self):
        cleaned_data = super(CreateUserForm, self).clean()
        if cleaned_data["password"] != cleaned_data["confirm_password"]:
            raise forms.ValidationError("Passwords don't match")
        

    
    def save(self, *args, **kwargs) -> User:
        cleaned_data = super(CreateUserForm, self).clean()
        user = User.objects.create_user(
           first_name=cleaned_data["first_name"],
           last_name=cleaned_data["last_name"],
           username=cleaned_data["username"],
           email=cleaned_data["email"],
           password=cleaned_data["password"]
        )
        return user
