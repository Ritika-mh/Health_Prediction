from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Patient
from .serializers import PatientSerializer
from .gemini_service import generate_health_prediction

class CreatePatient(APIView):

    def post(self, request):

        try:
            serializer = PatientSerializer(data=request.data)

            if serializer.is_valid():

                patient = serializer.save()

                remarks = generate_health_prediction(patient)

                if remarks:
                    patient.remarks = remarks
                else:
                    patient.remarks = "Patient created successfully but AI prediction not available."

                patient.save()

                return Response({
                    "status": True,
                    "message": "Patient created successfully.",
                    "data": PatientSerializer(patient).data
                }, status=status.HTTP_201_CREATED)

            return Response({
                "status": False,
                "message": "Validation error.",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:

            return Response({
                "status": False,
                "message": str(e),
                "data": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdatePatient(APIView):

    def post(self, request):

        try:
            patient_id = request.data.get("id")

            patient = Patient.objects.filter(id=patient_id).first()

            if not patient:
                return Response({
                    "status": False,
                    "message": "Patient not found.",
                    "data": None
                })

            serializer = PatientSerializer(
                patient,
                data=request.data,
                partial=True
            )

            if serializer.is_valid():

                patient = serializer.save()

                remarks = generate_health_prediction(patient)

                if remarks:
                    patient.remarks = remarks
                else:
                    patient.remarks = "Patient updated but AI prediction failed."

                patient.save()

                return Response({
                    "status": True,
                    "message": "Patient updated successfully.",
                    "data": PatientSerializer(patient).data
                }, status=status.HTTP_201_CREATED)

            return Response({
                "status": False,
                "message": "Validation error.",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:

            return Response({
                "status": False,
                "message": str(e),
                "data": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetPatientById(APIView):

    def post(self, request):

        try:
            patient_id = request.data.get("id")

            patient = Patient.objects.filter(id=patient_id).first()

            if not patient:
                return Response({
                    "status": False,
                    "message": "Patient not found.",
                    "data": None
                })

            return Response({
                "status": True,
                "message": "Patient details fetched successfully.",
                "data": PatientSerializer(patient).data
            })

        except Exception as e:

            return Response({
                "status": False,
                "message": str(e),
                "data": None
            })


class GetAllPatients(APIView):

    def post(self, request):

        try:

            patients = Patient.objects.all()

            serializer = PatientSerializer(
                patients,
                many=True
            )

            return Response({
                "status": True,
                "message": "Patient list fetched successfully.",
                "data": serializer.data
            })

        except Exception as e:

            return Response({
                "status": False,
                "message": str(e),
                "data": None
            })


class DeletePatient(APIView):

    def post(self, request):

        try:
            patient_id = request.data.get("id")

            patient = Patient.objects.filter(id=patient_id).first()

            if not patient:
                return Response({
                    "status": False,
                    "message": "Patient not found.",
                    "data": None
                })

            patient.delete()

            return Response({
                "status": True,
                "message": "Patient deleted successfully.",
                "data": None
            })

        except Exception as e:

            return Response({
                "status": False,
                "message": str(e),
                "data": None
            })























           