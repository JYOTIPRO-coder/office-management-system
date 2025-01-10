from django.contrib import admin
from django.urls import path,include
from. import views

urlpatterns = [
    
    path('',views.index,name='index' ),
    path('add-emp',views.add_emp,name='add-emp' ),
    path('del-emp',views.del_emp,name='del-emp' ),
    path('view-emp',views.view_emp,name='view-emp' ),
    path('update-emp',views.update_emp,name='update-emp' ),
    path('update/<int:pk>',views.update_single,name='update' ),
    path('delete',views.del_emp,name='delete' ),
    path('del_singl/<int:pk>',views.del_single,name='del_singl' ),
 
]
