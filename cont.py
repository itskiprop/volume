age = int(input("enter age"))
nationality = str(input("enter nationality(Kenya,Tanzania,Uganda)"))
has_valid_ID = str(input("do you have a valid ID (yes/no): ")).lower()
#check age 
if age>= 18:
    print ("eligible")
#check nationality
if nationality == ("Kenya","Tanzania", "Uganda: "):
   print('eligible: ')

#checkvalid Id
if has_valid_ID =="yes":
   print("eligible")
else:
   print("not eligible: ")

