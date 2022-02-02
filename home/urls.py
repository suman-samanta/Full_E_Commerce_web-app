from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("contact",views.contact, name='contact'),
    path("login",views.loginuser,name='login'),
    path("logout",views.logoutuser,name='logout'),
    path("signup",views.signup,name='signup'),
    path("add_a_product",views.add_a_product,name='add_a_product'),
    path("product_view/<str:pd_nm>",views.product_view,name='product_view'),
    path("add_to_cart/<str:pd_nm>",views.add_to_cart,name='add_to_cart'),
    path("mycart",views.mycart,name='mycart'),
    path("remove_cart/<str:pd_nm>",views.remove_product_from_cart,name='remove_cart'),
    path("order_now/<str:pd_nm>",views.buy_now,name='order_now'),
    path("place_order/<str:pd_nm>",views.order_place,name='place_order'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)