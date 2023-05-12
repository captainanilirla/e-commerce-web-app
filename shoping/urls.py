from django.urls import path
from shoping.views import index,details,cart_view,checkout,return_view,cancel_view
from django.urls import reverse

app_name='shoping'

urlpatterns = [
    path('',index,name='index'),
    path('<int:product_id>/<slug:slug>',details,name='details'),
    path('cart/',cart_view,name='cart_view'),
    path('checkout/',checkout,name='checkout'),
    path('success/',return_view,name='return_view'),
    path('cancel/',cancel_view,name='cancel_view'),
]