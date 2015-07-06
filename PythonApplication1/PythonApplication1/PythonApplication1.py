print('Tempurature conversion')
print("if converting Celcius to Farenheit, Enter cf")
print("if converting from Farenheit to Celcius, Enter fc")
SelectedConversion = input("enter your selection ")
temp = int(input("enter tempurature to be converted "))
ConvTemp = 0


if SelectedConversion == "fc":
    ConvTemp = ((temp - 32) * 5) / 9
    print(str(temp) + " farenheight is " + str(ConvTemp) + " Celcius" ) 
elif SelectedConversion == "cf":
     ConvTemp = ((temp * 9) /5) + 32
     print(str(temp) + "Celsius is " + str(ConvTemp) + " Farenheight")
else:
    print('you can only convert numeric digits')

