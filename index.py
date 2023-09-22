import phonenumbers
from numberinput import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")

print (geocoder.description_for_number(ch_number, "en"))

# Service provider
from phonenumbers import carrier
service_number = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number, "en"))

# Timezone
from phonenumbers import timezone
timeZone = timezone.time_zones_for_number(service_number)
  
# It print the timezone of a phonenumber
print(timeZone)

# Getting Country information
Region = geocoder.description_for_number(service_number,"en")
  
# Printing the region of a phone number
print(Region)
  
# Validating a phone number
valid = phonenumbers.is_valid_number(service_number)
  
# Checking possibility of a number
possible = phonenumbers.is_possible_number(service_number)
  
# Printing the output
print(valid)
print(possible)