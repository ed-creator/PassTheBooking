from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from .models import Client


def index(request):
    current_user = request.user
    context = {
        'current_user': current_user,
    }
    return render(request, 'client/index.html', context)

# doesnt make sense this view should not exist
def detail(request, client_id):
    current_user = get_object_or_404(Client, pk=client_id)
    return render(request, 'client/detail.html', {'current_user': current_user})
