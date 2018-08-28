
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('paradigms', views.ParadigmView)
router.register('Programmers', views.ProgrammerView)

urlpatterns = [
     path('', include(router.urls)),
     path('api_auth/', include('rest_framework.urls')),

]
