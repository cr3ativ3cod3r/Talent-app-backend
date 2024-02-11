from django.urls import path
from . import views

urlpatterns = [
	path('', views.ApiOverview, name='home'),
    path('all-items/', views.ItemListView.as_view(), name='list'),
    #'/your-model/?status=value'
    path('create/', views.create.as_view(), name='add'),
    path('Item/<int:pk>/', views.new.as_view(), name='update'),

    
    path('allshows/', views.showlist.as_view(), name='showlist'),
    path('addshow/', views.addshow.as_view(), name='addshow'),
    path('allshows/<int:pk>/', views.reviewshow.as_view(), name='updateshow'),

    path('bookedshows/<int:id_key>', views.showlist.as_view(), name='bookedshow'),
    path('deleteshow/<int:pk>', views.addshow.as_view(), name='deleteshow'),

    path('Register/',views.UserRegistration.as_view(),name='reg'),
    path('Login/',views.userlogin.as_view(),name='log'),
    path('search/',views.Find.as_view(),name='search'),

]
