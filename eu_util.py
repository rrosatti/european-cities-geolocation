# the world_cities.csv was taken from http://simplemaps.com/resources/world-cities-data
import pandas as pd
import eu_scraping as eu_scrap
import pickle
from pathlib import Path

data_path = "C:/Users/rodri/OneDrive/Documentos/python/data/world_cities/"

def save_pickle(data, filename):
	with open(data_path+filename, 'wb') as f:
		pickle.dump(data, f)

def get_pickle(filename):
	with open(data_path+filename, 'rb') as f:
		data = pickle.load(f)
	return data

def file_exists(filename):
	if Path(data_path+filename).is_file():
		return True
	else:
		return False

def get_dataset():
	df = pd.read_csv(data_path+'world_cities.csv')
	return df

def get_european_cities_dataset():
	df = get_dataset()
	iso_code = eu_scrap.get_iso_code()
	df2 = df[ df['iso2'].isin(iso_code) ]
	return df2
