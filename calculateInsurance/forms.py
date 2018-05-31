from django import forms
from calculateInsurance.models import Car, Driver, Insurance


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('make_of_vehicle','type_of_risk', 'cubic_capacity', 'registration_number',
        'chassis','engine_number', 'year','number_of_seats', 'license_issued_year')
        labels = {'type_of_risk': 'Type of vehicle',}

    def getTypeOfRisk(self):
        all_cleaned_data = super().clean()
        type_of_risk = all_cleaned_data['type_of_risk']
        return type_of_risk

    def getSeatNumber(self):
        all_cleaned_data = super().clean()
        number_of_seats = all_cleaned_data['number_of_seats']
        seatNo = number_of_seats - 5
        return seatNo

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('insured', 'address', 'contact_number')
        labels = {'insured': 'Name',}


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ('type_of_insurance',)

    def getInsuranceType(self):
        all_cleaned_data = super().clean()
        type_of_insurance = all_cleaned_data['type_of_insurance']
        return type_of_insurance
