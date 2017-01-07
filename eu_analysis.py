import pandas as pd
import numpy as np
import eu_util as eutil

def get_data_by_country(df,country_iso):
	return df[ df['iso2'] == country_iso]

df = eutil.get_european_cities_dataset()
df_germany = get_data_by_country(df, 'DE')
print(df_germany)