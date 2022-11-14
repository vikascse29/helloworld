from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'tutorial'
urlpatterns = [
    path('', views.index, name='index'),
    path('nana/', views.nana, name='nana'),
    path('dock/', views.dock, name='dock'),
    path('postgres/', views.postgres, name='postgres'),
    path('postgresquery/', views.postgresquery, name='postgresquery'),
    path('mysql/', views.mysql, name='mysql'),
    path('dataframe/', views.dataframe, name='dataframe'),
    
    
    #path('admin/', admin.site.urls),
    
    
] 

urlpatterns += staticfiles_urlpatterns()