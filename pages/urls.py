from django.urls import path
from .views import PageCreate, PageListView, PageDetailView, PageUpdate, PageDelete

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/',
         PageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('create/', PageCreate.as_view(), name='create'),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),
], 'pages')
