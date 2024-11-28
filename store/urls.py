from django.urls import path
from .import views 

urlpatterns = [
    path('',views.index , name='home'),
    path('product/<int:id>',views.product , name='product'),
    path('category',views.category , name='category'),
    path('category/<int:cid>',views.category , name='category_name'),
    path('cart',views.cart , name='cart'),
    path('cart/add/<int:pid>',views.cart_ubdate , name='cart_ubdate'),
    path('cart/remove/<int:pid>',views.cart_remove , name='cart_remove'),
    path('checkout',views.checkout , name='checkout'),
    path('checkout_complete',views.checkout_complete , name='checkout_complete'),
]
