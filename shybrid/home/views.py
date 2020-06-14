from django.shortcuts import render
from django.conf import settings

#Email Modules
from django.core.mail import send_mail, send_mass_mail


def home(request):
    if request.method == "POST":
        print("this is request: ", request.POST['name'])
        print("send email function ")
        # print(request.GET.get('queryform'))
        requester_name = request.POST['name']
        requester_email = request.POST['email']
        requester_sub = request.POST['subject']
        requester_msg = request.POST['message']

        email_from = settings.EMAIL_HOST_USER
        email_to = ['bharath.nr1@gmail.com','bharath.nr1@s-hybrid.com', 
                    'asisbagga@gmail.com', 'asisbagga@s-hybrid.com',
                    'ishnitbagga@s-hybrid.com', ]
        email_admin = settings.EMAIL_ADMIN

        content = 'Customer Query'

        message1 = ('Quote request', 'Have attached the pdf with the required materials', email_from, [email_to])
        message2 = ('New comedian registration', content , email_from, [email_admin])
        #send_mass_mail((message1, message2), fail_silently=False)
        # send_mail(
        #     'Customer Query',
        #     'Here are the details: ',
        #     email_from,
        #     [email_to],
        #     fail_silently=False,
        # ) 
        return render(request, 'thankyou.html')
    else:
        return render(request, 'home.html')


def send_email(request):

    return render(request, 'thankyou.html')