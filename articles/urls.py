from django.urls import path
from articles import views

urlpatterns = [
    path('<int:category_id>/',views.ArticleListView.as_view(), name = 'article_detail_view'),
    path('detail/<int:article_id>/', views.ArticleDetailView.as_view(), name='article_detail_view'),
    path('detail/<int:article_id>/comment/', views.CommentView.as_view(), name='comment_view'),
    path('detail/<int:article_id>/comment/<int:comment_id>/', views.CommentDetailView.as_view(), name='comment_detail_view'),
    path('detail/<int:article_id>/likes/', views.ArticleLikes.as_view(), name='article_likes'),
    path('detail/<int:article_id>/comment/<int:comment_id>/likes/', views.CommentLikes.as_view(), name='comment_likes'),
    path('<int:user_id>/user_article/',views.ArticleUserView.as_view(), name = 'article_user_view'),
    path('detail/<int:article_id>/bookmark/', views.BookMarkView.as_view(), name='bookmark_view'),
    path('bookmark/<int:user_id>/', views.BookMarkView.as_view(), name='bookmark_view'),
]