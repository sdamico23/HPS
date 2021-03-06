"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views

app_name = "main"
## path(route, view, kwargs = none, name =None) route is the url pattern, view links to view, kwargs is additional arg to view
# url tells django which page to take you to
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path('register/student/', views.StudentRegisterView.as_view(), name='student_register'),
    path('register/teacher/', views.TeacherRegisterView.as_view(), name='teacher_register'),
    path("logout", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("report/", views.report, name="report"),
    path("account/", views.profile, name="profile"),
    path("reports/", views.reports, name="reports"),
    path("resources/", views.resources, name="resources")

]
