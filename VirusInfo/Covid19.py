import requests
class Covid_19:
  """
  Information on the number of people infected with Covid-19 and other information can be obtained.
  Added: v0.4
  """
  def japan_Deaths(date=None):
    """
    Number of infected persons on selected dates in Japan.
    Added: v0.4
    """    
    if date == None:
      raise TypeError('Argument "date" is missing.')
    req2 = requests.get(f"https://opendata.corona.go.jp/api/Covid19JapanNdeaths?date={date}")
    text2 = req2.text.replace('-', '')
    s2 = text2.replace('{', '').replace('"', '').replace('errorInfo:errorFlag:0,errorCode:null,errorMessage:null},itemList:[date', '').replace(f'{date}', '').replace(':,ndeaths:', '').replace('}]}', '')
    if s2 == "errorInfo:errorFlag:0,errorCode:null,errorMessage:null},itemList:[]}":
      raise TypeError('Data for this date could not be found.')
    elif s2 == "errorInfo:errorFlag:1,errorCode:100,errorMessage:日付の形式が不正です。},itemList:[]}":
      raise TypeError('Date format is invalid.')
    return s2

  def japan_all():
    """
    Number of infected persons on selected dates in Japan.
    Added: v0.4
    """    
    req3 = requests.get(f"https://data.corona.go.jp/converted-json/covid19japan-all.json")
    text3 = req3.text.replace(f'","','\n')
    s3 = text3.replace('[{"srcurl_pdf": "", "srcurl_web": "", "description": "", "npatients": 0, "nexits": 0, "ndeaths": 0, "ncurrentpatients": 0, "srcurl_pdf_archived": "", "lastUpdate": "','').replace('", "area": [{"','\n').replace('", "name": "", "ncurrentpatients": 0, "nexits": 0, "ndeaths": 0, "npatients": ','').replace('name_jp": "','').replace('},','\n').replace('{"','').replace('}]}]','')
    return s3


  def castam(city=None, date=None):
    """Cumulative number of infected people in the specified area up to the specified date
    Added: v0.4
    """
    if city == None:
      raise TypeError('Argument "city" is missing.')
    elif date == None:
      raise TypeError('Argument "date" is missing.')
    req1 = requests.get(f"https://opendata.corona.go.jp/api/Covid19JapanAll?date={date}&dataName={city}")
    text1 = req1.text.replace('-', '')
    s1 = text1.replace('{"errorInfo":{"errorFlag":"0","errorCode":null,"errorMessage":null},"itemList":[{"date":"', '').replace('","name_jp":"', '').replace(f"{city}", '').replace(f"{date}", '').replace('","npatients":"', '').replace('"}]}', '')
    return s1