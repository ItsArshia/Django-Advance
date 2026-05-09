from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index_view'),
    path('post/', views.PostListView.as_view(), name="post_list"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    # path('go-to-maktabkhooneh', views.RedirectToMaktab.as_view(url="https://maktabkhooneh.org") , name='redirect_test')
    path('post/create', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/remove', views.PostDeleteView.as_view(), name='post-remove'),
]