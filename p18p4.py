#String check by two given strings


#return whether the string is matched or not
def stringcheck(s1,s2):
    output =0
    if(len(s1)==len(s2)):
        if(s1==s2):
            output=1    
    if(len(s1)>len(s2)):
        output=s1.find(s2)
    if(len(s2)>len(s1)):
        output=s1.find(s2)
    return output


a= input("Enter your first string : ").lower()
b= input("Enter your second string : ").lower()

result = stringcheck(a,b)

if (result>0):
    print("Strings are matching")
else:
    print("Strings are not matching")
