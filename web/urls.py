from django.urls import re_path
from . import views
from django.urls import path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login$', views.login, name='login'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^addprice/$',views.addprice, name='addprice'),
    re_path(r'^pricelist/$',views.pricelist, name='pricelist'),
    re_path(r'^shopregister/$',views.shopregister, name='shopregister'),
    re_path(r'^stocks/$',views.shopstock, name='stocks'),
    re_path(r'^addshopstock/$',views.addshopstock, name='addshopstock'),
    re_path(r'^stocklist/$',views.shoplist, name='shoplist'),
    re_path(r'^entitle_list/$',views.entitle_list, name='entitle_list'),
    path('update_price/<str:product_name>/', views.update_price, name='update_price'),
    path('update_stock/<int:id>/',views.update_stock, name='update_stock'),
    path('entitlement_update/<int:id>/',views.update_remaining_stock, name='entitlement_update'),
    re_path(r'^collector/$', views.collector_login, name='collector_login'),
    re_path(r'^collector_register/$', views.collector_register, name='collector_register'),
    re_path(r'^collector_index/$', views.collector_index, name='collector_index'),
    re_path(r'^collector_shoplist/$', views.collector_shoplist, name='collector_shoplist'),
    re_path(r'^collector_stocklist/$', views.collector_stocklist, name='collector_stocklist'),
    re_path(r'^collector_pricelist/$', views.collector_pricelist, name='collector_pricelist'),
    re_path(r'^rationshop_officer_register/$', views.rationshop_officer_register, name='rationshop_officer_register'),
    re_path(r'^rationshop/$', views.rationshop_officer_login, name='rationshop'),
    re_path(r'^rationshop_index/$', views.rationshop_officer_index, name='rationshop_index'),
    re_path(r'^e_card/$', views.rationcard_details, name='e_card'),
    re_path(r'^card_entitlement/$', views.entitlement, name='card_entitlement'),
    re_path(r'^rationshop_billing_index/$', views.rationshop_billing, name='rationshop_billing_index'),
    re_path(r'^transaction_details/$', views.transaction_details, name='transaction_details'),
    #re_path(r'^display_details/$', views.display_details, name='display_details'),

 ]