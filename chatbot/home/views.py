import os
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from home.models import *
import google.generativeai as genai

load_dotenv()
key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=key)
model = genai.GenerativeModel(model_name='gemini-2.5-flash')



# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    message = ""
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        description = request.POST.get("description")


        Contact.objects.create(name=name, mobile=mobile, email=email, description=description)
       
        message = "Your Contact Form has been submitted successfully!"


    return render(request, "contact.html", {"message": message})


def login(request):
    message = ""
    message_type = ""


    if request.method == "POST":
        username= request.POST.get("username")
        password = request.POST.get("password")


        user = Register.objects.filter(username=username, password=password).first()


        if user:
            message = "Login successful!"
            message_type = "success"
            return redirect('chatbot')
        else:
            message = "Invalid username or password."
            message_type = "error"


    return render(request, "login.html", {"message": message, "message_type": message_type})


def register(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")


        Register.objects.create(username=username, name=name, mobile=mobile, email=email, password=password)
       
        message = "User Registered successfully!"
    return render(request, 'register.html', {'message':message})


def chatbot(request):
    response_text = None
    error = None
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '').strip()
        if prompt:
            try:
                chat = model.start_chat()
                result = chat.send_message(prompt)
                response_text = result.text
            except Exception as e:
                error = "Could not get response from Gemini: " + str(e)
    return render(request, 'chatbot.html', {'response': response_text, 'error': error})


def logout(request):
    return render(request, 'logout.html')
    