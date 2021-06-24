import requests
r=requests.get('http://api.openweathermap.org/data/2.5/weather?q=Karimnagar&appid=d8f2e92dbff408602210c1b1c8f823c2')
with open("weather1.text",'wb') as f:
 f.write(r.content)