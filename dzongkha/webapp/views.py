from multiprocessing import context
from django.shortcuts import render, redirect
from .models import DzongkhaWord
from django.db.models import Q
from .forms import ContactDetailsForm
import random
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import dzongkhaSerializer

# Create your views here.
class dzongkhaList(APIView):

    def get(self, request):
        dzongkha1= DzongkhaWord.objects.all()
        serializer = dzongkhaSerializer(dzongkha1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

def index(request):
    all_zhebsa = list(DzongkhaWord.objects.all())
    day_zhebsa = random.sample(all_zhebsa,3)[0]
    context = {
        'day_zhebsa': day_zhebsa
    }
    
   

    return render(request, 'webapp/index.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactDetailsForm()
    context = {
        'form': form
    }

    return render(request, 'webapp/contact.html', context)

def about(request):
    return render(request, 'webapp/about.html')

def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        #data = Data.objects.filter(zhebsa__icontains=q)
        multiple_q = Q(Q(zhebsa__icontains=q) | Q(phelkay__icontains=q))
        data = DzongkhaWord.objects.filter(multiple_q)
    else:
        data = ''
    context = {
        'data': data
    }
    return render(request, 'webapp/home.html', context)