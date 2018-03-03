a= True
b= True
c= False
print("a is {0}".format(a))
print("b is {0}".format(b))
print("b is {0}".format(c))
print("~a is {0}".format(not a))
print("~b is {0}".format(not b))
print("~b is {0}".format(not c))
print("a & b is {0}".format(a and b and c)) 
print("a or b is {0}".format(a or b or c)) 


#################################################
## A     ### B     ### c      ### A and B and c ### A or B or c  #######
## True  ### True  ### True   ### True          ### True         #######
## True  ### True  ### False  ### False         ### True         #######
## True  ### False ### True   ### False         ### True         #######
## True  ### False ### False  ### False         ### True         #######
## False ### True  ### True   ### False         ### True         #######
## False ### True  ### False  ### False         ### True         #######
## False ### False ### True   ### False         ### True         #######
## False ### False ### False  ### False         ### False        #######
#################################################
