from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")        
        message_text = request.POST.get("message")

        # Save to database
        print(request.POST)
        Contact.objects.create(
            name=name,
            email=email,
            subject= subject,
            message=message_text
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('home')

    return render(request, "home.html")
