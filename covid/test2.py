import requests

f = requests.get('https://api.covid19india.org/state_district_wise.json').json()

h=(f['Kerala']['districtData'])
for hh in h:
    print(hh,h[hh])
