from django.shortcuts import render
from django.http import HttpResponse
import requests
message = ''
from bs4 import BeautifulSoup


def getdata(c):
    global country,count,recovered,deaths,active_cases,recovery_percentage,death_percentage

    # print(country,'now')
    country = c
    data = requests.get('https://www.worldometers.info/coronavirus/country/' + country).text
    soup = BeautifulSoup(data, 'html.parser')
    h = soup.find_all('div', class_='maincounter-number')
    count = h[0].text.strip()
    count = count.replace(',', '')
    deaths = h[1].text.strip()
    deaths = deaths.replace(',', '')
    recovered = h[2].text.strip()
    recovered = recovered.replace(',', '')
    active_cases = int(count) - int(deaths) - int(recovered)
    closed_cases = int(deaths) + int(recovered)
    recovery_percentage = (int(recovered) / int(count)) * 100
    death_percentage = (int(deaths) / int(count)) * 100
    message = {'Country': country, 'No Of Cases': str(count), 'Recovered': str(
        recovered), 'Deaths': str(deaths), 'Active Cases': str(
        active_cases), 'Recovered Cases percentagr': str(recovery_percentage), 'Death Percenrage': str(
        death_percentage)}


# message=str(message[country])
# print(message)

def index(request):
    return HttpResponse((message))



def covidindia(request):
    getdata('india')

    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})


def covidus(request):
    getdata('us')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})

def coviditaly(request):
    getdata('italy')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidspain(request):
    getdata('spain')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidchina(request):
    getdata('china')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidgermany(request):
    getdata('germany')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidiran(request):
    getdata('iran')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidfrancce(request):
    getdata('france')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidswitzer(request):
    getdata('switzerlands')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def coviduk(request):
    getdata('uk')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidnetherlands(request):
    getdata('netherlands')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidaustria(request):
    getdata('austria')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidbelgium(request):
    getdata('belgium')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})

def covidcanada(request):
    getdata('canada')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidturkey(request):
    getdata('turkey')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidportugal(request):
    getdata('portugal')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidnorway(request):
    getdata('norway')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidaustralia(request):
    getdata('australia')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})

def covidbrazil(request):
    getdata('brazil')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidsweden(request):
    getdata('sweden')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})


def covidisrael(request):
    getdata('israel')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidmalaysia(request):
    getdata('malaysia')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def coviddenmark(request):
    getdata('denmark')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidireland(request):
    getdata('ireland')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidpoland(request):
    getdata('poland')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidindonasia(request):
    getdata('indonesia')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidgreece(request):
    getdata('greece')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidphilli(request):
    getdata('philippines')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidiraq(request):
    getdata('iraq')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidhongkong(request):
    getdata('hongkong')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidalgeria(request):
    getdata('algeria')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidsoutjkoria(request):
    getdata('south-korea')
    return render(request,'index.html', {'Country': country.upper(), 'NoOfCases' : str(count), 'Recovered' : str(recovered) ,'Deaths' : str(deaths) ,'ActiveCases' :str(active_cases) , 'RecoveredCasespercentage' : str(recovery_percentage) , 'DeathPercenrage' : str(death_percentage)})
def covidhome(request):
    return render(request, 'home.html')





# Create your views here.
