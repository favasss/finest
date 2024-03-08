from django.urls import path
from finalapp import views
app_name = 'finalapp'
urlpatterns = [

    path('',views.register,name='register'),
    path('home',views.home,name='home'),
    path('login.html',views.login,name='login'),
    path('browse.html',views.browse,name='browse'),
    path('mypc/<int:mypc_id>/',views.detail,name='detail'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('logout',views.logout,name='logout')
]
