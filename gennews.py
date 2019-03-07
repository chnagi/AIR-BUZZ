import random
import requests
import string
hap = set()
hap2 = set()
data = {}
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

for i in range(100):
    title = id_generator(size=10)
    author =id_generator(size=15)
    body = id_generator(size=1000)
    aur = {
        "Title": title,
        "Author": author,
        "Body": body,
    }
    try:
        r = requests.post('https://airbuscms.herokuapp.com/api/news/', data=aur)
        print(r)
    except Exception as e:
        print("Error:",e)
