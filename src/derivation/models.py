from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class Clinic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PersonalInformation(models.Model):
    OTHER = 'O'
    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = [
        (OTHER, 'Other'),
        (FEMALE, 'Female'),
        (MALE, 'Male')
    ]
    run = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    adress = models.CharField(max_length=50)
    birthday = models.DateField()

    def __str__(self):
        return self.name, self.lastname


class Professional(models.Model):
    personal_information = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % self.personal_information.name, self.personal_information.lastname

    class Meta:
        ordering = ('-created',)


class Patient(models.Model):
    FONASA = 'fon'
    ISAPRE = 'isa'
    OTHER = 'oth'
    INSURANCE_CHOICES = [
        (FONASA, 'Fonasa'),
        (ISAPRE, 'Isapre'),
        (OTHER, 'Other')
    ]
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    personal_information = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE, primary_key=True)
    health_plan_insurance = models.CharField(max_length=3, choices=INSURANCE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % self.personal_information.name, self.personal_information.lastname
    
    class Meta:
        ordering = ('-created',)


class EmergencyContact(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)    
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return "%s %s" % self.name, self.lastname


class TherapySession(models.Model):
    ONLINE = 'onl'
    PRESENTIAL = 'prs'
    MODALITY_CHOICES = [
        (ONLINE, 'Online'),
        (PRESENTIAL, 'Presential')
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    attendance = models.BooleanField()
    pay = models.BooleanField()
    pay_date = models.DateField(auto_now=False, auto_now_add=False)
    modality = models.CharField(choices=MODALITY_CHOICES, max_length=3)

    def __str__(self):
        return "%s %s therapy session date: %s" % self.patient.personal_information.name, self.patient.personal_information.lastname, self.date

    class Meta:
        ordering = ('-date',)



