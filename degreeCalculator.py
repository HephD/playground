convertValue = input("Would you like to convert this value to Celsius or Fahrenheit? C/F > ")

fahrenheit = ["F", "f", "fahrenheit", "Fahrenheit"]

celsius = ["C", "c", "celsius", "Celsius"]


if convertValue in fahrenheit:
  cV = input("Enter the value you'd like to convert. > ")
  fV = (((int(cV)*9)/5)+32)#formula to convert celsius to fahrenheit
  print(fV)
elif convertValue in celsius:
  fV = input("Enter the value you'd like to convert. > ")
  cV = (((int(fV)-32)*5)/9)#formula to convert fahrenheit to celsius
  print(cV)
else: print("Cannot convert this value. Try again.") #need to find a way to make the program restart when ended or failed.
