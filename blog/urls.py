from . import views
from django.urls import path

urlpatterns = [
    path('blog/', views.PostHome.as_view(), name='blog_home'),
    path('blog/all', views.PostList.as_view(), name='blog_all'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='blog_detail'),
]