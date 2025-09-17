#Transportation Mode Selection
#problem: Choose a mode of transportation based on the distance (e.g., <3km:Walk, 3-15km: Bike,>15km:Car)

distance =5
if distance<3:
    transport="Walk"
elif distance <=15:
    transport="Bike"
else:
    transport="Car"

print("AI recommends you the transport of:",transport)