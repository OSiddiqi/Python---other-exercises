class Menu():

    def menu():
        ans = True
        while ans:
            print("""
            1. Add a member
            2. Remove a member
            3. Update member details
            4. Check item out
            5. Check item in
            """)
            ans = input("What would you like to do?")
            if ans == "1":
                print("Member added")
            elif ans == "2":
                print ("Member deleted")
            elif ans == "3":
                print ("Member updated")
            elif ans == "4":
                print ("You're taking this item out")
            elif ans == "5":
                print ("Thanks for bringing it back")
            else:
                print ("Goodbye and hope you remain ignorant of some strange thing called 'the internet!'")
    menu()