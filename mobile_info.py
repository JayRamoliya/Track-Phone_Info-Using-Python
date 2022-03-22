import phonenumbers #here import phonenuber -->pip install phonenumbers
"""
here import geocoder
carrier
timezone
"""
from phonenumbers import geocoder, carrier, timezone

# pip install phonenumbers
num=input("enter your number with +91 : ")
#save the number in variable numbers
number = phonenumbers.parse(num)

# this will print the country name
print(geocoder.description_for_number(number,'en'))
#this will print the card info
print(carrier.name_for_number(number,'en'))
#this will print the time 
print(timezone.time_zones_for_number(number))