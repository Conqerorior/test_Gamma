from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BasePostModel(models.Model):
    """
    Создание абстрактной модели для общих полей формы.
    """

    sender_full_name = models.CharField(
        max_length=128, verbose_name="ФИО отправителя"
    )
    recipient_full_name = models.CharField(
        max_length=128, verbose_name="ФИО получателя"
    )
    departure_point = models.TextField(verbose_name="Пункт отправки")
    destination_point = models.TextField(verbose_name="Пункт получения")
    departure_index = models.PositiveIntegerField(
        default=0, verbose_name="Индекс места отправки"
    )
    destination_index = models.PositiveIntegerField(
        default=0, verbose_name="Индекс места получения"
    )

    class Meta:
        abstract = True


class Letter(BasePostModel):
    """
    Модель для представления информации о письмах.
    """

    LETTER = 0
    REGISTERED_LETTER = 1
    VALUABLE_LETTER = 2
    EXPRESS_LETTER = 3
    LETTER_TYPES = (
        (LETTER, "Письмо"),
        (REGISTERED_LETTER, "Заказное письмо"),
        (VALUABLE_LETTER, "Ценное письмо"),
        (EXPRESS_LETTER, "Экспресс-письмо"),
    )
    letter_type = models.PositiveSmallIntegerField(
        default=LETTER, choices=LETTER_TYPES, verbose_name="Тип письма"
    )
    letter_weight = models.PositiveIntegerField(verbose_name="Вес письма")

    class Meta:
        verbose_name = "Письма"
        verbose_name_plural = "Письма"
        ordering = ("sender_full_name",)

    def __str__(self):
        return (
            f"Письмо от: {self.sender_full_name} "
            f"для {self.recipient_full_name}"
        )


class Package(BasePostModel):
    """
    Модель для представления информации о посылках.
    """

    SMALL_PACKAGE = 0
    PACKAGE = 1
    FIRST_CLASS_PACKAGE = 2
    VALUABLE_PACKAGE = 3
    INTERNATIONAL_PACKAGE = 4
    EXPRESS_PACKAGE = 5
    PACKAGE_TYPES = (
        (SMALL_PACKAGE, "Мелкий пакет"),
        (PACKAGE, "Посылка"),
        (FIRST_CLASS_PACKAGE, "Посылка 1 класса"),
        (VALUABLE_PACKAGE, "Ценная посылка"),
        (INTERNATIONAL_PACKAGE, "Посылка международная"),
        (EXPRESS_PACKAGE, "Экспресс-посылка"),
    )
    phone = PhoneNumberField(region="RU", verbose_name="Телефон для извещения")
    package_type = models.PositiveSmallIntegerField(
        default=SMALL_PACKAGE, choices=PACKAGE_TYPES, verbose_name="Тип посылки"
    )
    payment_amount = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="Сумма платежа"
    )

    class Meta:
        verbose_name = "Посылка"
        verbose_name_plural = "Посылки"
        ordering = ("sender_full_name",)

    def __str__(self):
        return (
            f"Посылка от: {self.sender_full_name} "
            f"для {self.recipient_full_name}"
        )
