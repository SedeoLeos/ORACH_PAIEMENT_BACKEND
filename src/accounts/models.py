from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db.models.signals import  post_save
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active',False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    sexeChoice = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
        
    )
    professionChoice =(
        ('Etudiant','Etudiant'),
        ('Professionnelle','Professionnelle'),
        ('Expert','Expert'),
    )
    fonctionChoice =(
        ("DRH","Directeur Ressource humaine"),
        ("DRH","Directeur Ressource humaine"),
        ("DRH","Directeur Ressource humaine"),
        ("DRH","Directeur Ressource humaine"),
        ("DRH","Directeur Ressource humaine"),
    )
        
    
    username = None
  
    sexe =models.CharField(max_length=20,choices=sexeChoice,default=sexeChoice[0])
    dateNaiss =models.DateField(null=True)
    profession=models.CharField(max_length=40,choices=professionChoice,default=professionChoice[0])
   
    telephone=models.IntegerField(null=True)
    fonction=models.CharField(max_length=40,choices=fonctionChoice,default=fonctionChoice[0])
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    def __str__(self):
        return self.first_name
   


    
class cotisation (models.Model):
    montant = models.FloatField()
    mois = models.CharField(max_length=20)  
    def __str__(self):
            return self.mois
   
      
class versement(models.Model):
    montant = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    tel = models.CharField(max_length=10)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    cotisation = models.ForeignKey(cotisation,on_delete=models.CASCADE)   
#post_save.connect(modifierCompte,sender=Cotisation)

