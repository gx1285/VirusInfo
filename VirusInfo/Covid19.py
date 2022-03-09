import requests
class Covid_19:
  def japan(date=None):
    if date == None:
      raise TypeError('Argument "date" is missing.')
    req =  requests.get(f"https://opendata.corona.go.jp/api/Covid19JapanNdeaths?date={date}")
    text = req.text.replace('-', '')
    s = text.replace('{', '').replace('"', '').replace('errorInfo:errorFlag:0,errorCode:null,errorMessage:null},itemList:[date', '').replace(f'{date}', '').replace(':,ndeaths:', '').replace('}]}', '')
    if s == "errorInfo:errorFlag:0,errorCode:null,errorMessage:null},itemList:[]}":
      raise TypeError('Data for this date could not be found.')
    elif s == "errorInfo:errorFlag:1,errorCode:100,errorMessage:日付の形式が不正です。},itemList:[]}":
      raise TypeError('Date format is invalid.')
    return s
