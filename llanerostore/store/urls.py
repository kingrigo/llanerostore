from django.urls import path
from .views import index, StoreView, StoreDetail
app_name = 'store'
urlpatterns = [
    path('home/', index, name='home'),
    path('tienda/', StoreView.as_view(), name='tienda'),
    path('tienda/<int:pk>', StoreDetail.as_view(), name='detalle'),
    # path('tienda/new', StoreNew.as_view(), name='nuevo'),
    # path('tienda/del/<int:pk>', StoreDelete.as_view(), name='borrar'),
]