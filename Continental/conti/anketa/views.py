from django.http import HttpResponse

def index(request):
    return HttpResponse ("Toto je moja prvá aplikácia")