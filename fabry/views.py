from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from fabrydb.models import Dadosgerais

@login_required
def home(request):
    n = Dadosgerais.objects.count()
    extra_context = {}
    extra_context['nb_patients'] = n
    return render(request, 'site/home_box.html', extra_context)
