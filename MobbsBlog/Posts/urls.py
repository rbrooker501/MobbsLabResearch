from django.urls import path
from .views import HomeView, MyPostsView, PostDetailView, PostCreateView, PostEditView, PostDeleteView, LikeView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/edit/<int:pk>', PostEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/remove', PostDeleteView.as_view(), name='post-delete'),
    path('like/<int:pk>', LikeView, name='post-like'),
    path('my_posts', MyPostsView.as_view(), name='my-posts'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment')
]