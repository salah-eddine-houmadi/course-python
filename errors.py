while True:
    try:
        a = int(input("enter number 1:"))
        b = int(input("enter number 2:"))
        print(f"The division is{a / b}")

    except ValueError:
        print("Please dont perform bad typrcasts")

    except ZeroDivisionError:
        print("hey dont divide by 0")
        
    except Exception as e:
        print("Some error occurrd!", e)