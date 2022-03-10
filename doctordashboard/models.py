from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser



#How to make Keys in specific key

class Clinic(models.Model):
   
    clinicName = models.CharField(max_length=100, blank=True, null=True)
    


class Role(models.Model):
    title =  models.CharField(max_length = 100)
    

class User(AbstractUser):
    clinic = models.ForeignKey(Clinic, on_delete = models.CASCADE)
    role =  models.ForeignKey(Role, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    bday = models.DateField(auto_now=False, auto_now_add=False)
    email =  models.EmailField()
    phone_number =  models.CharField(max_length=8)
    address =  models.CharField(max_length = 50)
   
    MARRIED = 'M'
    SINGLE = 'S'
    DIVORCED = 'D'
    LEGALY_SEPARATED = 'L'
    WIDOWED = 'W'
    MARTIAL_STATUS = [ 
      (MARRIED, 'M'),
      (SINGLE, 'S'),
      (DIVORCED, 'D'),
      (LEGALY_SEPARATED, 'L'0\),
      (WIDOWED, 'W')
     ]
    MartialStatus = models.CharField(max_length=1, blank= True,  choices= MARTIAL_STATUS)
    
   #in case of emergency 
   E_firstName = models.CharField(max_length = 50)
   E_lastName = models.CharField(max_length = 50)
   E_relationship = models.CharField(max_length = 50)
   E_phoneNumber =  models.CharField(max_length=8)
   
   #finance 
   salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
   bank = models.CharField(max_length=50)
   account_number = models.CharField(max_length=20)
   
   #additonal documents 


class Room(models.Model):
    clinic =  models.ForeignKey(Clinic, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)

class Operation(models.Model):
    
    ROOTCANAL = 'RC'
    TOOTHEXTRACTIONS = 'TE'
    PULPOTOMY = 'PU'
    BRIDGE = 'BR'
    SURGERIESTYPES = [
        (ROOTCANAL, 'Root Canal'),
        (TOOTHEXTRACTIONS, 'Tooth Extraction'),
        (PULPOTOMY, 'Pulpotomy'),
        (BRIDGE, 'Bridge'),
    ]
    # serach the clinc by operations it's provide
    # and more for surgerytypes we might add a check list on the dentist sign up  the list of operations he/ she does
    clinic =  models.ManyToManyField(Clinic)
    title = models.CharField(max_length=2, blank= True,  choices= SURGERIESTYPES)
    cost =  models.DecimalField(max_digits=10, decimal_places=2, default=0)




class Patient(models.Model):
    firstName = models.CharField(max_length=100, blank=True, null=True)
    lastName = models.CharField(max_length=100, blank=True, null=True)
    PhoneNumber = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    # birthDate = models.DateField(blank=True, null=True)
    address =  models.CharField(max_length = 50)


class Appointment(models.Model):
    
    #Think more about the relations
    #give each operation an estimated time both the dentist and patient know the time and benefit it
    patient =  models.OneToOneField(Patient, on_delete = models.CASCADE)
    createdby =  models.ForeignKey(User, on_delete = models.CASCADE, related_name='+')
    room = models.OneToOneField(Room, on_delete = models.CASCADE)
    doctor = models.OneToOneField(User, on_delete =  models.CASCADE)
    datetime = models.DateTimeField(blank=True, default=datetime.date.today, null=False)
    duration =  models.DurationField()
    reason =  models.CharField(max_length=100)
    

class Visit(models.Model):
    patient = models.OneToOneField(Patient, on_delete = models.CASCADE)
    room = models.OneToOneField(Room, on_delete = models.CASCADE)
    doctor = models.OneToOneField(User, on_delete =  models.CASCADE)
    datetime = models.DateTimeField(blank=True, default=datetime.date.today, null=False)
    cost =  models.DecimalField(max_digits=10, decimal_places=2, default=0)
    comments = models.CharField(max_length=500)
    
class VisitOperation(models.Model):
    visit = models.OneToOneField(Visit, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation,  on_delete=models.CASCADE)
    cost = models.DecimalField( max_digits=10, decimal_places=2, default= 0)


class JournalEntryType(models.Model):
    title =  models.CharField(max_length=100)
    
    

# paymentjournal link it to the visit
class PaymentJournal(models.Model):
    patient =  models.OneToOneField(Patient, on_delete=models.CASCADE)
    journalentrytype =  models.OneToOneField(JournalEntryType, on_delete =  models.CASCADE)
    clinic =  models.OneToOneField(Clinic, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete = models.PROTECT)
    amount =  models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    reason =  models.CharField(max_length=100)
    
class Login(models.Model):
    username =  models.CharField(max_length = 100)
    password =  models.CharField(max_length = 50)
    

class CreateUserForm(models.Model):
    username =  models.CharField(max_length= 100)
    email =  models.EmailField()
    password1 =  models.CharField(max_length = 50)
    password2 = models.CharField(max_length = 50)
    
