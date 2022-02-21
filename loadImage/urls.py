from django.urls import re_path
 
 #importando vistas
from loadImage.views import PrimerLoadImageViewList, PrimerLoadImageViewDetail

urlpatterns=[
    re_path(r'^cargar/$', PrimerLoadImageViewList.as_view()),
    re_path(r'^cargar/(?P<pk>\d+)/$', PrimerLoadImageViewDetail.as_view()),
]