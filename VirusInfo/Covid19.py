import requests
def covid_19_ja(date=None):
  if date == None:
    raise TypeError('Argument "date" is missing.')
  req =  requests.get(f"https://opendata.corona.go.jp/api/Covid19JapanNdeaths?date={date}")
  text = req.text.replace('-', '')
  s = text.replace('{', '').replace('"', '').replace('errorInfo:errorFlag:0,errorCode:null,errorMessage:null},itemList:[date', '').replace(f'{date}', '').replace(':,ndeaths:', '').replace('}]}', '')
  if s == "errorInfo:errorFlag:0,errorCode:null,errorMessage:null},itemList:[]}":
    raise TypeError('Data for this date could not be found.')
  return s
