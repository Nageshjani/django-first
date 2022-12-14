from email.message import EmailMessage
from django.shortcuts import render
from email_reg.forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site  
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from email_reg.token import  account_activation_token
from django.http import HttpResponse  






def signup_form(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.save()
            current_site=get_current_site(request)
            mail_subject ='Activation link has been sent to your email id'  
            message=render_to_string('acc_active_email.html',{

                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user)


            })

            to_email=form.cleaned_data.get('email')

            email=EmailMessage(
                mail_subject,message,to=[to_email]
            )
            email.send()
            return HttpResponse("OPEN EMAIL AND CONFIRM")

    form=SignupForm()
    return render(request,'signup.html',{'form':form})

