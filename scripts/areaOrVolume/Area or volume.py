from call_areas import *
from call_volumes import *

a_or_v=input("Do you want to know an area or a volume? ").lower()

if a_or_v=="area":
    call_areas()

elif a_or_v=="volume":
    call_volumes()
    
else:
    print("Your answer must be area or volume.")
