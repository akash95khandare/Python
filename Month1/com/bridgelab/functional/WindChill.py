from com.bridgelab.util import Utility

t = int(input("Enter temperature : "))
v = int(input("Enter wind speed : "))
print("Wind Chill is : ", Utility.weather(t, v))