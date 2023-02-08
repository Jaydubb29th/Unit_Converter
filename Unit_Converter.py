#I want to convert...
num = float(input())
#of this unit...
orig_unit = str(input())
#to this unit (second unit must be spelled out completely - no abbreviations - no plural)...
new_unit = str(input())


inch = {          #original unit is name of dictionary
    "feet": (1/12)*num,   #new unit in red
    "yards": (1/36)*num,
    "miles": (1/63360)*num,
    "nanometers": (1/0.000000254)*num,
    "micrometers": 25400*num,
    "millimeters": 25.4*num,
    "centimeters": 2.54*num,
    "decimeters": 0.254*num,
    "meters": 0.0254*num,
    "dekameters": 0.00254*num,
    "hectometers": 0.000254*num,
    "kilometers": 0.0000254*num
}
foot = {
    "inches": 12*num,
    "yards": (1/3)*num,
    "miles": (1/5280)*num,
    "nanometers": 304800000*num,
    "micrometers": 304800*num,
    "millimeters": 304.8*num,
    "centimeters": 30.48*num,
    "decimeters": 3.048*num,
    "meters": 0.3048*num,
    "dekameters": 0.03048*num,
    "hectometers": 0.003048*num,
    "kilometers": 0.0003048*num
}
yard = {
    "inches": 12*num,
    "feet": 3*num,
    "miles": (1/1760)*num,
    "nanometers": 914400000*num,
    "micrometers": 914400*num,
    "millimeters": 914.4*num,
    "centimeters": 91.44*num,
    "decimeters": 9.144*num,
    "meters": 0.9144*num,
    "dekameters": 0.09144*num,
    "hectometers": 0.009144*num,
    "kilometers": 0.0009144*num
}
mile = {
    "inches": 63360*num,
    "feet": 5280*num,
    "yards": 1760*num,
    "nanometers": 1609344000000*num,
    "micrometers": 1609344000*num,
    "millimeters": 1609344*num,
    "centimeters": 160934.4*num,
    "decimeters": 16093.44*num,
    "meters": 1609.344*num,
    "dekameters": 160.9344*num,
    "hectometers": 16.09344*num,
    "kilometers": 1.609344*num
}
nanometer = {
    "inches": (1/25400000)*num,
    "feet": (1/304800000)*num,
    "yards": (1/914400000)*num,
    "miles": (1/1609344000000)*num,
    "micrometers": (1/1000)*num,
    "millimeters": (1/1000000)*num,
    "centimeters": (1/10000000)*num,
    "decimeters": (1/100000000)*num,
    "meters": (1/1000000000)*num,
    "dekameters": (1/10000000000)*num,
    "hectometers": (1/100000000000)*num,
    "kilometers": (1/1000000000000)*num
}
micrometer = {
    "inches": (1/25400)*num,
    "feet": (1/304800)*num,
    "yards": (1/914400)*num,
    "miles": (1/1609000000)*num,
    "nanometers": 1000*num,
    "millimeters": (1/1000)*num,
    "centimeters": (1/10000)*num,
    "decimeters": (1/100000)*num,
    "meters": (1/1000000)*num,
    "dekameters": (1/10000000)*num,
    "hectometers": (1/100000000)*num,
    "kilometers": (1/1000000000)*num
}
millimeter = {
    "inches": (1/25.4)*num,
    "feet": (1/304.8)*num,
    "yards": (1/914.4)*num,
    "miles": (1/1609000)*num,
    "nanometers": 1000000*num,
    "micrometers": 1000*num,
    "centimeters": (1/10)*num,
    "decimeters": (1/100)*num,
    "meters": (1/1000)*num,
    "dekameters": (1/10000)*num,
    "hectometers": (1/100000)*num,
    "kilometers": (1/1000000)*num
}
centimeter = {
    "inches": (1/2.54)*num,
    "feet": (1/30.48)*num,
    "yards": (1/91.44)*num,
    "miles": (1/160900)*num,
    "nanometers": 10000000*num,
    "micrometers": 10000*num,
    "millimeters": 10*num,
    "decimeters": (1/10)*num,
    "meters": (1/100)*num,
    "dekameters": (1/1000)*num,
    "hectometers": (1/10000)*num,
    "kilometers": (1/100000)*num
}
decimeter = {
    "inches": 3.937*num,
    "feet": 3.048*num,
    "yards": 9.144*num,
    "miles": (1/16090)*num,
    "nanometers": 100000000*num,
    "micrometers": 100000*num,
    "millimeters": 100*num,
    "centimeters": 10*num,
    "meters": (1/10)*num,
    "dekameters": (1/100)*num,
    "hectometers": (1/1000)*num,
    "kilometers": (1/10000)*num
}
meter = {
    "inches": 39.37*num,
    "feet": 3.281*num,
    "yards": 1.094*num,
    "miles": (1/1609)*num,
    "nanometers": 1000000000*num,
    "micrometers": 1000000*num,
    "millimeters": 1000*num,
    "centimeters": 100*num,
    "decimeters": 10*num,
    "dekameters": (1/10)*num,
    "hectometers": (1/100)*num,
    "kilometers": (1/1000)*num
}
dekameter = {
    "inches": 393.7*num,
    "feet": 32.808*num,
    "yards": 10.936*num,
    "miles": (1/160.9)*num,
    "nanometers": 10000000000*num,
    "micrometers": 10000000*num,
    "millimeters": 10000*num,
    "centimeters": 1000*num,
    "decimeters": 100*num,
    "meters": 10*num,
    "hectometers": (1/10)*num,
    "kilometers": (1/100)*num
}
hectometer = {
    "inches": 3937*num,
    "feet": 328.084*num,
    "yards": 109.361*num,
    "miles": (1/16.093)*num,
    "nanometers": 100000000000*num,
    "micrometers": 100000000*num,
    "millimeters": 100000*num,
    "centimeters": 10000*num,
    "decimeters": 1000*num,
    "meters": 100*num,
    "dekameters": 10*num,
    "kilometers": (1/10)*num
}
kilometer = {
    "inches": 39370*num,
    "feet": 3281*num,
    "yards": 1094*num,
    "miles": (1/1.609)*num,
    "nanometers": 1000000000000*num,
    "micrometers": 1000000000*num,
    "millimeters": 1000000*num,
    "centimeters": 100000*num,
    "decimeters": 10000*num,
    "meters": 1000*num,
    "dekameters": 100*num,
    "hectometers": 10*num,
    }

