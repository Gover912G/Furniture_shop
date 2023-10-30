from django.urls import path

from app import views

app_name = "app"
urlpatterns= [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('cart', views.cart, name="cart"),
    path('contact', views.contact, name="contact"),
    path('services', views.services, name="services"),
    path('shop', views.shop, name="shop"),
    path('thank', views.thank, name="thank"),

]