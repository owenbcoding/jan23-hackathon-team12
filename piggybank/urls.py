from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django_otp.admin import OTPAdminSite
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin
from django.contrib.admin.views.decorators import staff_member_required
from allauth_2fa.middleware import BaseRequire2FAMiddleware


# Ensure users go through the allauth workflow when logging into admin.
admin.site.login = staff_member_required(admin.site.login, login_url='/accounts/login')
# Run the standard admin set-up.
admin.autodiscover()


class OTPAdmin(OTPAdminSite):
    pass

admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('profiles.urls')),
    path('piggyaccount/', include('piggyaccount.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    # Include the allauth and 2FA urls from their respective packages.
    path('accounts/', include('allauth_2fa.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


class RequireSuperuser2FAMiddleware(BaseRequire2FAMiddleware):
    def require_2fa(self, request):
        # Superusers are require to have 2FA.
        return request.user.username
