import imp
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home_page),
    path('bloglist/',views.blog_list),
    path('addblog/',views.add_blog),
    path('detailblog/<int:id>/',views.blog_details),
    path('updateblog/<int:id>/',views.update_blog),
    path('deleteblog/<int:id>/',views.delete_blog),
    path('createaccount/', views.create_account),


]
