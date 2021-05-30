from django.shortcuts import render
from .models import TForm, Email
from django.core.mail import send_mail
from django.shortcuts import redirect
import random
import urllib.request
OTP = random.randint(10000, 99999)
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
        mob_string = str(tform.mobile_no)
        print('ok', OTP, 'this is the OTP')
        final_string = 'https://sms.mobileadz.in/api/push?apikey=5c1237a429cbb&sender=TRIPTA&mobileno=' + mob_string + '&text=Your%20CoreGST.com%20verification%20code%20is%20' + str(OTP)
        print(final_string)
        if TForm.objects.filter(mobile_no=tform.mobile_no).first() is not None:
            webUrl = urllib.request.urlopen(final_string)
            return redirect('/tform/enterotp/')
        else:
            email = Email.objects.get(id=1).admin_email
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
                'admin@tripta.in',
                [email],
            )
            tform.save()
            return render(request, 'success_check.html')

    else:
        return render(request, 'signup.html')


def check_otp_view(request):
    if request.method == 'POST':
        input = request.POST.get('otp')

        if int(input) == OTP:
            return render(request, 'logged_in.html')
        else:
            return redirect('/tform/enterotp/')
    else:
        return render(request, 'otp_verification.html')


