import csv
from functions import (output_f,
                        data_dict,
                        get_tree,
                        details_sources,
                        format_date,
                        format_str,
                        format_url,
                       )

import argparse

fast = False

parser = argparse.ArgumentParser(description='Run Scraper.')

parser.add_argument('-f','--fast', help='select fast scraping', type=bool, default=False)
parser.add_argument('-r','--rows', help='limit number of first rows to be scraped', type=int, default=0)
args = parser.parse_args()

supa = get_tree('https://www.againstcovid19.com/singapore/cases/search')
tabular = supa.find_all('tr')
fieldnames = data_dict.keys()

if __name__ == "__main__":
   with open(output_f,'w', newline='') as f:
      csv_writer = csv.DictWriter(f, fieldnames)
      csv_writer.writeheader()
      for i, row in enumerate(tabular):
         if i ==0:
            pass
         else:
            print('working on row no:', i)
            try:
               tabs = row.find_all('td')
               
               if fast != True:
                  ds = details_sources(format_url(tabs[0]))
                  data_dict['Details'] = ds[0]
                  data_dict['Sources'] = ds[1]
               else:
                  data_dict['Details'] = ''
                  data_dict['Sources'] = ''
                  
               data_dict['Case'] = format_str(tabs[0])
               data_dict['Patient'] = format_str(tabs[1])
               data_dict['Age'] = format_str(tabs[2])
               data_dict['Gender'] = format_str(tabs[3])
               data_dict['Nationality'] = format_str(tabs[4])
               data_dict['Status'] = format_str(tabs[5])
               data_dict['Infection_Source'] = format_str(tabs[6])
               data_dict['Country_of_Origin'] = format_str(tabs[7])
               data_dict['Symptomatic_to_Confirmation'] = format_str(tabs[8])
               data_dict['Days_to_Recover'] = format_str(tabs[9])
               data_dict['Symptomatic_At'] = format_date(tabs[10]) #date
               data_dict['Confirmed_At'] = format_date(tabs[11]) #date
               data_dict['Recovered_At'] = format_date(tabs[12]) #date
               data_dict['Displayed_Symptoms'] = format_str(tabs[13])
               
               data_dict['URL'] = format_url(tabs[0])
               csv_writer.writerow(data_dict)
            
               if (args.rows != 0) and (i>= args.rows):
                  break
                  
            except Exception as e:
               print(e)

         
  
