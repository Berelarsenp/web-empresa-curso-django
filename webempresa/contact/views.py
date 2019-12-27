from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffetiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                'no-contestar@inbox.mailtrap.io', # acá va un mail real que coincida con el servidor que tenemos configurado en settings
                ["berelarsenp@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                # Todo salió bien, redirecionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no salió bien, redirecionamos a FAIL
                return redirect(reverse('contact')+"?fail")
    
    return render(request, "contact/contact.html", {'form':contact_form})