from django.shortcuts import render
from .models import TForm
from config.settings import ADMIN_EMAIL
from django.core.mail import send_mail


def input_form_view(request):
    if request.method == 'POST':
        tform = TForm()
        tform.email = request.POST.get('email')
        tform.client_code = request.POST.get('client_code')
        tform.company_name = request.POST.get('company_name')
        tform.mobile_no = request.POST.get('mobile_no')
        tform.city = request.POST.get('city')
        tform.state = request.POST.get('state')
        tform.address = request.POST.get('address')

        if TForm.objects.filter(mobile_no=tform.mobile_no).first() is not None:
            # means the mobile number already exists go for otp
            pass
        else:
            mail_body = f"Hello, " \
                        f"\n A user has requested to create an account. " \
                        f"Following are the details. Please verify and take further steps. " \
                        f"\n Email: {tform.email} " \
                        f"\n Client Code: {tform.client_code} " \
                        f"\n Company Name: {tform.company_name}" \
                        f"\n Mobile Number: {tform.mobile_no}" \
                        f"\n City: {tform.city}" \
                        f"\n State: {tform.state}" \
                        f"\n Address: {tform.address}"
            send_mail(
                "Account Registration Requested",
                mail_body,
                'admin@tripta.com',
                [ADMIN_EMAIL],
            )
            tform.save()
            return render(request, 'success_check.html')

