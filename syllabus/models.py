from django.db import models

#Use 'python manage.py makemigrations syllabus' to create tables
#Use 'python manage.py shell' to make a shell



class User(models.Model):
    user_id = models.CharField(max_length=200, primary_key=True)
    role = models.CharField(max_length=15)


class Syllabi(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    #semester_held = FALL
    semester_held = models.CharField(max_length=200)
    #semester_year = 2021
    semester_year = models.IntegerField()
    #class_dept = CMSC
    class_dept = models.CharField(max_length=6)
    #class_code = 447
    class_code = models.IntegerField()
    #class_id = CMSC447
    class_id = models.CharField(max_length=200, primary_key=True)
    professor_name = models.CharField(max_length=50)


class Textbook(models.Model):
    class_id = models.ForeignKey(Syllabi, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

