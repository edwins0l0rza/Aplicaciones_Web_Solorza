from django.urls import path
from GamerV1 import views
from GamerV1.views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='index'),
    path('producto/crear/', views.ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto_delete'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),

]
