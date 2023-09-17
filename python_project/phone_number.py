import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("enter your phone number : ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
sim_details = carrier.name_for_number(phone, "en")
register = geocoder.description_for_number(phone, "en")

print( phone , number , time , sim_details , register )



