from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager
from django.urls import reverse
# Create your models here.

ROLES = (
    ('NOR','normal'),
    ('ADM','admin'),
    ('SUP','superuser')
)

class User(AbstractBaseUser,PermissionsMixin):
    full_name = models.CharField(max_length=100,verbose_name='نام و نام خانوادگی')
    email = models.EmailField(unique=True,verbose_name='ایمیل')
    phone = models.CharField(max_length=11,blank=True,null=True,verbose_name='شماره موبایل')
    city = models.CharField(max_length=100,blank=True,null=True,verbose_name='شهر')
    address = models.CharField(max_length=450,blank=True,null=True,verbose_name='ادرس')
    join_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ عضویت')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    _role = models.CharField(choices=ROLES,max_length=3,default='NOR')

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self,role):
        if role not in dict(ROLES):
            raise ValueError('invalid value')
        self._role = role

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.email
    
    # def get_absolute_url(self):
    #     return reverse('account:profile',args=[str(self.id)])

    def save(self, *args, **kwargs):
        role = self.role
        match role:
            case 'NOR':
                self.is_staff = False
                self.is_superuser = False
            case 'ADM':
                self.is_staff = True
                self.is_superuser = False
            case 'SUP':
                self.is_staff = True
                self.is_superuser = True
        super(User, self).save(*args, **kwargs)


