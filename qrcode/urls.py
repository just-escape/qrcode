from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from q import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("scan_admin/<str:instance_slug>/<str:instance_secret>", views.scan_admin),
    path("reset/<str:instance_slug>/<str:instance_secret>", views.reset),
    path("<str:instance_slug>/<str:scan_slug>", views.scan),
]

urlpatterns += staticfiles_urlpatterns()
