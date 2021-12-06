import json
from django.shortcuts import render
from web.models import Gallery, Category, Contact, Address, Details
from django.http.response import HttpResponse
from django.http.response import JsonResponse


def index(request):
    galleries=Gallery.objects.all()
    categories=Category.objects.all()
    catagory_name=request.GET.get('category')
    adresses=Address.objects.all()
    detailes=Details.objects.all()
    
    context = {
        "galleries" :galleries,
        "categories" :categories,
        "catagory_name":catagory_name,
        "adresses" : adresses,
        "detailes" : detailes
    }

    return render(request,"index.html", context=context)


def contact(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    message = request.POST.get("message")

    if not Contact.objects.filter(email=email).exists():

        Contact.objects.create(
            name = name,
            email = email,
            message = message
        )

        response_data = {
            "status" :"success",
            "message" : "Done",
            "title" : "We will contact you"
        }
    else:
        response_data = {
            "status" :"error",
            "message" : "You are already sent the message. No need to sent again",
            "title" : "We got your message."
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def category(request):
    category_name =request.GET.get('category')
    if category_name:

        if category_name == "All":

            galleries = Gallery.objects.all().values()
            data = list(galleries)  
            response_data = {
                "title" : "success",
                "data" : data,
            }
        elif Category.objects.filter(name=category_name).exists():
            if Gallery.objects.filter(category__name=category_name).exists():
                galleries = Gallery.objects.filter(category__name=category_name).values()
                data = list(galleries)  

                response_data = {
                    "title" : "success",
                    "data" : data,
                }
            else:
                response_data = {
                    "title" : "failed",
                    "message" : "projects not found",
                }
        else:
            response_data = {
                "title" : "failed",
                "message" : "Category not found",
            }
    else:
        response_data = {
            "title" : "failed",
            "message" : "Category not found",
        }

    return JsonResponse({'response_data': response_data})