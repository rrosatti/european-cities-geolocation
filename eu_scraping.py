from bs4 import BeautifulSoup
import eu_util as eutil
import requests, pickle

url = 'http://www.countrycallingcodes.com/iso-country-codes/europe-codes.php'
filename = 'european_iso_codes.pickle'

def get_iso_code():

	if eutil.file_exists(filename):
		iso_codes = eutil.get_pickle(filename)
	else:
		soup = BeautifulSoup(requests.get(url).text, 'html5lib')
		tables = soup.find_all('table')
		# the table I want is the 4th one
		iso_table = tables[3]
		
		# get all tr tags inside the table
		trs = iso_table.find_all('tr')
		iso_codes = []

		# for each tr search for all td tags and get the 2nd (ISO-2)
		for tr in trs:
			tds = tr.find_all('td')
			iso_codes.append(tds[1].text)

		iso_codes = iso_codes[1:]
		eutil.save_pickle(iso_codes, filename)
	
	return iso_codes
