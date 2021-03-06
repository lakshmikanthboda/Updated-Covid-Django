from django.urls import path

from . import views


urlpatterns = [
    path('',views.covidhome, name='covid'),
    path('covid/india', views.covidindia, name='covid'),
path('covid/italy', views.coviditaly, name='covid'),
    path('covid/us', views.covidus, name='covid'),
    path('covid/spain', views.covidspain, name='covid'),
    path('covid/china', views.covidchina, name='covid'),
path('covid/germany', views.covidgermany, name='covid'),
path('covid/iran', views.covidiran, name='covid'),
path('covid/france', views.covidfrancce, name='covid'),
path('covid/switzerland', views.covidswitzer, name='covid'),
path('covid/uk', views.coviduk, name='covid'),
path('covid/netherlands', views.covidnetherlands, name='covid'),
path('covid/austria', views.covidaustria, name='covid'),
path('covid/belgium', views.covidbelgium, name='covid'),
path('covid/canada', views.covidcanada, name='covid'),
path('covid/turkey', views.covidturkey, name='covid'),
path('covid/portugal', views.covidportugal, name='covid'),
path('covid/norway', views.covidnorway, name='covid'),
path('covid/australia', views.covidaustralia, name='covid'),
path('covid/brazil', views.covidbrazil, name='covid'),
path('covid/sweden', views.covidsweden, name='covid'),
path('covid/israel', views.covidisrael, name='covid'),
path('covid/malaysia', views.covidmalaysia, name='covid'),
path('covid/denmark', views.coviddenmark, name='covid'),
path('covid/ireland', views.covidireland, name='covid'),
path('covid/poland', views.covidpoland, name='covid'),
path('covid/indonesia', views.covidindonasia, name='covid'),
path('covid/greece', views.covidgreece, name='covid'),
path('covid/phillipines', views.covidphilli, name='covid'),
path('covid/iraq', views.covidiraq, name='covid'),
path('covid/hongkong', views.covidhongkong, name='covid'),
path('covid/algeria', views.covidalgeria, name='covid'),
path('covid/southkorea', views.covidsoutjkoria, name='covid'),
    path('covid/india/states',views.alldata,name='all')
]