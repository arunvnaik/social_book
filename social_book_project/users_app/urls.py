from django.urls import path
from .views import (RegisterView,LoginView,AuthorsSellersView,
upload_books,fetch_data_view,UserFilesView,my_books_view, UserListView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/authors-sellers/', AuthorsSellersView.as_view(), name='authors-sellers-api'),
    path('api/users/', UserListView.as_view(), name='user_list'),
    path('upload-books/', upload_books, name='upload_books'),
    path('fetch-data/', fetch_data_view, name='fetch_data'),
    path('user-files/', UserFilesView.as_view(), name='user_files'),
    path('my-books/', my_books_view, name='my_books'),
    
    

] 


# http://127.0.0.1:8000/auth/token/login/