from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("daiphu_website.apps.public.urls")),
    path("accounts/", include("daiphu_website.apps.accounts.urls")),
    path("contact/", include("daiphu_website.apps.contact.urls")),
]
