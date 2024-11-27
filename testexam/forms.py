from django import forms
from .models import Appointment,Question,DiseaseType,DoctorSpec


# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ['type_of_disease', 'type_of_doctor', 'name', 'phone', 'date', 'time', 'message']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#             'time': forms.TimeInput(attrs={'type': 'time'}),
#         }

class AppointmentForm(forms.ModelForm):
    type_of_disease = forms.ModelChoiceField(
        queryset=DiseaseType.objects.all(),  # Barcha kasalliklarni ro'yxatlaydi
        empty_label="Tanlang",  # Default holatda ko'rinadigan yozuv
        label='Type of Disease',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    type_of_doctor = forms.ModelChoiceField(
        queryset=DoctorSpec.objects.all(),  # Barcha shifokorlarni ro'yxatlaydi
        empty_label="Tanlang",  # Default holatda ko'rinadigan yozuv
        label='Type of Doctor',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Appointment
        fields = [
            'type_of_disease',
            'type_of_doctor',
            'name',
            'phone',
            # 'date',
            'message',
        ]
        widgets = {
            # 'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'id_date', 'type': 'date'}),
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
class AppointmentResponseForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['admin_message']  # Faqat admin javobi maydonini qo'shamiz
        widgets = {
            'admin_message': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'form-control'}),
        }
class QuestionForm(forms.Form):
    question = forms.CharField(label='Ask a question', max_length=255)

# telegram_bot

