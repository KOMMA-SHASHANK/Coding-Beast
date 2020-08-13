l1=set("abcdefghijklmnopqrstuvwxyz")
l2=input("please enter any  string")
l2=l2.replace(" ","")
l2=l2.lower()
print(l2)
l3=set(l1.symmetric_difference(l2))
print(l3)
if (l3==set()):
    print("The String is PANGRAM")
else:
    print("The String is NOT PANGRAM")
        

