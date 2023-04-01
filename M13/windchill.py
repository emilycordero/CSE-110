'''
Emily Cordero
windchill.py 
Write a program that asks the user for a temperature and then shows the wind chill values for various wind speeds at that temperature.
'''
V=float
wind_chill = float

# Function to calculate wind speed
def calculate_v(V):
        V = V + 5
        return V
 
# Function to calculate and return wind chill based on temp and wind speed
# wind Chill (f) = 35.74 + 0.6215T -35.75(V^0.16)+0.4275T(V^0.16)
def compute_wind_chill(T,V):
    wind_chill = 35.74 + 0.6215*(T) - 35.75*(V**0.16)+0.4275*(T)*(V**0.16)
    return wind_chill

def convert_temp(T):
     T= T*(9/5)+32
# Choose a temperature
T = float(input('What is the temperature? '))
degree_of_temp = input('Fahrenheit or Celsius (F/C)?')

for V in calculate_v(V):
    print(f'At temperature {T}F, and wind speed {V} mph, the windchill is: {wind_chill}F')