ounce = {      #original unit
    "pounds": num/16,
    "US tons": num/32000,
    "UK tons": num/35840,
    "stones": num/224,
    "micrograms": 28350000*num,
    "milligrams": 28350*num,
    "grams": 28.35*num,
    "kilograms": num/35.274,
    "metric tons": num/35270
}
pound = {
    "ounces": 16*num,
    "stones": num/14,
    "US tons": num/2000,
    "UK tons": num/2240,
    "micrograms": 453600000*num,
    "milligrams": 453600*num,
    "grams": 453.6*num,
    "kilograms": num/2.205,
    "metric tons": num/2205
}
stone = {
    "ounces": 35274*num,
    "pounds": 2205*num,
    "US tons": num/142.9,
    "UK tons": num/160,
    "micrograms": 6350000000*num,
    "milligrams": 6350000*num,
    "grams": 6350.29*num,
    "kilograms": 6.35029*num,
    "metric tons": num/157.5
}
US_ton = {
    "ounces": 32000*num,
    "pounds": 2000*num,
    "stones": 142.9*num,
    "UK tons": num/1.12,
    "micrograms": 907200000000*num,
    "milligrams": 907200000*num,
    "grams": 907200*num,
    "kilograms": 907.2*num,
    "metric tons": num/1.102
}
UK_ton = {
    "ounces": 35840*num,
    "pounds": 2240*num,
    "stones": 160*num,
    "US tons": 1.12*num,
    "micrograms": 1016000000000*num,
    "milligrams": 1016000000*num,
    "grams": 1016000*num,
    "kilograms": 1016*num,
    "metric tons": 1.016*num
}
microgram = {
    "ounces": num/28350000,
    "pounds": num/453600000,
    "stones": num/6350000000,
    "US tons": num/907200000000,
    "UK tons": num/1016000000000,
    "milligrams": num/1000,
    "grams": num/1000000,
    "kilograms": num/1000000000,
    "metric tons": num/1000000000000
}
milligram = {
    "ounces": num/28350,
    "pounds": num/453600,
    "stones": num/6350000,
    "US tons": num/907200000,
    "UK tons": num/1016000000,
    "micrograms": 1000*num,
    "grams": num/1000,
    "kilograms": num/1000000,
    "metric tons": num/1000000000
}
gram = {
    "ounces": num/28.35,
    "pounds": num/453.6,
    "stones": num/6350,
    "US tons": num/907200,
    "UK tons": num/1016000,
    "micrograms": 1000000*num,
    "milligrams": 1000*num,
    "kilograms": num/1000,
    "metric tons": num/1000000
}
kilogram = {
    "ounces": 35.274*num,
    "pounds": 2.205*num,
    "stones": num/6.35,
    "US tons": num/907.2,
    "UK tons": num/1016,
    "micrograms": 1000000000*num,
    "milligrams": 1000000*num,
    "grams": 1000*num,
    "metric tons": num/1000
}
metric_ton = {
    "ounces": 35270*num,
    "pounds": 2205*num,
    "stones": 157.5*num,
    "US tons": 1.102*num,
    "UK tons": num/1.016,
    "micrograms": num*1000000000000,
    "milligrams": 1000000000*num,
    "grams": 1000000*num,
    "kilograms": 1000*num
}

