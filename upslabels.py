
#Price Calculator for UPS Label Service
#Base Price is $15

print ("Thank you for choosing btnt's label service. Please fill out this form. Leave address line 2 blank if it is not applicable.")

FromName = input("Name you are shipping from: ")
FromAddress1 = input ("From street address (line 1): ")
FromAddress2 = input ("From street address (line 2): ")
FromAddress3 = input ("From city: ")
FromAddress4 = input ("From state/province: ")
FromAddress5 = input ("From ZIP/postal code: ")
FromAddress6 = input ("From country: ")

ToName = input("Name you are shipping to: ")
ToAddress1 = input ("To street address (line 1): ")
ToAddress2 = input ("To street address (line 2): ")
ToAddress3 = input ("To city: ")
ToAddress4 = input ("To state/province: ")
ToAddress5 = input ("To ZIP/postal code: ")
ToAddress6 = input ("To country: ")

while True:
  MetricOrImperial = input ("Are you using centimetres and kilograms or inches and pounds? (CK/IP)")
  if MetricOrImperial.upper() not in ('CK', 'IP'):
    print ("You entered an invalid response. Please check your spelling and try again.")
  else:
    break

if MetricOrImperial == "CK":
  dimensionsCL = input ("What is the length of your package, in centimeters?")
  dimensionsCW = input ("What is the width of your package, in centimeters?")
  dimensionsCH = input ("What is the height of your package, in centimeters?")
  dimensionsL = int(dimensionsCL)/2.54
  dimensionsW = int(dimensionsCW)/2.54
  dimensionsH = int(dimensionsCH)/2.54
  weightCK = input ("What is the weight of your package, in kilograms?")
  weight = int(weightCK)/2.205
elif MetricOrImperial == "IP":
  dimensionsL = input ("What is the length of your package, in inches?")
  dimensionsW = input ("What is the width of your package, in inches?")
  dimensionsH = input ("What is the height of your package, in inches?")
  weight = input ("What is the weight of your package, in pounds?")

x = 15

shippingSpeed = input("What is your desired shipping speed in days? (Enter number between 1 - 5)")
intl = input ("Is your package Domestic (D) or International (I)")

if intl == 'I':
  x = x + 2

if shippingSpeed == "1":
  x = x + 5
elif shippingSpeed == "2":
  x = x + 4
elif shippingSpeed == "3":
  x = x + 3

print ("```\n" + FromName + "\n" + FromAddress1 + "\n" + FromAddress2 + "\n" + FromAddress3 + ", " + FromAddress4 + " " + FromAddress5 + "\n" + FromAddress6 + "\n-----\n" + ToName + "\n" + ToAddress1 + "\n" + ToAddress2 + "\n" + ToAddress3 + ", " + ToAddress4 + " " + ToAddress5 + "\n" + ToAddress6 + "\n-----\n" + dimensionsL + "/" + dimensionsW + "/" + dimensionsH + "/" + weight + "lbs\n" + "-----\n" + "Shipping Speed: " + shippingSpeed + "days" + "\n```\n")
print ("Thank you for filling out the form. Please copy paste the above text from the ``` to the ``` and send it to me when you order. My discord is btnt#4041 and my nulled is qqnz. \nPlease be aware: my timezone is EST. \nAll orders will be handled within the hours of 12:50 to 13:20, or 16:00 to 18:00. MM is accepted; fees will be on you.")

#Contact me, btnt#4041 or qqnz on nulled.
#大陆同志，我QQ号为2172662271