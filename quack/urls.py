from django.contrib import admin
from django.urls import path, include
from posts import views
from posts.backends import NewRegistrationView

urlpatterns = [

    path('', views.index, name='home'),
    path('api/', include('apiv1.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/register', NewRegistrationView.as_view(), name="register"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),

]
