from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def print_hello(request):
    
    student_data={'students': [{
        'name': 'Fathimath',
        'gender': 'Female',
        'year': 2001,
        'sucess': False
    },
    {
        'name': 'Kadeejath',
        'gender': 'Female',
        
        'sucess': False
    },
    {
        'name': 'Salah',
        'gender': 'Male',
        'year': 2008,
        'sucess': True
    }
    
    ]} 
    return render(request, 'hello.html', student_data)

