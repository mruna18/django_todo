from django.urls import path
from . import views

urlpatterns=[
  path('', views.home, name='home'),
  path('add/', views.add, name='add'),
  path('history/', views.history, name='history'),
  path('edit/<int:pk>',views.edit, name='edit'),
  path('delete/<int:pk>',views.delete_, name='delete_'),
  path('history_delete/<int:pk>',views.his_del, name='his_del'),
  path('history_restore/<int:pk>',views.restore, name='restore'),
  path('history_deleteAll',views.del_all, name='del_all'),
  path('history_restore_all',views.restore_all, name='restore_all'),
]