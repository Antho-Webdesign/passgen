from django.urls import path, include
from generator.views import home, listall, deleterecord, search, about, mentions

urlpatterns = [
    path('', home, name='home'),
    path('listall/', listall, name="listall"),
    path('delete/<int:id>', deleterecord, name="deleterecord"),
    path('search', search, name="search"),
    path('a-propos/', about, name="about"),
    path('mentions-legales/', mentions, name="mentions-legales"),
]
