from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_details,name='home'),
    path('contact/',views.contact_details,name='contact'),
    path('blog/',views.blog_details,name='blog'),
    path('sign/',views.sign_up,name='sign'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.profile_details,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('update/<int:id>/',views.update_details,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    
]
