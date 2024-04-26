from django.http import JsonResponse
from .models import Employee, Certificate, SkillDefination
from .serializers import EmployeeSerializer, SkillDefinationSerializer, CertificateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET','POST'])
def certificate_list(request):
    if request.method == 'GET':
        certificates = Certificate.objects.all()
        serializer = CertificateSerializer(certificates, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = CertificateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET','POST'])
def Skill_list(request):
    if request.method == 'GET':
        skills = SkillDefination.objects.all()
        serializer = SkillDefinationSerializer(skills, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = SkillDefinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def getEmployeeByID(request, employeeId):

    try:
        empoyee = Employee.objects.get(employeeId = employeeId)
    except Employee.DoesNotExist:
        return  Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serilizer = EmployeeSerializer(empoyee)
        return Response(serilizer.data)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass