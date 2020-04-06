import requests
from bs4 import BeautifulSoup as soup
import datetime

date = datetime.datetime.today()  # datetime object for formating name of the output file
output_f = 'covid19singapore_{year}-{month}-{day}({hour}-{minute}).csv'.format(
   year=date.year,
   month= date.month,
   day=date.day,
   hour=date.hour,
   minute=date.minute,)
   
data_dict = {
      'Case': '',
      'Patient': '',
      'Age': '',
      'Gender': '',
      'Nationality': '',
      'Status': '',
      'Infection_Source': '',
      'Country_of_Origin': '',
      'Symptomatic_to_Confirmation': '',
      'Days_to_Recover': '',
      'Symptomatic_At': '',
      'Confirmed_At': '',
      'Recovered_At': '',
      'Displayed_Symptoms': '',
      'Details': '',
      'Sources': '',
      'URL': '',
   }


def get_tree(url):
   try:
      url = url
      r = requests.get(url)
      return soup(r.text, 'html.parser')
   except Exception as e:
      print('get tree --> ')
      print(e)

      

def details_sources(url):
   try:
      supa = get_tree(url)
      tableRow = supa.find(class_='row row-xs')
      Details_box = tableRow.find(class_='col-lg-8 col-xl-9 mg-t-10')
      Details = Details_box.find(class_='card')
      sources_box = tableRow.find(class_='col-md-6 col-lg-4 col-xl-3 mg-t-10')
      Sources = sources_box.find(class_='card mg-t-10')
      return [Sources.text.replace('Sources', '').strip().replace(' ',''), Details.text.replace('Details', '').strip()]
   except Exception as e:
      print('details sources --> ')
      print(e)


def format_date(a):
   date = a.text.replace('nd', '').replace('th', '').replace('rd','').replace('st','').strip()
   if date != '-':
      date_object = datetime.datetime.strptime(date, '%d, %b %Y')
      return "{}-{}-{}".format(date_object.year, date_object.month, date_object.day)
   else:
      return ''


def format_str(str):
   str = str.text.strip()
   if str != '-':
      return str
   else:
      return ''


def format_url(bs0):
   return 'https://www.againstcovid19.com' + bs0.a['href']