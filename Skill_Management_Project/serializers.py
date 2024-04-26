from rest_framework import serializers
from .models import Employee, Certificate, SkillDefination

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['certificateId', 'certificateSource', 'certificateNumber', 'isVerified']

class SkillDefinationSerializer(serializers.ModelSerializer):
    certificate = CertificateSerializer()  # Include complete certificate information

    class Meta:
        model = SkillDefination
        fields = ['isCertificateRequired', 'certificate', 'SkillDescription', 'skillGroup']
    def create(self, validated_data):
        certificate_data = validated_data.pop('certificate')  # Remove certificate data from validated_data
        certificate = Certificate.objects.create(**certificate_data)  # Create Certificate object
        skill = SkillDefination.objects.create(certificate=certificate, **validated_data)  # Create SkillDefination object
        return skill

class EmployeeSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True, read_only=True)
    skills = SkillDefinationSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ['name', 'employeeId', 'mobileNo', 'email', 'location', 'address', 'managerId', 'projectId', 'certificates', 'skills']
