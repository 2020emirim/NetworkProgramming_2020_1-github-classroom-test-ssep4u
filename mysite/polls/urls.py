from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # 127.0.0.1:8000/polls/
    path('', views.IndexView.as_view(), name='index'),
    # 127.0.0.1:8000/polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # 127.0.0.1:8000/polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # 127.0.0.1:8000/polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]