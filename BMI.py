def health():
    name = input("Enter your Full Name: ".strip().lower())
    weight = float(input("Enter your Weight in Kg: ").strip())
    height = float(input("Enter your Height in metres: ").strip())
    bmi = round(weight/(height**2),2)
    
    print(bmi)
    
    if bmi>0:
        if bmi<=18.5:
            print(f"{name}, you are underweight")
        elif bmi<=24.9:
            print(f"{name}, you are healthy weight")
        elif bmi<=29.9:
            print(f"{name}, you are over weight")
        else:
            print(f"{name}, you are obese")
    else:
        print("invalid input")
    while True:
        again = input("Do you want to check again?(y/n): ").strip().lower()
        if again == 'y':
            health()
        elif again == 'n':
            print("okeyy, bye bye!!")
            break           
        else:
            print("invalid input")
health()


    
    
