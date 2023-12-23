sub_dict = {
"Bangla": "",
"English": "",
"Math": "",
"Physics": "",
"Biology": ""
}

Bangla_sub=int(input("Enter marks of Bangla: "))
English_sub=int(input("Enter marks of English: "))
Math_sub=int(input("Enter marks of Math: "))
Physics_sub=int(input("Enter marks of Physics: "))
Biology_sub=int(input("Enter marks of Biology: "))

sub_dict["Bangla"] = Bangla_sub
sub_dict["English"] = English_sub
sub_dict["Math"] = Math_sub
sub_dict["Physics"] = Physics_sub
sub_dict["Biology"] = Biology_sub

#print(sub_dict)
"""
The University Grants Commission of Bangladesh recommended Grading system. 
https://ugc.portal.gov.bd/sites/default/files/files/ugc.portal.gov.bd/page/ad5e35a2_65ec_4a35_948a_b4a7a54de7ba/Uniform%20Recommended%20Grading%20System%20%281%29.pdf
"""
for x, y in sub_dict.items():
    #print(sub_dict[x])
    #print(x, y)
    now_sub = sub_dict[x]
    if(now_sub>=80):
        print(x , ": A+")
    elif(now_sub<=79 and now_sub>=75):
        print(x , ": A")
    elif(now_sub<=74 and now_sub>=70):
        print(x , ": A-")
    elif(now_sub<=69 and now_sub>=65):
        print(x , ": B+")
    elif(now_sub<=64 and now_sub>=60):
        print(x , ": B")
    elif(now_sub<=59 and now_sub>=55):
        print(x , ": B-")
    elif(now_sub<=54 and now_sub>=50):
        print(x , ": C+")
    elif(now_sub<=49 and now_sub>=45):
        print(x , ": C")
    elif(now_sub<=44 and now_sub>=40):
        print(x , ": D")
    else:
        print(x , ": F")

avg=(Bangla_sub+English_sub+Math_sub+Physics_sub+Biology_sub)/5
now_sub = avg
x = "\nFinal Grade is"
#print(now_sub, x)
if(now_sub>=80):
    print(x , ": A+")
elif(now_sub<=79 and now_sub>=75):
    print(x , ": A")
elif(now_sub<=74 and now_sub>=70):
    print(x , ": A-")
elif(now_sub<=69 and now_sub>=65):
    print(x , ": B+")
elif(now_sub<=64 and now_sub>=60):
    print(x , ": B")
elif(now_sub<=59 and now_sub>=55):
    print(x , ": B-")
elif(now_sub<=54 and now_sub>=50):
    print(x , ": C+")
elif(now_sub<=49 and now_sub>=45):
    print(x , ": C")
elif(now_sub<=44 and now_sub>=40):
    print(x , ": D")
else:
    print(x , ": F")

