from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main_page'),
    path('id=<id>/<slug>', views.menu_detail_MPTT, name='menu_detail_MPTT')
]
