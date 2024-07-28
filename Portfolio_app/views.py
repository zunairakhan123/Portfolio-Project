from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def project(request):
    projects_show=[
        {
            'title': 'Portfolio',
            'path': 'images/portfolio.PNG',
        },
        {
            'title': 'Blog app',
            'path': 'images/blogapp.PNG',
        },
        {
            'title': 'Rasoi Connect',
            'path': 'images/rasoi_connect.PNG',
        },
        {
            'title': 'Ecommerce',
            'path': 'images/ecommerce.PNG',
        },

        {
            'title': 'Timetable Scheduler',
            'path': 'images/timtable.PNG',
        },
        {
            'title': 'CRUD',
            'path': 'images/CRUD.PNG',
        },        

    ]
    return render (request,"projects.html",{"projects_show": projects_show})

def contact(request):
    return render (request,"contact.html")
