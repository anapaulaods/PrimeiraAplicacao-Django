from django.urls import path
from . import views

app_name='enquete'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:id_pergunta>/', views.detalhes, name='detalhes'),
	path('<int:id_pergunta>/resultados', views.resultados, name='resultados'),
	path('<int:id_pergunta>/votacao', views.votacao, name='votacao'),
]