from django.conf.urls import url,include
from django.urls import path
from .views import home,book_list,book_detail,book_create,book_update,dashboard,mylogin,register,mylogout,map
app_name = 'book'
urlpatterns = [
    path('', home, name='home'),
    path('list/',book_list, name='book_list'),
    path('create/',book_create, name='book_create'),
    path('<int:id>/update/',book_update, name='book_update'),
    path('<int:id>/detail/',book_detail, name='book_detail'),
    path('dashboard',dashboard, name='dashboard'),
    path('login',mylogin, name='login'),
    path('register',register, name='register'),
    path('logout',mylogout, name='logout'),
    path('map',map, name='map'),

]