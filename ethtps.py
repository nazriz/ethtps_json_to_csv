import requests
import json
import pandas as pd
import csv

query = {"providers":"0"}
response = requests.get("https://api.ethtps.info/API/v2/AllData",params=query)

tps_data = response.json()

def dumpData(protocol_name):
	protocol_key = f"{protocol_name}"

	protocol_data = tps_data['allTPSData']['All'][protocol_name]

	protocol_data_dict = {}

	for data in protocol_data:
		date = data['data'][0]['date']
		value = data['data'][0]['value']
		protocol_data_dict[date] = value

	df = pd.DataFrame(list(protocol_data_dict.items()),columns = ['date','value']) 

	df.to_csv(f'{protocol_name}_tps_data.csv')


# Change paramter to name of protocol as necessary
dumpData("Ethereum")

