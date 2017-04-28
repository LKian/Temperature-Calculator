print "Welcome to Temperature Converter. \n"
temp = raw_input("Enter the temperature you'd like to convert.  Please end with C or F: \n")
degrees = temp[0:-1]
degrees = float(degrees)


if temp.endswith('f'):
	print "Leah"
	f_to_c = ((degrees-32)/(1.8))
	f_to_c = round(f_to_c, 2)
	print degrees, "F","is",f_to_c,"Celsius"

elif temp.endswith('c'):
	print "CCCCCCC"
	c_to_f = degrees * 1.8 + 32
	c_to_f = round(c_to_f, 2)
	print degrees,"C","is",c_to_f,"Fahrenheit"