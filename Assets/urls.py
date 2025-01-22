from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import (
    CreateAssetView, assetState, AssetsDetailView, Register,
    viewAssets, adminDashboard, assetmanagerDashboard,
    technicianDashboard, reporterDashboard, auditorDashboard, userDashboard, verificationPage
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.register_or_redirect, name='register_or_redirect'),  # Changed root path
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),

    path('assets/', viewAssets, name='viewAssets'),
    path('asset/<int:pk>/', AssetsDetailView.as_view(), name='assetDetail'),
    path('create/', CreateAssetView.as_view(), name='createAsset'),
    path('asset/<int:pk>/update-state/', assetState, name='assetState'),

    path("assetmanagerDashboard/", views.assetmanagerDashboard, name="assetmanagerDashboard"),
    path("technicianDashboard/", views.technicianDashboard, name="technicianDashboard"),
    path("reporterDashboard/", views.reporterDashboard, name="reporterDashboard"),
    path("auditorDashboard/", views.auditorDashboard, name="auditorDashboard"),
    path("userDashboard/", views.userDashboard, name="userDashboard"),
    path('verification/', verificationPage, name='verification'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
