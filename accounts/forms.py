from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Setup based on Django for Professionals with some additional fields
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'is_staff', 'last_login')
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'is_staff', 'last_login')