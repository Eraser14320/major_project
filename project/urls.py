"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import classroom
from users import views as users_views
from classroom import views as classroom_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from exam import views as exam_views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',classroom_views.welcome, name='welcome'),
    path('user/', include('users.urls')),
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('thankyou/', exam_views.thankyou, name="exam-thankyou" ),
    path('<str:subject>/', include('classroom.urls')),
    path('<str:subject>/exam/', include('exam.urls'), name='main_exam'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
