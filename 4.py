ph_no = input("Enter ph_no: ")
if len(ph_no) > 13 or ph_no[:3] != "+91" or ph_no[3]>5 or not ph_no[3:].isdigit():
    print("Invalid phone number")
else:
    print("Valid phone number")