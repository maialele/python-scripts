import json, requests, sys
APPID = '60e829f5b5a5a64ab87e4c724ec2d316'

# print("today is day 0\n")
# for i in range(4):
#     main = w[i]['main']
#     print("the temperature for Day",i,':\n'
#     "Temperature is: ",main['temp'],'\n'
#     "The Maximum temp is: ", main['temp_max'],'\n'
#     "Overall: ", w[i]['weather'][0]['description'],'\n\n\n'
#     )


class GetData:
    def __init__(self, url):
        self.url = url
    
    def get_request(self):
        response = requests.get(url)
        response.raise_for_status()
        weatherData = json.loads(response.text)
        self.weatherData = weatherData
        return weatherData['list']

    def embed_response(self, response=None):
        response = self.weatherData
        try:
            if self.response == None:
                print('no json respose given')
            else:
                print("today is day 0\n")
                for i in range(4):
                    main = w[i]['main']
                    print("the temperature for Day",i,':\n'
                    "Temperature is: ",main['temp'],'\n'
                    "The Maximum temp is: ", main['temp_max'],'\n'
                    "Overall: ", w[i]['weather'][0]['description'],'\n\n\n'
                    )
        except:
            print('call the get request method first')


if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s' % (location, APPID)

my_request = GetData(url)
my_request.get_request()
my_request.embed_response()
