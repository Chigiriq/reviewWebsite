from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "name",
        "bio",  # Add bio to list_display
        "verifiedReviewer",  # Add verifiedReviewer to list_display
        "is_staff",
    ]

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("name", "bio", "verifiedReviewer")}),  # Add bio and verifiedReviewer to fieldsets
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("name", "bio", "verifiedReviewer")}),  # Add bio and verifiedReviewer to add_fieldsets
    )

admin.site.register(CustomUser, CustomUserAdmin)
