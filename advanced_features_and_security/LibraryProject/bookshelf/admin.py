from accounts.models import CustomUser
from accounts.admin import CustomUserAdmin

admin.site.register(CustomUser, CustomUserAdmin)
