from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam, About,Question,DoctorSelf, Service, Contact,DiseaseType,DoctorSpec
from .forms import AppointmentForm,QuestionForm
import openai
from django.contrib import messages # Tasdiq xabarlarini qo'llash uchun
from .models import Appointment, DiseaseType, DoctorSpec
from telegram import Bot
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentResponseForm
from django.contrib.auth.decorators import login_required
from django.conf import settings  # Assuming you are using Django settings for API key management
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

@login_required
def contact_page(request):
    if request.method == 'POST':
        # Formani qayta ishlash
        pass
    return render(request, 'appointment.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('appointment')  # Muvaffaqiyatli kirgandan keyin yo'naltirish
        else:
            return render(request, 'login.html', {'error': 'Noto\'g\'ri username yoki parol'})
    return render(request, 'login.html')

def LogoutView(request):
    logout(request)  # Foydalanuvchini tizimdan chiqarish
    return redirect('login')  # Login sahifasiga yo'naltirish

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            error_message = "Bo'sh joyni to'ldiring"
            return render(request, "register.html", {"error_message": error_message})

        # Foydalanuvchini yaratish va parolni xeshlash
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect("login")
        else:
            error_message = "Bu username allaqachon mavjud"
            return render(request, "register.html", {"error_message": error_message})

    return render(request, "register.html")
def HomeView(request):
    user = request.user  # Hozirgi foydalanuvchi
    context = {
        'user': user,
    }
     # Fetch all Home objects from the database
    return render(request, 'home.html', context)
def ExamView(request):
    results = Exam.objects.all()
    return render(request, 'exam.html',{"exam": results})

def ServiceView(request):
    service = Service.objects.all()
    return render(request, 'service.html',{"service": service})

def ContactView(request):
    contact = Contact.objects.all()
    return render(request, 'contact.html',{"contact": contact})

# test example
def AboutView(request):
    aboutus = About.objects.all()
    return render(request, 'about.html', {"aboutus": aboutus})

# appointment
def AppointmentView(request):
    categories = DiseaseType.objects.all()
    categories2 = DoctorSpec.objects.all()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user  # Foydalanuvchini xabar bilan bog'lash
            form.save()
            messages.success(request, 'So‘rovingiz muvaffaqiyatli yuborildi.')
            return redirect('appointment_success')  # Yuborishdan keyin yo'naltirish
        else:
            messages.error(request, 'Formada xatolik bor, qayta to‘ldiring.')
    else:
        form = AppointmentForm()
        # Form maydonlarini kategoriyalar bilan to'ldirish
        form.fields['type_of_disease'].queryset = categories
        form.fields['type_of_doctor'].queryset = categories2

    return render(request, 'appointment.html', {'form': form, 'categories': categories, 'categories2': categories2})

def Appointment_success(request):
    return render(request, 'appointment_success.html')

# chatgptdan foydalanish


# OpenAI API kalitingizni kiriting


# OpenAI API bilan ishlash
openai.api_key = settings.OPENAI_API_KEY


def ask_question(request):
    answer = ""
    question = ""
    if request.method == 'POST':
        question = request.POST.get('question')  # Foydalanuvchi savol bergan joy
        # Avval bazadan qidirish
        try:
            existing_answer = Question.objects.filter(question__iexact=question).first()
            if existing_answer:
                answer = existing_answer.answer  # Bazadan javobni oling
            else:
                # Agar bazada javob topilmasa, OpenAI'dan foydalanish
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",  # Yoki gpt-4 modeli
                    messages=[{"role": "system", "content": "qaysi tilda yozsam shu tilda javob ber"},
                        {"role": "user", "content": question}],
                    max_tokens=150
                )
                answer = response.choices[0].message['content'].strip()

                # Javobni bazaga saqlash
                Question.objects.create(question=question, answer=answer)
        except Exception as e:
            answer = f"Xatolik: {e}"

    return render(request, 'search.html', {'question': question, 'answer': answer})
# chatgptdan foydalanish


def DoctorSelfViewList(request):
    # Get the 'name' parameter from the GET request
    name_filter = request.GET.get('name', '')
    info_filter = request.GET.get('info', '')
    # Filter products by name if the 'name' parameter is provided
    doctorself = DoctorSelf.objects.all()
    if name_filter:
        doctorself = doctorself.filter(name__icontains=name_filter)
    if info_filter:
        doctorself = doctorself.filter(info__iexact=info_filter)

    # Pass the filtered products to the template
    context = {
        'doctorself': doctorself,
    }

    return render(request, 'doctorself.html', context)


# telegram_bot


def respond_to_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        form = AppointmentResponseForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Javob muvaffaqiyatli yuborildi')
            return redirect('home')  # Adminni ko'rsatish uchun kerakli yo'nalish
        else:
            messages.error(request, 'Javobni yuborishda xatolik bo‘ldi')

    else:
        form = AppointmentResponseForm(instance=appointment)

    return render(request, 'respond_to_appointment.html', {'form': form, 'appointment': appointment})

@login_required
def user_inbox(request):

    user_appointments = Appointment.objects.all()


    context = {
        'appointments': user_appointments,  # Bu erda barcha so'rovlarni yuboramiz
    }
    return render(request, 'user_inbox.html', context)