
from django.contrib import admin
from django.urls import path
from django.urls import include
from post.views import *
from post.views import home_view,post_create_view,post_delete_view,post_edit_view,post_detail_view,tag_posts_view
from community.views import community_view
from users.views import profile_view,profile_edit_view,profile_delete_view
from django.conf import settings
from django.conf.urls.static import static
from chat.views import chat_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('community/', include('community.urls')),
    path('accounts/', include('allauth.urls')),
    
    path('', home_view, name='home'),
    # path('', views.home_view, name='home'),
    path('post/create/', post_create_view, name='post-create'),
    path('post/delete/<pk>/', post_delete_view, name='post-delete'),
    path('post/edit/<pk>/', post_edit_view, name='post-edit'),
    path('post/<pk>/', post_detail_view, name='post'),
    path('tag/<slug:slug>/', tag_posts_view, name='tag-posts'),

    path('profile/', profile_view, name='profile'),
    path('community/', community_view, name='community'),
    path('profile/delete/', profile_delete_view, name='profile-delete'),
    path('<username>/', profile_view, name='userprofile'),
    path('profile/edit/', profile_edit_view, name='profile-edit'),
    
    path('comment/sent/<pk>/', comment_sent, name='comment-sent'),
    path('comment/delete/<pk>/', comment_delete_view, name='comment-delete'),
    
    # for chat app
 
    # path('chat/', chat_view, name='chat'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
