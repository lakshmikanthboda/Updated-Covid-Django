import requests
g = requests.get('https://api.covid19india.org/data.json').json()

#https://api.covid19india.org/state_district_wise.json

info=['active', 'confirmed', 'deaths', 'lastupdatedtime', 'recovered', 'state']
states = ['Maharashtra', 'Kerala', 'Tamil Nadu', 'Delhi', 'Rajasthan', 'Uttar Pradesh', 'Andhra Pradesh', 'Karnataka', 'Telangana', 'Gujarat', 'Madhya Pradesh', 'Jammu and Kashmir', 'Punjab', 'Haryana', 'West Bengal', 'Bihar', 'Chandigarh', 'Ladakh', 'Assam', 'Andaman and Nicobar Islands', 'Chhattisgarh', 'Uttarakhand', 'Goa', 'Odisha', 'Himachal Pradesh', 'Puducherry', 'Jharkhand', 'Manipur', 'Mizoram', 'Arunachal Pradesh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Lakshadweep', 'Meghalaya', 'Nagaland', 'Sikkim', 'Tripura']
active=[]
confirm=[]
deaths=[]
lastuudate=[]
recovered=[]
state=[]
print(g)
for i in range(0, len(g['statewise'])):
    country_data = g['statewise'][i]
    active.append(country_data['active'])
    confirm.append(country_data['confirmed'])
    deaths.append(country_data['deaths'])
    lastuudate.append(country_data['lastupdatedtime'])
    recovered.append(country_data['recovered'])
    state.append(country_data['state'])
data ={}
for i in range(len(state)):
    data[state[i]]=[active[i],confirm[i],deaths[i],lastuudate[i],recovered[i]]

for st in state:
    print(data[st])

print(data['Total'])