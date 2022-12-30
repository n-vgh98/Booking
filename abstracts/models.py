from django.db import models
from django.conf import settings

from abstracts.currencies.models import Currency
from abstracts.locations.models import City
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class AbstractFeature(models.Model):
    title = models.CharField(max_length=128)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractPlace(models.Model):
    title = models.CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_%(class)ss')
    description = models.TextField(null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    address_detail = models.TextField(verbose_name='address detail', )
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    @property
    def get_city_name(self):
        return self.city.name

    @property
    def get_province_name(self):
        return self.city.province.name

    @property
    def get_country_name(self):
        return self.city.province.country.name


class AbstractComment(models.Model):
    CREATED = 10
    APPROVED = 20
    REJECTED = 30
    DELETED = 40
    STATUS_CHOICES = (
        (CREATED, 'Created'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (DELETED, 'Deleted')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='%(class)ss')
    comment_body = models.TextField()

    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=CREATED)
    validated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='validated_%(class)ss')

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractRate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_%(class)ss')
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractRule(models.Model):
    check_in = models.TimeField(verbose_name='check in time')
    check_out = models.TimeField(verbose_name='check out time')
    text = models.TextField(null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractTerminal(models.Model):
    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='terminal_city_%(class)s')
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractPrice(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, related_name='price_currency_%(class)s')
    price = models.FloatField()
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractTicket(models.Model):
    # price
    capacity = models.SmallIntegerField(default=1)
    date_of_departure = models.DateField()
    time_of_departure = models.TimeField()
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, related_name='price_currency_flight_tickets')
    price = models.FloatField()
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractDailyPrice(AbstractPrice):
    SATURDAY = 5
    SUNDAY = 6
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    DAY_CHOICES = (
        (SATURDAY, 'saturday'),
        (SUNDAY, 'sunday'),
        (MONDAY, 'monday'),
        (TUESDAY, 'tuesday'),
        (WEDNESDAY, 'wednesday'),
        (THURSDAY, 'thursday'),
        (FRIDAY, 'friday')
    )
    day = models.PositiveSmallIntegerField(choices=DAY_CHOICES, default=MONDAY)

    class Meta:
        abstract = True


class AbstractSpecialPrice(AbstractPrice):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class AbstractGallery(models.Model):
    name = models.CharField(max_length=52)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractImageGallery(models.Model):
    path = models.ImageField()
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractReservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                             related_name='%(class)s_user_reservations')
    status = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AbstractPassenger(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, ' male'),
        (FEMALE, 'female')
    )
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=32)
    national_id = models.PositiveIntegerField()
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=MALE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
