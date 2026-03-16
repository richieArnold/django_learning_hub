"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from core.views import home
from core.views import about
from core.views import contact
from core.views import blogs
from core.views import addCourse
from core.views import viewCourses
from core.views import courseDetail
from core.views import deleteCourse
from core.views import register
from core.views import logout_view
# static files
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blogs/', blogs, name='blogs'),
    path('addCourse/', addCourse, name="addCourse"),
    path('viewCourses/', viewCourses, name="viewCourses"),
    path('course/<int:course_id>/', courseDetail, name="courseDetail"),
    path('deleteCourse/<int:course_id>/', deleteCourse, name="deleteCourse"),
    path('register/', register, name="register"),
    path('logout/', logout_view, name="logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

