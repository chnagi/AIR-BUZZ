import random
import requests
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
        flno = str(random.randint(10,10000))
        curr = {
        "HarnessLength": random.randint(10,100),
        "GrossWeight": random.randint(1000,5000),
        "AtmosphericPressure": random.randint(10,1000),
        "FuelCapacity_left": random.randint(10,1000),
        "FuelCapacity_right": random.randint(10,1000),
        "FuelQuantity_left": random.randint(10,1000),
        "FuelQuantity_right": random.randint(10,1000),
        "Max_Altitude": random.randint(10,100000),
        "Flight_No": flno,
        "MSN": MSN
        }
        if flno in hap2:
            continue
        data[MSN]["data"].append(curr)
    try:
        r = requests.post('https://airbuscms.herokuapp.com/api/aircraft/', data={"MSN":MSN,"Name":name})
        print(r)
        for fl in data[MSN]["data"]:
            r1 = requests.post('https://airbuscms.herokuapp.com/api/flight/', data=fl)
            print("R!:",r1)
    except Exception as e:
        print("Error:",e)
