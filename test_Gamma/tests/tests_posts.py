from django.test import TestCase
from django.core.exceptions import ValidationError
from rest_framework.exceptions import ErrorDetail

from api.serializers import LetterSerializer, PackageSerializer
from posts.models import Letter, Package


class LetterModelTestCase(TestCase):
    def test_create_letter(self):
        letter_data = {
            'sender_full_name': 'Test Test Test',
            'recipient_full_name': 'Test Test Test',
            'departure_point': 'City A',
            'destination_point': 'City B',
            'departure_index': 123456,
            'destination_index': 654321,
            'letter_type': Letter.LETTER,
            'letter_weight': 10,
        }

        letter = Letter.objects.create(**letter_data)

        self.assertEqual(letter.sender_full_name, 'Test Test Test')
        self.assertEqual(letter.recipient_full_name, 'Test Test Test')

    def test_invalid_letter_creation(self):
        invalid_letter_data = {
            'sender_full_name': 'Test Test Test',
            'recipient_full_name': 'Test Test Test',
            'departure_point': 'City A',
            'departure_index': 123456,
            'destination_index': 654321,
            'letter_type': Letter.LETTER,
            'letter_weight': 10,
        }

        serializer = LetterSerializer(data=invalid_letter_data)

        if not serializer.is_valid():
            print(serializer.errors)

        assert serializer.errors == {
            'destination_point': [
                ErrorDetail(string='Обязательное поле.', code='required')
            ]
        }


class PackageModelTestCase(TestCase):
    def test_create_package(self):
        package_data = {
            'sender_full_name': 'Test Test Test',
            'recipient_full_name': 'Test Test Test',
            'departure_point': 'City A',
            'destination_point': 'City B',
            'departure_index': 123456,
            'destination_index': 654321,
            'phone': '+7834567890',
            'package_type': Package.SMALL_PACKAGE,
            'payment_amount': 50.00,
        }

        package = Package.objects.create(**package_data)

        self.assertEqual(package.sender_full_name, 'Test Test Test')
        self.assertEqual(package.recipient_full_name, 'Test Test Test')

    def test_invalid_package_creation(self):
        invalid_package_data = {
            'sender_full_name': 'Test',
            'recipient_full_name': 'Test',
            'departure_point': 'City A',
            'destination_point': 'City B',
            'departure_index': 123456,
            'destination_index': 654321,
            'phone': '+7 968 777 66 55',
            'package_type': Package.SMALL_PACKAGE,
            'payment_amount': 50.00,
        }

        with self.assertRaises(ValidationError):
            Package.objects.create(**invalid_package_data)


class LetterSerializerTestCase(TestCase):
    def test_valid_letter_serializer(self):
        valid_data = {
            'sender_full_name': 'Test Test Test',
            'recipient_full_name': 'Test Test Test',
            'departure_point': 'City A',
            'destination_point': 'City B',
            'departure_index': 123456,
            'destination_index': 654321,
            'letter_type': Letter.LETTER,
            'letter_weight': 10,
        }

        serializer = LetterSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_letter_serializer(self):
        invalid_data = {
            'sender_full_name': 'Test Test Test',
            'recipient_full_name': 'Test Test Test',
        }

        serializer = LetterSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())


class PackageSerializerTestCase(TestCase):
    def test_valid_package_serializer(self):
        valid_data = {
            'sender_full_name': 'Test Test Test',
            'recipient_full_name': 'Test Test Test',
            'departure_point': 'City A',
            'destination_point': 'City B',
            'departure_index': 123456,
            'destination_index': 654321,
            'phone': '+7 968 777 66 55',
            'package_type': Package.SMALL_PACKAGE,
            'payment_amount': 50.00,
        }

        serializer = PackageSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_package_serializer(self):
        invalid_data = {
            'sender_full_name': 'Test Test Test',
            'recipient_full_name': 'Test Test Test',
        }

        serializer = PackageSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
