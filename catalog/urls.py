

from django.urls import path
from .views import index, BookList,BookDetails
urlpatterns = [
    path('', index, name='catalog' ),
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<uuid:pk>', BookDetails.as_view(), name='book_details')
]