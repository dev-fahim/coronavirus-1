from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

# Register your models here.

from userApp.models import UserProfile


class UserProfileAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email',  'name', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email',  'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2')
        }),
    )


admin.site.register(UserProfile, UserProfileAdmin)