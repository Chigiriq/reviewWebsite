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
    list_filter = ("review_request_status", "verifiedReviewer")
    search_fields = ("username", "email")

    actions = ["approve_reviewers", "deny_reviewers"]

    @admin.action(description="Approve selected reviewers")
    def approve_reviewers(self, request, queryset):
        queryset.update(verifiedReviewer=True, review_request_status="Approved")
        self.message_user(
            request, "Selected users have been approved as verified reviewers."
        )

    @admin.action(description="Deny selected reviewers")
    def deny_reviewers(self, request, queryset):
        queryset.update(verifiedReviewer=False, review_request_status="Denied")
        self.message_user(request, "Selected users have been denied verification.")

    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {"fields": ("name", "bio", "verifiedReviewer")},
        ),  # Add bio and verifiedReviewer to fieldsets
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {"fields": ("name", "bio", "verifiedReviewer")},
        ),  # Add bio and verifiedReviewer to add_fieldsets
    )


admin.site.register(CustomUser, CustomUserAdmin)
