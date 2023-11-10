def isValid(s):
    z=[]
    for i in s:
        if(i=="(" or i=="[" or i=="{"):
            z.append(i)
        elif(len(z)==0):
            return False
        elif(i==")" and z[-1]=="(" or i=="]" and z[-1]=="[" or i=="}" and z[-1]=="{"):
            z.pop()
        
        
    if(len(z)==0):
        return True
    else:
        return False

s = "()[{}()]"
if isValid(s):
    print("True")
else:
    print("False")