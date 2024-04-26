from django.shortcuts import render

# Create your views here.
def  home_view(request):
    return render(request,'myresume/index.html')
def skill_view(request):
    return  render(request,'myresume/skill.html')

def  lang_view(request):
    return render(request,'myresume/language.html')
def bio_view(request):
    context={'my_email':'kmhoseini76@gmail.com','my_phone':'0912-2580590','my_name':"بهار",'my_last_name':'محمدحسینی','my_age':'47'}
    return  render(request,'myresume/bio.html',context)

def study_view(request):
    return render(request,'myresume/study.html')
'''
def  project_view(request):
    return  render(request,'project.html')



'''