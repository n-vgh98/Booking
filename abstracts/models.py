from django.db import models


class AbstractFeature(models.Model):
    title = models.CharField(max_length=128)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractPlace(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    is_valid = models.BooleanField(default=True)
    # address = models.Foreignkey(Address)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
