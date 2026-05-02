from django.http import HttpResponse


def development(request):
    return HttpResponse("This is the development page.")
