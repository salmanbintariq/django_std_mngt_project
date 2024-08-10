from django.db import models

# Create your models here.
CHOICES = [
    ("IT", "IT"),
    ("MATH", "MATH"),
    ("COMPUTER", "COMPUTER"),
    ("PHYSICS", "PHYSICS")
]

class StudentModel(models.Model):
    student_id = models.CharField(max_length=10, unique=True, blank=True)
    fname = models.CharField("First Name", max_length=30) 
    lname = models.CharField("Last Name", max_length=30)
    email = models.EmailField("Email Address", max_length=30, unique=True)
    department = models.CharField("Department", max_length=20, choices=CHOICES)

    def __str__(self):
        return f"{self.fname} {self.lname} - {self.department}"

    def save(self, *args, **kwargs):
        if not self.student_id:
            last_student = StudentModel.objects.all().order_by('id').last()
            if last_student:
                new_id = int(last_student.student_id) + 1
                self.student_id = f"{new_id:03d}"
            else:
                self.student_id = "001"
        super(StudentModel, self).save(*args, **kwargs)        

