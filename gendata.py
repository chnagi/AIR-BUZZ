from random import random
hap = set()
hap2 = set()
data = {}
for i in range(1000):
    MSN = random.randint(1,10000)
    name = 'A'+str(random.randint(100,999))
    if str(MSN) in hap:
        continue
    data[MSN] = {"Name":name,"data":[]}
    for k in range(1000):
        flno =
        curr = {
        "HarnessLength": random.randint(10,100),
        "GrossWeight": random.randint(1000,5000),
        "AtmosphericPressure": random.randint(10,1000),
        "FuelCapacity_left": random.randint(10,1000),
        "FuelCapacity_right": 10000,
        "FuelQuantity_left": 100,
        "FuelQuantity_right": 100,
        "Max_Altitude": 201,
        "Flight_No": "123",
        "MSN": 1
        }
        if hap2
