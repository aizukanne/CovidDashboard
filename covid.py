def getNewData():
	import requests
	import json
	import pandas as pd
	url = "https://covid-193.p.rapidapi.com/statistics"
	headers = {
		'x-rapidapi-host': "covid-193.p.rapidapi.com",
    	'x-rapidapi-key': "4c37223acemsh65b1a8b456b72c1p15a99ajsnd4a09ab346a4"
    }
	response = requests.request("GET", url, headers=headers)
	data = json.loads(response.text)
	df = pd.json_normalize(data['response'])
	# newCases = data['response'][0]['cases']['new']
	# totalCases = data['response'][0]['cases']['total']
	# timeStamp = data['response'][0]['time']
	return df

# def getLastData(totalCases, country):
# 	import requests
# 	import json
# 	from datetime import date, timedelta
# 	yesterday = date.today() - timedelta(1)
# 	url = "https://covid-193.p.rapidapi.com/history"
# 	querystring = {"day":yesterday,"country":country}
# 	headers = {
# 	   	'x-rapidapi-host': "covid-193.p.rapidapi.com",
# 		'x-rapidapi-key': "4c37223acemsh65b1a8b456b72c1p15a99ajsnd4a09ab346a4"
# 	}
# 	response = requests.request("GET", url, headers=headers, params=querystring)
# 	data = json.loads(response.text)
# 	if len(data['response']) > 0:
# 		oldTotal = data['response'][0]['cases']['total']
# 	else:
# 		return (0, yesterday)

# 	if (oldTotal == totalCases and len(data['response']) > 1):
# 		oldTotal = data['response'][1]['cases']['total']
# 		if oldTotal == totalCases:
# 			yesterday = date.today() - timedelta(2)
# 			url = "https://covid-193.p.rapidapi.com/history"
# 			print(yesterday)
# 			querystring = {"day":yesterday,"country":"austria"}
# 			headers = {
# 			   	'x-rapidapi-host': "covid-193.p.rapidapi.com",
# 				'x-rapidapi-key': "4c37223acemsh65b1a8b456b72c1p15a99ajsnd4a09ab346a4"
# 			}
# 			response = requests.request("GET", url, headers=headers, params=querystring)
# 			data = json.loads(response.text)
# 			oldTotalCases = data['response'][0]['cases']['total']
# 			oldTimeStamp = data['response'][0]['time']
# 			return (oldTotalCases, oldTimeStamp)
# 		else:
# 			oldTotalCases = data['response'][1]['cases']['total']
# 			oldTimeStamp = data['response'][1]['time']
# 			return (oldTotalCases, oldTimeStamp)			
# 	elif oldTotal != totalCases:
# 		oldTotalCases = data['response'][0]['cases']['total']
# 		oldTimeStamp = data['response'][0]['time']
# 		return (oldTotalCases, oldTimeStamp)
# 	else:
# 		return (oldTotal, yesterday)

def getCountries():
	import requests
	import json
	url = "https://covid-193.p.rapidapi.com/countries"
	headers = {
    	'x-rapidapi-host': "covid-193.p.rapidapi.com",
    	'x-rapidapi-key': "4c37223acemsh65b1a8b456b72c1p15a99ajsnd4a09ab346a4"
    }
	response = requests.request("GET", url, headers=headers)
	data = json.loads(response.text)
	countries = data['response']
	return countries