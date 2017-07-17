import urllib

base_url = 'https://api.census.gov/data/'
yr = raw_input('year: ')
vs = raw_input('variable (e.g., STNAME): ')
mnth = raw_input('month (as a number): ')
st = raw_input('state abbr (can be ALL): ')

if (st == "ALL"):
	st = '*'

full_url = base_url + yr + '/pep/natstprc?get=' + vs + '&DATE=' + mnth + '&for=state:' + st

data = urllib.urlopen(full_url)

print full_url 

json_file = open("Data.json", "w")
json_file.write(data.read())
json_file.close()