from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import logging
from .util import reception_control

logger = logging.getLogger(__name__)

# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# def home(request):
#     print(request.POST)
 
#     return render(request,'users/home.html')



class MyView(View):
    template_name = 'home.html'
    test_result = {
            'type': 'simple',
            'nsample': [0],
            'alimit': [0],
            'rlimit':[0],
            'frisk':0,
            'crisk':0,
            'advice': 'not implemented yet'      
              }
    def _get_mock_data(self):
        self.mckresult =  {
            'type': 'double',
            'nsample': [50,50],
            'alimit': [0,3],
            'rlimit':[3,4],
            'frisk':1.23,
            'crisk':6.52,
            'possible_nqa':[],
            'advice': 'not implemented yet'      
              }
        return self.mckresult
        
    def get(self, request):
        results = ''
        return render(request,'users/home.html')
    
    def post(self, request):
        print(request.POST)
        print(float(request.POST['aqualityl']))
        results = reception_control(float(request.POST['Lot']),float(request.POST['aqualityl']),request.POST['type'])
        print(results)
        return render(request,'users/home.html',context={"results": results})
       
