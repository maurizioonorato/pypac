from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),    #Come vedi, stiamo assegnando una view nominata post_list alla URL ^$. Questa espressione regolare combinerà^ (un inizio) seguito da $ (una fine) - cosicché solo una stringa vuota possa combaciare. È giusto, perché nei resolver di URL di Django, ' http://127.0.0.1:8000 /' non è una parte dell'URL. Questo schema dirà a Django che views.post_list è il posto giusto dove andare se qualcuno entra nel tuo sito all'indirizzo 'http://127.0.0.1:8000/'.
]