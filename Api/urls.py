from django.conf.urls import url

from Api import views

urlpatterns = [
    # Gestion get/create/delete with all books
    url(r"^api/$", views.book_list),
    # Gestion get/update/delete with one specific book
    url(r"^api/(?P<pk>[0-9]+)$", views.book_detail),
]
