####################################
# following variables are the same #
####################################
# str1=" salam "
 str2='Hello'

######################
## concat two string #
######################
 name='Javad'
 family='heidari'
 greeting= str1+name+family
 print(greeting)

 greeting2=str1+" "+name+" "+family
 print(greeting2)

 print(("\'"+greeting2+" \'") * 3)
######################################
## some useful operations on strings #
######################################
 print(greeting2.capitalize())
 print(greeting2.upper())
 print(greeting2.rsplit(' ')) # splitting the string by blank
 print(greeting2.strip(' ')) # remove the blanks before and after the string

###########################################
### another sample of printing a varibale #
###########################################
adad = 5
print(adad)
str_adad = str(adad)
print("adad number is : ", adad)  # print each part of input separately
print("adad number is : " + str(adad))  # concat two string
