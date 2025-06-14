from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('sales/', views.ListSalesView.as_view(), name='sales'),
    path('sales/<int:pk>/detail/', views.DetailSalesView.as_view(), name='detail'),
    path('sales/create/', views.CreateSalesView.as_view(), name='create'),
    path('sales/<int:pk>/delete/', views.DeleteSalesView.as_view(), name='delete'),
    path('sales/<int:pk>/update/', views.UpdateSalesView.as_view(), name='update'),
]
