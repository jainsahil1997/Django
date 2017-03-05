from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Department,Subject,Material

# Create your views here.
# python function user interest and give back then request
def index(request):
    all_department=Department.objects.all()
    template=loader.get_template('studyportal/index.html')
    context = {'all_department':all_department}
    #html=''
    #for dept in all_department:
    #    url='/' + str(dept.id) + '/'
    #    html +='<a href="' + url + '">'+ dept.dept_name + '</a><br>'
    #return HttpResponse(template.render(context,request))
    return render(request,'studyportal/index.html',context)
def subject(request,department_id):
    try:
        dept= Department.objects.get(pk=department_id)
    except Department.DoesNotExist:
        raise Http404("Does Not Exist")
    return render(request,'studyportal/detail.html',{'dept':dept})
