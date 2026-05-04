from django.db import models

class temp2(models.Model):
    username = models.CharField(max_length=100,unique=True,blank=False)
    password = models.CharField(max_length=100,blank=False)
    name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=100,unique=True,blank=False)
    mobile=models.CharField(max_length=100,blank=False)
    country=models.CharField(max_length=100,default='India',blank=False)
    state=models.CharField(max_length=100,blank=False)
    district=models.CharField(max_length=100,blank=False)
    country_choices=(
        ('USA', 'USA'),
        ('UK', 'UK'),
        ('India', 'India'),
        ('Japan', 'Japan')
    )
    gender_choice=(
        ('M','Male'),
        ('F','Female'),
        ('O', 'Others')
    )
    gender=models.CharField(max_length=1, choices=gender_choice)
    language_choices=(
        ('English', 'English'),
        ('Spanish', 'Spanish'),
        ('Portuguese', 'Portuguese'),
        ('Roman', 'Roman'),
        ('Russian', 'Russian'),
        ('Swedish','Swedish'),
        ('Hindi', 'Hindi'),
        ('Punjabi','Punjabi'),
        ('Marathi','Marathi')
    )
    language=models.CharField(max_length=20, choices=language_choices)
    class Meta:
        db_table='temp2'
class country(models.Model):
    country=models.CharField(max_length=50)
    class Meta:
        db_table='country'

class states(models.Model):
    country=models.ForeignKey(country,db_column='country',on_delete=models.CASCADE)
    state=models.CharField(max_length=100)
    class Meta:
        db_table='states'

class districts(models.Model):
    state=models.ForeignKey(states,db_column='state',on_delete=models.CASCADE)
    district=models.CharField(max_length=100)
    class Meta:
        db_table = 'districts'
class passwords(models.Model):
    user_id=models.ForeignKey(temp2,db_column='user_data',default=None,on_delete=models.CASCADE)
    website=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    class Meta:
        db_table='passwords'
