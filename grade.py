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
"""mymath() Function defined as-
The University Grants Commission of Bangladesh recommended Grading system. 
https://ugc.portal.gov.bd/sites/default/files/files/ugc.portal.gov.bd/page/ad5e35a2_65ec_4a35_948a_b4a7a54de7ba/Uniform%20Recommended%20Grading%20System%20%281%29.pdf
"""

def mymath(xkey, xvalue):
    s_num = xvalue
    if(s_num>=80):
        print(xkey , ": A+")
    elif(s_num<=79 and s_num>=75):
        print(xkey , ": A")
    elif(s_num<=74 and s_num>=70):
        print(xkey , ": A-")
    elif(s_num<=69 and s_num>=65):
        print(xkey , ": B+")
    elif(s_num<=64 and s_num>=60):
        print(xkey , ": B")
    elif(s_num<=59 and s_num>=55):
        print(xkey , ": B-")
    elif(s_num<=54 and s_num>=50):
        print(xkey , ": C+")
    elif(s_num<=49 and s_num>=45):
        print(xkey , ": C")
    elif(s_num<=44 and s_num>=40):
        print(xkey , ": D")
    else:
        print(xkey , ": F")


for a, b in sub_dict.items():
    mymath(xkey=a, xvalue=b)

#print(len(sub_dict))
avg=(Bangla_sub+English_sub+Math_sub+Physics_sub+Biology_sub)/len(sub_dict)
mymath(xkey="\nFinal Grade is", xvalue=avg)
