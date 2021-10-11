from django.urls import path
from hello.models import LogMessage
from hello import views

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("log/", views.log_message, name="log"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("hello/<name>", views.hello_there, name="hello_there"),
]