
from django.urls import path, re_path, include

from . import views

app_name = 'dockapp'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('nana/', views.nana , name='nana'),
    path('nana/nandocker/', views.nanadocker, name='nanadocker'),
    re_path(r'^nana/nandocker$', views.nanadocker),
]