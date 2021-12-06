from django.urls import path
from web.views import contact, index, category


app_name = "web"

urlpatterns = [
    path("",index,name="index"),
    path("contact/",contact,name="contact"),
    path("category/",category,name="category"),
]