teaspoon = {
    "tablespoons": num/3,
    "fluid ounces": num/6,
    "cups": num/ 48.692,
    "pints": num/96,
    "quarts": num/192,
    "gallons": num/768,
    "milliliters": num*4.929,
    "liters": num/202.9
}
tablespoon = {
    "teaspoons": num*3,
    "fluid ounces": num/2,
    "cups": num/16.231,
    "pints": num/32,
    "quarts": num/64,
    "gallons": num/256,
    "milliliters": num*14.787,
    "liters": num/67.628
}
fluid_ounce = {
    "teaspoons": num*6,
    "tablespoons": num*2,
    "cups": num/8.115,
    "pints": num/16,
    "quarts": num/32,
    "gallons": num/128,
    "milliliters": num*29.574,
    "liters": num/33.814
}
cup = {
    "teaspoons": num*48.692,
    "tablespoons": num*16.231,
    "fluid ounces": num*8.115,
    "pints": num/1.972,
    "quarts": num/3.943,
    "gallons": num/15.772,
    "milliliters": num*240,
    "liters": num/4.167
}
pint = {
    "teaspoons": num*96,
    "tablespoons": num*32,
    "fluid ounces": num*16,
    "cups": num*1.972,
    "quarts": num/2,
    "gallons": num/8,
    "milliliters": num*473.2,
    "liters": num/2.113
}
quart = {
    "teaspoons": num*192,
    "tablespoons": num*64,
    "fluid ounces": num*32,
    "cups": num*3.943,
    "pints": num*2,
    "gallons": num/4,
    "milliliters": num*946.4,
    "liters": num/1.057
}
gallon = {
    "teaspoons": num*768,
    "tablespoons": num*256,
    "fluid ounces": num*128,
    "cups": num*15.773,
    "pints": num*8,
    "quarts": num*4,
    "milliliters": num*3785,
    "liters": num*3.785
}
milliliter = {
    "teaspoons": num/4.929,
    "tablespoons": num/14.787,
    "fluid ounces": num/29.574,
    "cups": num/240,
    "pints": num/473.2,
    "quarts": num/946.4,
    "gallons": num/3785,
    "liters": num/1000
}
liter = {
    "teaspoons": num*202.9,
    "tablespoons": num*67.628,
    "fluid ounces": num*33.814,
    "cups": num*4.167,
    "pints": num*2.113,
    "quarts": num*1.057,
    "gallons": num/3.785,
    "milliliters": num*1000
}

second = {
    "minutes": num/60,
    "hours": num/3600,
    "days": num/86400
}
minute = {
    "seconds": num*60,
    "hours": num/60,
    "days": num/1440
}
hour = {
    "seconds": num*3600,
    "minutes": num*60,
    "days": num/24
}
day = {
    "seconds": num*86400,
    "minutes": num*1440,
    "hours": num*24
}

