from django.shortcuts import render

# Create your views here.
def  home_view(request):
    return render(request,'myresume/index.html')
def skill_view(request):
    return  render(request,'myresume/skill.html')

def  lang_view(request):
    return render(request,'myresume/language.html')
def bio_view(request):
    return  render(request,'myresume/bio.html')
'''
def study_view(request):
    return render(request,'study.html')

def  project_view(request):
    return  render(request,'project.html')



'''