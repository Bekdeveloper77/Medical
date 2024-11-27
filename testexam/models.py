from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SubMenu(models.Model):
    name = models.CharField(max_length=100, blank=True, default="", verbose_name='SubMenu Nomi')
    order = models.CharField(max_length=100, blank=True, default="", verbose_name='Tartib raqami')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Sub_Menyu'
        verbose_name_plural = 'Sub_Menyu'

class Menu(models.Model):
    name = models.CharField(max_length=100, blank=True, default="", verbose_name='Menu Nomi')
    order = models.CharField(max_length=100, blank=True, default="", verbose_name='Tartib raqami')
    submenu = models.ManyToManyField(SubMenu, max_length=500, default="", blank=True, verbose_name='Submenu')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Menyu'
        verbose_name_plural = 'Menyu'
class Exam(models.Model):
    Question = models.CharField(max_length=100, verbose_name='Savol')
    Option1 = models.CharField(max_length=100,  verbose_name='Variant_1')
    Option2 = models.CharField(max_length=100,  verbose_name='Variant_2')
    Option3 = models.CharField(max_length=100,  verbose_name='Variant_3')
    Option4 = models.CharField(max_length=100,  verbose_name='Variant_4')
    Correct = models.CharField(max_length=100,  verbose_name='To‘g‘ri javob')

    def __str__(self):
        return self.Question
    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Test'

# test example


# test example
class OnePage(models.Model):
    img = models.ImageField(upload_to="images/onepage", blank=True, verbose_name="Img")
    topname = models.CharField(max_length=100, blank=True, default="", verbose_name='Top name')
    name = models.CharField(max_length=100, blank=True, default="", verbose_name='Base name')
    text = models.CharField(max_length=200, default="", verbose_name="Text")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'OnePage'
        verbose_name_plural = 'OnePage'

class Service(models.Model):
    icon = models.ImageField(upload_to="images/service", blank=True, verbose_name="Icon")
    name = models.CharField(max_length=100, blank=True, default="", verbose_name='Service Nomi')
    info = models.CharField(max_length=200, blank=True, default="", verbose_name="Info")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Service'

class ServiceTop(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name="Name")
    info = models.CharField(max_length=200, blank=True, verbose_name="Info")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'ServiceTop'
        verbose_name_plural = 'ServiceTop'

class Patients(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name="Sarlavhasi")
    info = models.CharField(max_length=500, verbose_name="Malumoti")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Patients'
        verbose_name_plural = 'Patients'

class Partners(models.Model):
    icon = models.ImageField(upload_to="images/partner", blank=True, verbose_name="Icon")
    name = models.CharField(max_length=100, default="", blank=True, verbose_name='Hamkor Nomi')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Partners'
        verbose_name_plural = 'Partners'

class PartnersTop(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name="Name")
    info = models.CharField(max_length=200, blank=True, verbose_name="Info")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'PartnersTop'
        verbose_name_plural = 'PartnersTop'
class DiseaseType(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'DiseaseType'
        verbose_name_plural = 'DiseaseType'

class DoctorSpec(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'DoctorSpec'
        verbose_name_plural = 'DoctorSpec'


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')  # Foydalanuvchi bilan bog'lash
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    type_of_disease = models.ForeignKey(DiseaseType, on_delete=models.SET_NULL, null=True, verbose_name='Kasallik turi', related_name='disease')
    type_of_doctor = models.ForeignKey(DoctorSpec, on_delete=models.SET_NULL, null=True, verbose_name='Doktor mutaxassisligi', related_name='doctors')
    date = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqti")
    message = models.TextField(blank=True, null=True)
    admin_message = models.TextField(blank=True, null=True, verbose_name="Admin javobi")  # Admin javobi uchun maydon

    def __str__(self):
        return f"{self.name} - {self.date}"

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

class FootetLink(models.Model):
    name = models.CharField(max_length=100, blank=True, default="", verbose_name='Havolalar Nomi')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'FootetLink'
        verbose_name_plural = 'FootetLink'

class FootetLinkTop(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    link = models.ForeignKey(FootetLink, on_delete=models.CASCADE, blank=True, default="", verbose_name="havolalar")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'FootetLinkTop'
        verbose_name_plural = 'FootetLinkTop'

# Inside page

class AboutIn(models.Model):
    name = models.CharField(max_length=100, blank=True, default="", verbose_name='About')
    info = models.CharField(max_length=200, blank=True, default="", verbose_name="Info")
    img = models.ImageField(upload_to="images/about", blank=True, verbose_name="Icon")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'InAbout'
        verbose_name_plural = 'InAbout'

class AboutAchive(models.Model):
    name = models.CharField(max_length=100, blank=True, default="", verbose_name='Achive')
    info = models.CharField(max_length=200, blank=True, default="", verbose_name="Info")
    img = models.ImageField(upload_to="images/about", blank=True, verbose_name="Icon")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'AboutAchive'
        verbose_name_plural = 'AboutAchive'

class Specialist(models.Model):
    name = models.CharField(max_length=100, blank=True, default="", verbose_name='Specialist')
    info = models.CharField(max_length=200, blank=True, default="", verbose_name="Info")
    img = models.ImageField(upload_to="images/specialist", blank=True, verbose_name="Img")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Specialist'
        verbose_name_plural = 'Specialist'

class About(models.Model):
    name = models.CharField(max_length=100, blank=True, default="", verbose_name='About')
    info = models.CharField(max_length=200, blank=True, default="", verbose_name="Info")
    img = models.ImageField(upload_to="images/about", blank=True, verbose_name="Img")
    inabout = models.ManyToManyField(AboutIn, verbose_name="InAbout")
    achive = models.ManyToManyField(AboutAchive, verbose_name='Achive')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

class DoctorSelf(models.Model):
    name = models.CharField(max_length=100, blank=True, default="", verbose_name='DoctorSelf')
    info = models.CharField(max_length=200, blank=True, default="", verbose_name="Info")
    img = models.ImageField(upload_to="images/doctorself", blank=True, verbose_name="Img")
    text = models.CharField(max_length=100, blank=True, default="", verbose_name='Text')
    textinfo = models.CharField(max_length=200, blank=True, default="", verbose_name="Textinfo")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'DoctorSelf'
        verbose_name_plural = 'DoctorSelf'

class Medecine(models.Model):
    name = models.CharField(max_length=100, blank=True, default="", verbose_name='Medecine')
    info = models.CharField(max_length=200, blank=True, default="", verbose_name="Info")
    img = models.ImageField(upload_to="images/medicine", blank=True, verbose_name="Img")
    text = models.CharField(max_length=100, blank=True, default="", verbose_name='Text')
    textinfo = models.CharField(max_length=200, blank=True, default="", verbose_name="Textinfo")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Medecine'
        verbose_name_plural = 'Medecine'

# CHatGpt
class Question(models.Model):
    question = models.CharField(max_length=255, unique=True)  # Not 'query'
    answer = models.TextField()

    def __str__(self):
        return self.question

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, default="", verbose_name='Contact')
    info = models.CharField(max_length=200, blank=True, default="", verbose_name="Contact")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

# telegram_bot


