from django.contrib import admin
from django.urls import path,include
from task_manager.views import task_list,Update_task,delete_task,user_login,user_sign_up,user_logout,add_task

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',task_list,name="task_list"),
    path("add_task/",add_task,name="add_task"),
    path('update/<int:task_id>',Update_task,name="update_task"),
    path('delete/<int:task_id>',delete_task,name="delete_task"),
    path("login/",user_login,name="login"),
    path("signup/",user_sign_up,name="sign_up"),
    path("logout/",user_logout,name="logout"),
]