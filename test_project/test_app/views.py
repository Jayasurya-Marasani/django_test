from django.shortcuts import render
from test_app.models import Program, Student
from test_app.Forms import StudentForm
# Create your views here.
from django.http import HttpResponseRedirect
# 'request' name is convention. It can be some other name too.
# def index(request) :
#   my_dict = { 'message' : "This is an injected content"}
#   return render(request,'index.html',context=my_dict)

# clicked = 1
# def index(request) :
#   global clicked
#   clicked += 1
#   my_dict = {'count' : clicked}
#   return render(request, 'index.html', my_dict)

# def index(request) :
#    fruits = ['apple', 'banana', 'kiwi', 'guava', 'mango']
#    my_dict = { 'fruit_list': fruits }
#    return render(request, 'index.html', my_dict)

program_values = Program.objects.all()
student_values = Student.objects.all()

def index(request):
  my_dict = {
    'program_rows' : program_values,
     'student_rows' : student_values,
  }
  return render(request, 'index.html', my_dict)

def get_student(request):    
  if request.method == 'POST':          
    form = StudentForm(request.POST)     
    if form.is_valid():
        s_name = form.cleaned_data['name']
        s_roll = form.cleaned_data['roll']
        s_degree = form.cleaned_data['degree']        
        s_branch = form.cleaned_data['branch']
        return HttpResponseRedirect('')
  else: 
      form =StudentForm()
      return render(request, 'StudentForm.html', {'form': form})