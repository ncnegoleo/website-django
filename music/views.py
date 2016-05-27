from django.http import HttpResponse

def index(request):
    return HttpResponse("This is a music home page</h1>")
