from django.urls import path
from .views import input_form_view, check_otp_view



urlpatterns = [
    # path("", TFormView.as_view(), name='tform'),
    path('new/', input_form_view, name='final_form'),
    path('enterotp/', check_otp_view, name='otp check'),
]
