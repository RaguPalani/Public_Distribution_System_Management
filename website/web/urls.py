from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^home/$', views.home, name='home'),
    url(r'^addprice/$',views.addprice, name='addprice'),
    url(r'^pricelist/$',views.pricelist, name='pricelist'),
    url(r'^shopregister/$',views.shopregister, name='shopregister'),
    url(r'^stocks/$',views.shopstock, name='stocks'),
    url(r'^stocklist/$',views.shoplist, name='shoplist'),
    path('update_price/<int:id>/', views.update_price, name='update_price'),
    path('update_stock/<int:id>/',views.update_stock, name='update_stock'),
    url(r'^collector/$', views.collector_login, name='collector_login'),
    url(r'^collector_register/$', views.collector_register, name='collector_register'),
    url(r'^collector_index/$', views.collector_index, name='collector_index'),
    url(r'^collector_shoplist/$', views.collector_shoplist, name='collector_shoplist'),
    url(r'^collector_stocklist/$', views.collector_stocklist, name='collector_stocklist'),
    url(r'^collector_pricelist/$', views.collector_pricelist, name='collector_pricelist'),
    url(r'^rationshop_officer_register/$', views.rationshop_officer_register, name='rationshop_officer_register'),


 ]