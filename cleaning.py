import pandas as pd
import re  as r

hoax = pd.read_csv("final_hoaxid.csv", usecols=["title_name"])
filter_hoax1 = hoax[hoax["title_name"].str.contains('SALAH')]
filter_hoax2 = filter_hoax1["title_name"].str.replace('[SALAH]','', regex=False)
filter_hoax3 = filter_hoax2.str.replace('"','')
filter_hoax4 = filter_hoax3.str.lstrip()
print(filter_hoax4)
real = pd.read_csv("detik1.csv", usecols=["title_name"])
real1 = real["title_name"].replace('"','')
print(real1)
# real1.to_csv('clean_real.csv', index=False)

# filter_hoax3.to_csv('clean_hoax.csv', index=False)