#length conversion function
def length_convert():
    if orig_unit == "inch" or orig_unit == "inches" or orig_unit == "in":
        print(str(num) + " in. is " + str(inch.get(new_unit)) + " " + new_unit)
    elif orig_unit == "foot" or orig_unit == "feet" or orig_unit == "ft":
        print(str(num) + " ft. is " + str(foot.get(new_unit)) + " " + new_unit)
    elif orig_unit == "yard" or orig_unit == "yards" or orig_unit == "yd":
        print(str(num) + " yd. is " + str(yard.get(new_unit)) + " " + new_unit)
    elif orig_unit == "mile" or orig_unit == "miles" or orig_unit == "mi":
        print(str(num) + " mi. is " + str(mile.get(new_unit)) + " " + new_unit)
    elif orig_unit == "nanometer" or orig_unit == "nanometers" or orig_unit == "nm":
        print(str(num) + " nm. is " + str(nanometer.get(new_unit)) + " " + new_unit)
    elif orig_unit == "micrometer" or orig_unit == "micrometers" or orig_unit == "μm":
        print(str(num) + " μm. is " + str(micrometer.get(new_unit)) + " " + new_unit)
    elif orig_unit == "millimeter" or orig_unit == "millimeters" or orig_unit == "mm":
        print(str(num) + " mm. is " + str(millimeter.get(new_unit)) + " " + new_unit)
    elif orig_unit == "centimeter" or orig_unit == "centimeters" or orig_unit == "cm":
        print(str(num) + " cm. is " + str(centimeter.get(new_unit)) + " " + new_unit)
    elif orig_unit == "decimeter" or orig_unit == "decimeters" or orig_unit == "dm":
        print(str(num) + " dm. is " + str(decimeter.get(new_unit)) + " " + new_unit)
    elif orig_unit == "meter" or orig_unit == "meters" or orig_unit == "m":
        print(str(num) + " m. is " + str(meter.get(new_unit)) + " " + new_unit)
    elif orig_unit == "dekameter" or orig_unit == "decameter" or orig_unit == "dekameters" or orig_unit == "decameters" or orig_unit == "dam":
        print(str(num) + " dam. is " + str(dekameter.get(new_unit)) + " " + new_unit)
    elif orig_unit == "hectometer" or orig_unit == "hectometers" or orig_unit == "hm":
        print(str(num) + " hm. is " + str(hectometer.get(new_unit)) + " " + new_unit)
    elif orig_unit == "kilometer" or orig_unit == "kilometers" or orig_unit == "km":
        print(str(num) + " km. is " + str(kilometer.get(new_unit)) + " " + new_unit)
    else:
        print("Error! Incorrect unit input. \nCheck your spelling or something ya foo!")
#mass conversion function
def mass_convert():
    if orig_unit == "ounce" or orig_unit == "ounces" or orig_unit == "oz":
        print(str(num) + " oz. is " + str(ounce.get(new_unit)) + " " + new_unit)
    elif orig_unit == "pound" or orig_unit == "pounds" or orig_unit == "lb":
        print(str(num) + " lb. is " + str(pound.get(new_unit)) + " " + new_unit)
    elif orig_unit == "stone" or orig_unit == "stones" or orig_unit == "st":
        print(str(num) + " st. is " + str(stone.get(new_unit)) + " " + new_unit)
    elif orig_unit == "US ton" or orig_unit == "US tons" or orig_unit == "tn":
        print(str(num) + " tn. is " + str(US_ton.get(new_unit)) + " " + new_unit)
    elif orig_unit == "UK ton" or orig_unit == "UK tons" or orig_unit == "t":
        print(str(num) + " t. is " + str(UK_ton.get(new_unit)) + " " + new_unit)
    elif orig_unit == "microgram" or orig_unit == "micrograms" or orig_unit == "μg" or orig_unit == "mcg":
        print(str(num) + " mcg. is " + str(microgram.get(new_unit)) + " " + new_unit)
    elif orig_unit == "milligram" or orig_unit == "milligrams" or orig_unit == "mg":
        print(str(num) + " mg. is " + str(milligram.get(new_unit)) + " " + new_unit)
    elif orig_unit == "gram" or orig_unit == "grams" or orig_unit == "g":
        print(str(num) + " g. is " + str(gram.get(new_unit)) + " " + new_unit)
    elif orig_unit == "kilogram" or orig_unit == "kilograms" or orig_unit == "kg":
        print(str(num) + " kg. is " + str(kilogram.get(new_unit)) + " " + new_unit)
    elif orig_unit == "metric ton" or orig_unit == "metric tons" or orig_unit == "tonnes" or orig_unit == "tonne":
        print(str(num) + " m. tonne(s) " + str(metric_ton.get(new_unit)) + " " + new_unit)
    else:
        print("Error! Incorrect unit input. \nCheck your spelling or something ya foo!")
