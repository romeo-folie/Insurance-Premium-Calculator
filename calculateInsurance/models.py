from django.db import models
import uuid

# Create your models here.
class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    make_of_vehicle = models.CharField(max_length = 50)
    type_of_risk = models.CharField(max_length = 50)
    cubic_capacity = models.PositiveIntegerField(blank=True)
    registration_number = models.CharField(max_length = 50)
    chassis = models.CharField(max_length = 50, blank = True)
    engine_number = models.CharField(max_length=50, blank = True)
    year = models.CharField(max_length = 4, blank=True)
    number_of_seats = models.IntegerField()
    license_issued_year = models.CharField(max_length=4)

    def __str__(self):
        return "Car id: {} Risk type: {}".format(self.id,self.type_of_risk)

class Driver(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    insured = models.CharField(max_length= 50)
    address = models.CharField(max_length = 50, blank=True)
    contact_number = models.CharField(max_length=50, blank = True)

    def __str__(self):
        return "Name of User: {} Contact: {}".format(self.insured, self.contact_number)

class Insurance(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable = False)
    type_of_insurance = models.CharField(max_length=50)
    #total_premium_payable = models.IntegerField()
    #premium_per_day = models.FloatField()

    def __str__(self):
        return "Insurance Type: {}".format(self.type_of_insurance)
