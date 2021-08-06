from collections import namedtuple
from django.urls import path
from .views import*

urlpatterns=[
    path('allcat/',Category,name="all-categories"),
    path('sub/',SubCategory,name="sub-categories"),
    path('sub/create',Create,name="create-form"),
    path('sub/<int:id>/delete',Delete,name="sub-delete"),
    path('sub/<int:id>/update',Update,name="sub-update")
]