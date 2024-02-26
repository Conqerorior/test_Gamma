from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from posts.models import Letter, Package


class IndexValidator(serializers.IntegerField):
    def __init__(self):
        super().__init__(
            validators=[
                MinValueValidator(
                    limit_value=100000,
                    message='Индекс должен быть не менее 6 цифр',
                ),
                MaxValueValidator(
                    limit_value=999999,
                    message='Индекс должен быть не более 6 цифр',
                ),
            ]
        )


class LetterSerializer(serializers.ModelSerializer):
    departure_index = IndexValidator()
    destination_index = IndexValidator()
    letter_weight = serializers.IntegerField(
        min_value=1,
        error_messages={'min_value': 'Минимальный вес посылки 1 грамм'},
    )

    class Meta:
        model = Letter
        fields = (
            'id',
            'sender_full_name',
            'recipient_full_name',
            'departure_point',
            'destination_point',
            'departure_index',
            'destination_index',
            'letter_type',
            'letter_weight',
        )


class PackageSerializer(serializers.ModelSerializer):
    departure_index = IndexValidator()
    destination_index = IndexValidator()

    class Meta:
        model = Package
        fields = (
            'id',
            'sender_full_name',
            'recipient_full_name',
            'departure_point',
            'destination_point',
            'departure_index',
            'destination_index',
            'phone',
            'package_type',
            'payment_amount',
        )
