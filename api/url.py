from django.urls import path
from . import views


# 'List':'/product-list/',
# 'Detail View':'/product/<str:pk>/',
# 'Create':'/product-add/',
# 'Update':'/product-update/<str:pk>/',
# 'Delete':'/product-delete/<str:pk>/',
		

# url configuration
urlpatterns = [
    path('', views.getall),
    path('product-list/',views.products),
    path('product/<str:pk>/',views.product),
    
    # path('product-list/',views.getProduct),
]
