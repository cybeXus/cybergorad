from django.shortcuts import render

from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages



from .models import (
    Formation_dev_web, Formation_cybersecurite,
    Formation_reseau, Formation_dev_mobile, Formation_design, Blog
)





def contact(request):
    if request.method == "POST":
        nom = request.user.username  # Nom de l'utilisateur connecté
        email = request.user.email  # Email de l'utilisateur connecté
        message = request.POST.get('message')

        if not email:  # Vérifier si l'utilisateur a bien un email
            messages.error(request, "Vous devez avoir une adresse email pour envoyer un message.")
            return redirect('contact')

        message_envoye = f"Nom: {nom}\nEmail: {email}\nMessage: {message}"

        try:
            send_mail(
                subject=f"Nouveau message de {nom}",
                message=message_envoye,
                from_email=email,  # Utiliser l'email de l'utilisateur connecté
                recipient_list=["rakotoarivonyalifera27@gmail.com"],  # Ton email de réception
                fail_silently=False,
            )
            redirec('home/index.html')
            #messages.success(request, "Votre message a bien été envoyé !")
        except Exception as e:
            print(f"ERROR {e}")
            #messages.error(request, f"Erreur lors de l'envoi : {e}")

    return render(request, 'home/index.html')





def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home/index.html', {'blogs' : blogs })




def formations_dev_web(request):
    formations = Formation_dev_web.objects.all()
    return render(request, 'formations/dev_web.html', {'formations': formations})

def formations_cybersecurite(request):
    formations = Formation_cybersecurite.objects.all()
    return render(request, 'formations/cybersecurite.html', {'formations': formations})

def formations_reseau(request):
    formations = Formation_reseau.objects.all()
    return render(request, 'formations/reseau.html', {'formations': formations})

def formations_dev_mobile(request):
    formations = Formation_dev_mobile.objects.all()
    return render(request, 'formations/dev_mobile.html', {'formations': formations})

def formations_design(request):
    formations = Formation_design.objects.all()
    return render(request, 'formations/design.html', {'formations': formations})
