from django.db import models

# Create your models here.
# username, password, name, email, birth, address

class USerVo(models.Model):
    userid = models.TextField()
    password = models.CharField(max_length=10)
    username = models.TextField()
    name = models.TextField()
    email = models.EmailField()
    birth = models.TextField()
    address = models.TextField()

    class Meta:
        manage = True
        db_table = 'users'

    def __str__(self):
        return  f'[{self.pk}] {self.username}'
