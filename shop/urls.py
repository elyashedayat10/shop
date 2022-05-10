from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("accounts.urls", namespace="account")),
    path("profile/", include("profiles.urls", namespace="profile")),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls")),
                    ]
