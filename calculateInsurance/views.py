from django.shortcuts import render
from calculateInsurance import forms
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,'calculateInsurance/index.html')

def result(request):
    # context_dict = {'insPrice': value1, 'insPerDay': value2}
    return render(request, 'calculateInsurance/result.html',{'insPrice':" '' ", 'insPerDay':" '' "})

globalSeatNumber = 0
def calculate_insurance(request):

    insForm = forms.InsuranceForm()
    cForm = forms.CarForm()
    driForm = forms.DriverForm()

# and insForm.is_valid() and cForm.is_valid() and driForm.is_valid()
    if request.method == "POST":
        insForm = forms.InsuranceForm(request.POST)
        cForm = forms.CarForm(request.POST)
        driForm = forms.DriverForm(request.POST)
        insForm.save(commit=True)
        cForm.save(commit=True)
        driForm.save(commit=True)

        #get the seat number and pass it to the global seat number variable
        global globalSeatNumber
        globalSeatNumber = cForm.getSeatNumber()
        print(globalSeatNumber)

        if(insForm.getInsuranceType().lower() == "third party") and (cForm.getTypeOfRisk().lower() == "x1"):
            return render(request, 'calculateInsurance/result.html',{'insPrice': premiumForPrivateThirdParty()[0], 'insPerDay':premiumForPrivateThirdParty()[1], 'carType':"X1", 'insuranceType':"Third Party"})

        elif(insForm.getInsuranceType().lower() == "third party") and (cForm.getTypeOfRisk().lower() == "taxi"):
            return render(request,'calculateInsurance/result.html',{'insPrice': premiumForTaxiThirdParty()[0],'insPerDay': premiumForTaxiThirdParty()[1], 'carType':"Taxi",'insuranceType':"Third Party"})

        elif(insForm.getInsuranceType().lower() == "third party") and (cForm.getTypeOfRisk().lower() == "maxi bus"):
            return render(request,'calculateInsurance/result.html',{'insPrice': premiumForMaxiBusThirdParty()[0],'insPerDay': premiumForMaxiBusThirdParty()[1],'carType': "Maxi Bus", 'insuranceType':"Third Party"})

        elif(insForm.getInsuranceType().lower() == "third party") and (cForm.getTypeOfRisk().lower() == "motor cycle"):
            return render(request,'calculateInsurance/result.html',{'insPrice': premiumForMotorCycleThirdParty()[0],'insPerDay': premiumForMotorCycleThirdParty()[1],'carType': "Motor cycle", 'insuranceType':"Third Party"})

        elif(insForm.getInsuranceType().lower() == "comprehensive") and (cForm.getTypeOfRisk().lower() == "x4"):
            return render(request,'calculateInsurance/result.html',{'insPrice': comprehensivePremiumForX4()[0],'insPerDay': comprehensivePremiumForX4()[1],'carType': "X4", 'insuranceType':"Comprehensive"})

        elif(insForm.getInsuranceType().lower() == "comprehensive") and (cForm.getTypeOfRisk().lower() == "motor cycle"):
            return render(request, 'calculateInsurance/result.html', {'insPrice': comprehensivePremiumForMotorCycles()[0], 'insPerDay': comprehensivePremiumForMotorCycles()[1],'carType': "Motor Cycle", 'insuranceType':"Comprehensive"})

        elif(insForm.getInsuranceType().lower() == "comprehensive") and (cForm.getTypeOfRisk().lower() == "maxi bus"):
            return render(request, 'calculateInsurance/result.html', {'insPrice': comprehensivePremiumForMaxiBus()[0], 'insPerDay': comprehensivePremiumForMaxiBus()[1],'carType': "Maxi Bus", 'insuranceType':"Comprehensive"})
        else:
            return result(request)

    return render(request, 'calculateInsurance/calculate_insurance.html',{'insuranceForm':insForm,'carInfoForm':cForm,'driverInfoForm':driForm})


#Third party insurance premiums
def premiumForPrivateThirdParty():
    """Calculates the premium for a third party X1 vehicle"""
    TP_basic_premium = 210
    TPPDL = 3000
    old_age_loading = TP_basic_premium * 0.05
    inexperienced_driver_loading = 0.1 * TP_basic_premium
    additional_perils = 5
    ecowas_perils = 5
    PA_benefits = 20
    nicNhisNrscEcowas = 12
    extraTTPD = 20
    extraSeatLoading = globalSeatNumber * 5
    firstResult = TP_basic_premium + old_age_loading
    Total = firstResult + extraSeatLoading + inexperienced_driver_loading + extraTTPD + additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
    return [Total,perDay]

def premiumForTaxiThirdParty():
    """Calculates the premium for a third party insured Taxi"""
    TP_basic_premium = 310
    TPPDL = 3000
    old_age_loading = TP_basic_premium * 0.075
    inexperienced_driver_loading = 0
    additional_perils = 5
    ecowas_perils = 10
    PA_benefits = 20
    nicNhisNrscEcowas = 12
    extraTTPD = 20
    extraSeatLoading = 0
    firstResult = TP_basic_premium + old_age_loading
    ncd = firstResult * 0.2
    secondResult = firstResult - ncd
    Total = secondResult + extraTTPD + additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
    perDay = Total/365
    return [Total,perDay]

