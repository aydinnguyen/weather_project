import weather
import tkinter

mainWindow = tkinter.Tk()

mainWindow.geometry("300x300")

mainWindow.title("weather app by Aydin Anh Nguyen")

mainWindow.config(bg ="#FF0000")

api_key = "1cc72f37ccff0068813610aa29f347d3"

title = tkinter.Label(text="Weather app",
   bg=mainWindow['bg'],
   font=('DejaVu Serif',20,'bold'),
   fg="#0800FF")
title.pack(pady=20)

countryPrompt = tkinter.Label(text = "country: ",bg=mainWindow['bg'])
countryPrompt.pack()

countryBox = tkinter.Entry()
countryBox.pack(pady=5)

cityPrompt = tkinter.Label(text="City: ",bg=mainWindow['bg'] )
cityPrompt.pack()

cityBox = tkinter.Entry()
cityBox.pack(pady=5)

def getWeather():
  city = cityBox.get()
  country = countryBox.get()
  temperature = weather.get_weather(city, country, api_key)
  if temperature:
    result.config(text=f"The temperature in {city}, {country} is {round(temperature)}°C.")
  else:
    result.config(text="Temperature unavailable")

button = tkinter.Button(text="Get Weather",command=getWeather)
button.pack(pady=5)

result = tkinter.Label(text="",bg=mainWindow['bg'],font=("Arial",10,"italic"))
result.pack(pady=10)





mainWindow.mainloop()