from django.urls import path
from . import views
from .views import ( 
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView
)

urlpatterns = [
    
    path('articles/',PostListView.as_view(),name='blog-home'),
    path('user/<str:username>/',UserPostListView.as_view(),name='user-posts'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'), 
    path('',views.gallery,name='blog-gallery'),
    path('info/', views.info,name='blog-info'),
    path('technology/',views.technology,name='technology'),
    path('IOT/',views.IOT,name='IOT'),
    path('New_discoveries/',views.New_discoveries,name='New_discoveries'),
    path('Unspecified/',views.Unspecified,name='Unspecified'),
    
  ] 