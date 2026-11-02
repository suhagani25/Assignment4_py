fastag = input("Is FASTag active? (yes/no): ")
holiday = input("Is it a national holiday? (yes/no): ")
vehicle = input("Enter vehicle type: ")

if fastag == "no":
    print("Double toll penalty applied: cash mode")

else:
    if holiday == "yes":
        print("Festive waiver applied: half toll")

    else:
        if vehicle == "car":
            print("Toll amount: ₹100")
        elif vehicle == "SUV":
            print("Toll amount: ₹150")
        elif vehicle == "truck":
            print("Toll amount: ₹300")
        else:
            print("Invalid vehicle category")