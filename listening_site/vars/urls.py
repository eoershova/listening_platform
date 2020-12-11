from django.urls import path

from . import views
from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    path('', views.index, name='index'),
    path('var1/', views.var1, name='var1'),
    path('var2/', views.var2, name='var2'),
    path('var3/', views.var3, name='var3'),
    path('var4/', views.var4, name='var4'),
    path('var5/', views.var5, name='var5'),
    path('var6/', views.var6, name='var6'),
    path('var7/', views.var7, name='var7'),
    path('var8/', views.var8, name='var8'),
    path('var9/', views.var9, name='var9'),
    path('var10/', views.var10, name='var10'),
    path('var11/', views.var11, name='var11'),
    path('var12/', views.var12, name='var12')
]