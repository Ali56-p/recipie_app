from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def recipies(request):
    if request.method == "POST":
        data = request.POST

        recipie_image = request.FILES.get('recipie_image')
        recipie_name =data.get('recipie_name')
        recipie_discription = data.get('recipie_discription')

      

        recipie.objects.create(

          recipie_image = recipie_image,
          recipie_name  = recipie_name, 
          recipie_discription  = recipie_discription,
        )
  
        return redirect('/recipies/')
    
    queryset = recipie.objects.all()
    context = {'recipie': queryset}

    
    return render (request, "recipies.html",context)

def update_recipie(request,id):
   queryset = recipie.objects.get(id=id)
   if request.method == "POST":
      data = request.POST

      recipie_image = request.FILES.get('recipie_image')
      recipie_name =data.get('recipie_name')
      recipie_discription = data.get('recipie_discription')

      queryset.recipie_name = recipie_name
      queryset.recipie_discription = recipie_discription

      if recipie_image:
         
        queryset.recipie_image=recipie_image

      queryset.save()    
      return redirect('/recipies/')
 

   context = {'recipiee': queryset}
   return render(request, "update_recipie.html", context)


def delete_recipie(request,id):

  queryset = recipie.objects.get(id = id)
  queryset.delete()

  return redirect('/recipies/')

