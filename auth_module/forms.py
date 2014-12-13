from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from auth_module.models import MetadataUser

class MetadataUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MetadataUserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    class Meta:
        model = MetadataUser
        fields = ('email',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(MetadataUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class MetadataUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(MetadataUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    class Meta:
        model = MetadataUser
        fields = []