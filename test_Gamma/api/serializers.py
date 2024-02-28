from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)
from rest_framework import serializers

from posts.models import Letter, Package


class FullNameValidator(serializers.CharField):
    """
    Валидатор для проверки корректности формата ФИО.

    Проверяет, что значение поля ФИО состоит из букв и пробелов,
    а также содержит как минимум три компонента: Фамилия, Имя, Отчество.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(
            validators=[
                RegexValidator(
                    regex=r'^[a-zA-Zа-яА-Я\s]+$',
                    message='Некорректный формат ФИО. '
                    'Используйте только буквы и пробелы',
                )
            ],
            *args,
            **kwargs
        )

    def run_validators(self, value):
        super().run_validators(value)
        self.validate_sender_full_name(value)

    @staticmethod
    def validate_sender_full_name(value):
        components = value.split()
        if len(components) < 3:
            raise serializers.ValidationError(
                'Введите полное ФИО: Фамилия Имя Отчество'
            )


class IndexValidator(serializers.IntegerField):
    """
    Валидатор для проверки корректности формата почтового индекса.

    Проверяет, что значение поля индекса состоит из 6 цифр и находится
    в диапазоне от 100000 до 999999.
    """

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


class BaseSerializer(serializers.ModelSerializer):
    """
    Абстрактный сериализатор, предоставляющий общие поля д
    ля моделей с отправителями и индексами.

    """

    sender_full_name = FullNameValidator()
    recipient_full_name = FullNameValidator()
    departure_index = IndexValidator()
    destination_index = IndexValidator()

    class Meta:
        abstract = True


class LetterSerializer(BaseSerializer):
    """
    Сериализатор для модели Letter.
    """

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


class PackageSerializer(BaseSerializer):
    """
    Сериализатор для модели Package.
    """

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
