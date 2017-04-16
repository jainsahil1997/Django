from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Department,Subject,Material
from django.contrib.auth import authenticate ,login
from django.views.generic import View

# Create your views here.
# python function user interest and give back then request
def index(request):
    all_department=Department.objects.all().order_by('dept_name')
    template=loader.get_template('studyportal/index.html')
    context = {'all_department':all_department}
    #html=''
    #for dept in all_department:
    #    url='/' + str(dept.id) + '/'
    #    html +='<a href="' + url + '">'+ dept.dept_name + '</a><br>'
    #return HttpResponse(template.render(context,request))
    return render(request,'studyportal/index.html',context)
'''
def subject(request,department_id):
    try:
        dept= Department.objects.get(pk=department_id)
    except Department.DoesNotExist:
        raise Http404("Does Not Exist")
    return render(request,'studyportal/detail.html',{'dept':dept})
'''
def subject(request,department_id):
    dept=get_object_or_404(Department,pk=department_id)
    return render(request,'studyportal/detail.html',{'dept':dept})

def material(request,subject_code,department_id):
    subj=get_object_or_404(Subject,code=subject_code)
    dept=get_object_or_404(Department,pk=department_id)
    return render(request,'studyportal/detail1.html',{'subj':subj,'dept':dept})


class MaterialCreate(CreateView):
    model=Material
    fields=['dept_name','code','type','material_desc','material_link','material_file']




def create_material(request):
    form = MaterialForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        material = form.save(commit=False)
        material.save()
        return render(request, 'studyportal/index.html')
    return render(request, 'studyportal/index.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'studyportal/material_.html', {
        'form': form
    })
