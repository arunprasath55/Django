import django
from django.shortcuts import render
from django.http import HttpResponse

def mail(request):
    return render(request,'mailapp/index.html')


def result(request):
    mail=request.GET["mail"]
    name_main=mail.split('@')
    domain_with_company=name_main[1]
    domain=domain_with_company.split('.')
    comp=domain[1]
    name=name_main[0]
    

    return render(request,'mailapp/result.html',{'Name':name ,'domain':comp})