def premiumForMaxiBusThirdParty():
    """Calculates the premium for a third party MAXI BUS"""
    TP_basic_premium = 320
    TPPDL = 10000
    old_age_loading = TP_basic_premium * 0.05
    inexperienced_driver_loading = 0
    additional_perils = 5
    ecowas_perils = 10
    PA_benefits = 20
    nicNhisNrscEcowas = 12
    extraTTPD = 160
    extraSeatLoading = globalSeatNumber * 8
    firstResult = TP_basic_premium + old_age_loading
    ncd = firstResult * 0.2
    secondResult = firstResult - ncd
    Total = secondResult + extraTTPD + inexperienced_driver_loading + additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
    perDay = Total/365
    return [Total,perDay]

def premiumForMotorCycleThirdParty():
    """Calculates the premium for a third party motor cycle"""
    TP_basic_premium = 110
    TPPDL = 3000
    old_age_loading = 0
    inexperienced_driver_loading = 0.1 * TP_basic_premium
    additional_perils = 5
    ecowas_perils = 10
    PA_benefits = 20
    nicNhisNrscEcowas = 12
    extraTTPD = 160
    extraSeatLoading = globalSeatNumber * 8
    firstResult = TP_basic_premium + old_age_loading
    ncd = firstResult * 0.1
    secondResult = firstResult - ncd
    Total = secondResult + extraTTPD + inexperienced_driver_loading +additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
    perDay = Total/365
    return [Total,perDay]

#Comprehensive insurance premiums
def comprehensivePremiumForX4():
    """Calculates the comprehensive premium for X4 category vehicles"""
    sumInsured = 220000
    ownDamageRate = 0.06
    old_age_loading = 0
    inexperienced_driver_loading = 0
    TP_basic_premium = 210
    extraSeatLoading = 8
    TPPDL = 7500

    ownDamageBasicPremium = sumInsured * ownDamageRate
    cc_loadings = 0.1 * ownDamageBasicPremium

    comprehensiveBasic = ownDamageBasicPremium + cc_loadings + old_age_loading + TP_basic_premium
    ncd = 0.45 * comprehensiveBasic
    fleetDiscount = 0.05 * comprehensiveBasic

    firstResult = comprehensiveBasic - (ncd+fleetDiscount)

    excessBroughtBack = 0.1 * ownDamageBasicPremium
    extraSeatLoading = globalSeatNumber * 8
    inexperienced_driver_loading = 0
    extraTTPD = 110
    additional_perils = 5
    ecowas_perils = 5
    PA_benefits = 20
    nicNhisNrscEcowas = 12

    Total = firstResult + excessBroughtBack + extraSeatLoading + inexperienced_driver_loading + extraTTPD + additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
    perDay = Total/365
    return [Total, perDay]


def comprehensivePremiumForMaxiBus():
    """Calculates the comprehensive premium for maxi buses"""
    sumInsured = 220000
    ownDamageRate = 0.08

    inexperienced_driver_loading = 0
    TP_basic_premium = 320
    extraSeatLoading = 8
    TPPDL = 5000

    ownDamageBasicPremium = sumInsured * ownDamageRate
    cc_loadings = 0.1 * ownDamageBasicPremium
    old_age_loading = 0.05 * ownDamageBasicPremium

    comprehensiveBasic = ownDamageBasicPremium + cc_loadings + old_age_loading + TP_basic_premium

    ncd = 0.2 * comprehensiveBasic
    fleetDiscount = 0.1 * comprehensiveBasic

    firstResult = comprehensiveBasic - (ncd + fleetDiscount)

    excessBroughtBack = 0
    extraSeatLoading = 400
    inexperienced_driver_loading = 0
    extraTTPD = 75
    additional_perils = 5
    ecowas_perils = 5
    PA_benefits = 20
    nicNhisNrscEcowas = 12

    Total = firstResult + excessBroughtBack + extraSeatLoading + inexperienced_driver_loading + extraTTPD + additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
    perDay = Total/365
    return [Total, perDay]

def comprehensivePremiumForMotorCycles():
    """Calculates the comprehensive premium for motor cycles"""
    sumInsured = 15000
    ownDamageRate = 0.03
    old_age_loading = 0
    inexperienced_driver_loading = 0.1
    TP_basic_premium = 110
    extraSeatLoading = 0
    TPPDL = 3000

    ownDamageBasicPremium = sumInsured * ownDamageRate
    cc_loadings = 0 * ownDamageBasicPremium

    comprehensiveBasic = ownDamageBasicPremium + cc_loadings + old_age_loading + TP_basic_premium
    ncd = 0.1 * comprehensiveBasic
    fleetDiscount = 0

    firstResult = comprehensiveBasic - (ncd+fleetDiscount)
    excessBroughtBack = 0
    extraSeatLoading = 0
    inexperienced_driver_loading = 45
    extraTTPD = 20
    additional_perils = 5
    ecowas_perils = 5
    PA_benefits = 20
    nicNhisNrscEcowas = 12

    Total = firstResult + excessBroughtBack + extraSeatLoading + inexperienced_driver_loading + extraTTPD + additional_perils+ ecowas_perils+PA_benefits + nicNhisNrscEcowas
    perDay = Total/365
    return [Total, perDay]
