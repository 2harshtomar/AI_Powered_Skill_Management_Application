from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employeeId = models.CharField(max_length=15)
    mobileNo = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    managerId = models.CharField(max_length=15)
    projectId = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    certificateId = models.CharField(max_length=80)
    certificateSource = models.CharField(max_length=100)
    certificateNumber = models.CharField(max_length=100)
    isVerified = models.BooleanField(default=False)

    def __str__(self):
        return self.certificateId

class SkillDefination(models.Model):
    isCertificateRequired = models.BooleanField(default=False)
    certificate = models.OneToOneField(Certificate, on_delete=models.CASCADE, null=True)
    SkillDescription = models.CharField(max_length=200)
    skillGroup = models.CharField(max_length=10)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='skills', null=True)

    def __str__(self):
        return self.skillGroup
