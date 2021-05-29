from django.urls import path
from .views import input_form_view

urlpatterns = [
    # path("", TFormView.as_view(), name='tform'),
    path('new/', input_form_view),
]
