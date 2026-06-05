from rest_framework import serializers
from datetime import date
import re

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['remarks']

    def validate(self, data):
        full_name=data.get('full_name', '').strip()
        email=data.get('email', '').strip().lower()

        if full_name and email:
            if full_name=="Google" and email=="google@gmail.com":
                raise serializers.ValidationError(
                    "Invalid google full name and email."
                )
    def validate_full_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Full name is required."
            )

        # if value=="Google":
        #     raise serializers.ValidationError(
        #         "Google is not a valid name."
        #     )
        if len(value) < 3:
            raise serializers.ValidationError(
                "Full name must be at least 3 characters."
            )

        if not re.match(r'^[A-Za-z ]+$', value):
            raise serializers.ValidationError(
                "Full name should contain only letters and spaces."
            )

        return value

    def validate_dob(self, value):

        if value > date.today():
            raise serializers.ValidationError(
                "Date of birth cannot be a future date."
            )

        age = date.today().year - value.year

        if age > 120:
            raise serializers.ValidationError(
                "Invalid date of birth."
            )

        return value

    def validate_glucose(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Glucose must be greater than 0."
            )

        if value > 1000:
            raise serializers.ValidationError(
                "Invalid glucose value."
            )

        return value

    def validate_haemoglobin(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Haemoglobin must be greater than 0."
            )

        if value > 30:
            raise serializers.ValidationError(
                "Invalid haemoglobin value."
            )

        return value

    def validate_cholesterol(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Cholesterol must be greater than 0."
            )

        if value > 1000:
            raise serializers.ValidationError(
                "Invalid cholesterol value."
            )

        return value

    def validate_email(self, value):

        email = value.strip().lower()

        patient_id = self.instance.id if self.instance else None

        if Patient.objects.filter(email=email).exclude(id=patient_id).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )

        return email