#def volume_convert():
def volume_convert():
    if orig_unit == "teaspoon" or orig_unit == "teaspoons" or orig_unit == "tsp":
        print(str(num) + " tsp. is " + str(teaspoon.get(new_unit)) + " " + new_unit)
    elif orig_unit == "tablespoon" or orig_unit == "tablespoons" or orig_unit == "tbsp":
        print(str(num) + " tbsp. is " + str(tablespoon.get(new_unit)) + " " + new_unit)
    elif orig_unit == "fluid ounce" or orig_unit == "fluid ounces" or orig_unit == "fl oz":
        print(str(num) + " fl. oz. is " + str(fluid_ounce.get(new_unit)) + " " + new_unit)
    elif orig_unit == "cup" or orig_unit == "cups" or orig_unit == "c":
        print(str(num) + " c. is " + str(cup.get(new_unit)) + " " + new_unit)
    elif orig_unit == "pint" or orig_unit == "pints" or orig_unit == "pt":
        print(str(num) + " pt. is " + str(pint.get(new_unit)) + " " + new_unit)
    elif orig_unit == "quart" or orig_unit == "quarts" or orig_unit == "qt":
        print(str(num) + " qt. is " + str(quart.get(new_unit)) + " " + new_unit)
    elif orig_unit == "gallon" or orig_unit == "gallons" or orig_unit == "gal":
        print(str(num) + " gal. is " + str(gallon.get(new_unit)) + " " + new_unit)
    elif orig_unit == "milliliter" or orig_unit == "milliliters" or orig_unit == "ml" or orig_unit == "mL" or orig_unit == "cc" or orig_unit == "cubic centimeter" or orig_unit == "cubic centimeters":
        print(str(num) + " mL. is " + str(milliliter.get(new_unit)) + " " + new_unit)
    elif orig_unit == "liter" or orig_unit == "liters" or orig_unit == "L":
        print(str(num) + " L. is " + str(liter.get(new_unit)) + " " + new_unit)
    else:
        print("Error! Incorrect unit input. \nCheck your spelling or something ya foo!")
#def time_convert():
def time_convert():
    if orig_unit == "second" or orig_unit == "seconds" or orig_unit == "sec":
        print(str(num) + " sec. is " + str(second.get(new_unit)) + " " + new_unit)
    elif orig_unit == "minute" or orig_unit == "minutes" or orig_unit == "min":
        print(str(num) + " min. is " + str(minute.get(new_unit)) + " " + new_unit)
    elif orig_unit == "hour" or orig_unit == "hours" or orig_unit == "hr":
        print(str(num) + " hr. is " + str(hour.get(new_unit)) + " " + new_unit)
    elif orig_unit == "day" or orig_unit == "days":
        print(str(num) + " day(s) is " + str(day.get(new_unit)) + " " + new_unit)
    else:
        print("Error! Incorrect unit input. \nCheck your spelling or something ya foo!")

length_list = ["inch", "inches", "in", "foot", "feet", "ft", "yard", "yards", "yd", "miles", "mile", "mi", "nanometer", "nanometers", "nm", "micrometer", "micrometers", "μm", "millimeter", "millimeters", "mm", "centimeter", "centimeters", "cm", "decimeter", "decimeters", "dm", "meter", "meters", "m", "dekameter", "dekameters", "dam", "decameter", "decameters", "hectometers", "hectometer", "hm", "kilometer", "kilometers", "km"]
mass_list = ["ounce", "ounces", "oz", "pound", "pounds", "lb", "stone", "stones", "st", "US ton", "US tons", "tn", "UK ton", "UK tons", "t", "microgram", "micrograms", "mcg", "μg", "milligram", "milligrams", "mg", "gram", "grams", "g", "kilogram", "kilograms", "kg", "metric ton", "metric tons", "tonnes", "tonne"]
volume_list = ["teaspoon", "teaspoons", "tsp", "tablespoon", "tablespoons", "tbsp", "fluid ounce", "fluid ounces", "fl oz", "cup", "cups", "c", "pint", "pints", "pt", "quart", "quarts", "qt", "gallons", "gallon", "gal", "milliliter", "milliliters", "ml", "mL", "cubic centimeter", "cubic centimeters", "cc", "liter", "liters", "L"]
time_list = ["second", "seconds", "sec", "minute", "minutes", "min", "hour", "hours", "hr", "day", "days"]

if orig_unit in length_list:
    length_convert()
if orig_unit in mass_list:
    mass_convert()
if orig_unit in volume_list:
    volume_convert()
if orig_unit in time_list:
    time_convert()