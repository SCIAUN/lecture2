a= True
b= False
print("a is {0}".format(a))
print("b is {0}".format(b))
print("~a is {0}".format(not a))
print("~b is {0}".format(not b))
print("a & b is {0}".format(a and b)) # True if both of them are True
print("a or b is {0}".format(a or b)) # True if one or both of them are True


#################################################
## A     ### B     ### A and B ### A or B #######
## True  ### True  ### True    ### True   #######
## True  ### False ### False   ### True   #######
## False ### True  ### False   ### True   #######
## False ### False ### False   ### False  #######
#################################################
