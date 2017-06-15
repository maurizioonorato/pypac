from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),    #Come vedi, stiamo assegnando una view nominata post_list alla URL ^$. Questa espressione regolare combiner�^ (un inizio) seguito da $ (una fine) - cosicch� solo una stringa vuota possa combaciare. � giusto, perch� nei resolver di URL di Django, ' http://127.0.0.1:8000 /' non � una parte dell'URL. Questo schema dir� a Django che views.post_list � il posto giusto dove andare se qualcuno entra nel tuo sito all'indirizzo 'http://127.0.0.1:8000/'.
]