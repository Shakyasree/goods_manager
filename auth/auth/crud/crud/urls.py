from django.contrib import admin  
from django.urls import path  
from django.contrib.auth import views as auth_views
from stock import views  
from users import views as user_views
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('add/', views.add),  
    path('show/',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  
