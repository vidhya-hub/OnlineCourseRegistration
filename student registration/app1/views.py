from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,View,UpdateView,ListView,DeleteView
from app1.models import StudentModel
from app1.forms import Studentform,Loginform

class registration(CreateView):
    template_name = "sregistration.html"
    success_url = "/index/"
    model = StudentModel
    form_class = Studentform

class logincheck(FormView):
    template_name = "login.html"
    form_class = Loginform

class validate(View):
    def post(self,request):
        un=request.POST.get("username")
        pa=request.POST.get("password")
        try:
            data=StudentModel.objects.get(email=un,password=pa)
            return render(request,"welcome.html",{"data":data})
        except StudentModel.DoesNotExist:
            return render(request,"login.html",{"error":"invalid user"})
class viewall(ListView):
    template_name = "viewall.html"
    model = StudentModel
    fields = "__all__"
    form_class = Studentform
class update(UpdateView):
    template_name = "update.html"
    model = StudentModel
    fields = "__all__"
    success_url = '/viewall/'

class delete(DeleteView):
    template_name = "delete.html"
    model = StudentModel
    fields= "__all__"
    success_url = '/viewall/'




