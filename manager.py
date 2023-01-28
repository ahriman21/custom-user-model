from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,full_name,email,password,phone=None,city=None,address=None):
        if not email:
            raise ValueError('ایمیل خود را وارد کنید')
        
        if not full_name:
            raise ValueError('نام کامل خود را وارد کنید')

        if len(password) < 4 :
            raise ValueError('گذرواژه دست کم باید 4 کاراکتر باشد')

        user = self.model(full_name=full_name,
                        email=self.normaliza_email(email),
                        phone=phone,
                        city=city,
                        address=address)
        
        user.set_password(password)
        user.role = 'NOR' # normal
        user.save()
        return user

    def create_superuser(self,full_name,email,password,phone=None,city=None,address=None):
        user = self.create_user(full_name,email,password,phone,city,address)
        user.is_staff = True
        user.is_superuser = True
        user.role = 'SUP' # superuser
        user.save()
        return user

    def create_admin(self,full_name,email,password,phone='',city='',address=''):
        user = self.create_user(full_name,email,password,phone,city,address)
        user.is_staff = True
        user.role = 'ADM' # admin
        # user.has_perm('')
        user.save()
        return user
