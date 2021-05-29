from django.shortcuts import render
from .models import TForm


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
        tform.save()

        return render(request, 'success.html')

    return render(request, 'signup.html')

    #
    # submitbutton= request.POST.get("submit")
    # form = InputFormRevamped(request.POST or None)
    # if form.is_valid():
    #     email = form.cleaned_data.get('email')
    #     client_code = form.cleaned_data.get('client_code')
    #     company_name = form.cleaned_data.get('company_name')
    #     mobile_no = form.cleaned_data.get('mobile_no')
    #     city = form.cleaned_data.get('city')
    #     state = form.cleaned_data.get('state')
    #     address = form.cleaned_data.get('address')
    #     print('hello')
    #     form.save(commit=False)
    #
    #     #
    #     # everything = [email, client_code, company_name, mobile_no, city, state, address]
    #     #
    #     # # context= {'form': form, 'email': email, 'city': city,
    #     # #           'submitbutton': submitbutton, 'address': address}\
    #     #
    #     # data_string = str(email) + ' , '
    #     # for x in everything[1:]:
    #     #     data_string += str(x) + ' , '
    #     # data_string += '\n'
    #     # print(data_string)
    #     #
    #     # f = open('data.txt', 'a')
    #     # f.write(data_string)
    #     # f.close()
    #
    # return render(request, 'success.html', context)

