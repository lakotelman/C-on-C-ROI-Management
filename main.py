class User:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.portfolio = {}

t1 = User("mr.monopoly")
t2 = User("mr.green")

class AppControl: 
    def __init__(self):
        self.all_users = {t1.profile_name: t1,
                        t2.profile_name: t2 }
        self.active_user = self.all_users["mr.monopoly"]
    
    def control_create_user(self, user): 
        self.all_users[user.profile_name] = user
    
    def control_toggle_user(self, user_obj):
        self.active_user = user_obj
        
    def control_edit_user(self): 
        pass 

    def control_add_property(self, property):
        self.all_users[self.active_user.profile_name].portfolio[property.address] = property
        return self.all_users[self.active_user.profile_name]

    def control_edit_property(self): 
        pass 



class AppView:
    def __init__(self, controller):
        self.controller = controller 
        
    def view_create_user(self):
        profile_name = input("What would you like your account name to be? ")
        u = User(profile_name)
        self.controller.add_user_to_all(u)
        print(f"Added {profile_name} to the co-op account")
        self.run()

    def view_toggle_user(self):
        choice_dict = {}
        for i, profile_name in enumerate(self.controller.all_users.items()):
            print(f"[{i+1}] {profile_name[0]}")
            choice_dict[str(i+1)] = profile_name[1]
        toggle = input("\nWhich profile would you like to view? ")
        try:
            self.controller.control_toggle_user(choice_dict[toggle])
            print(f"\nActive User is {self.controller.active_user.profile_name.title()}")
            self.run()
        except Exception as err: 
            print("\nInvalid input. Please try again")
            self.view_toggle_user()

    def view_edit_user(self):
        pass

    def display_portfolio(self):
        pass

    def view_new_property(self):
        address = input("\nWhat is the address for this property? ")
        investment = input("\nFor this property, what is the total for your initial investment? ")
        gross = input("\n For this property, what is the total for your monthly gross income? ")
        expenses = input("\n For this property, what is your total monthly expenses? ")
        p = Property(address, int(gross), int(expenses), int(investment))
        self.controller.add_property_to_portfolio(p)
        print(self.controller.active_user.profile_name)
        print(self.controller.active_user.portfolio)
        self.run()

    def view_edit_property(self):
        pass

    def run(self):
        print(f"Welcome, {self.controller.active_user.profile_name.title()}")
        print("What would you like to do?")
        print("""
[1] Change Profile
[2] Add Profile
[3] Edit Profile
[4] View your portfolio and properties 
[5] Create a new property
[6] Edit your portfolio
[7] Quit
        """)
        while True:
            menu_select = input("") 
            if menu_select == "1": 
                self.view_toggle_user()
            if menu_select == "2": 
                self.view_create_user()
            if menu_select == "3": 
                pass
            if menu_select =="4": 
                pass 
            if menu_select == "5": 
                print("Just a few questions...")
                self.view_new_property()
            if menu_select == "6": 
                self.view_edit_property()
            if menu_select == "7": 
                break


class Property: 
    def __init__(self, address, gross, expenses, investment): 
        self.address = address 
        self.gross = gross
        self.expenses = expenses 
        self.investment = investment
        self.net = self.gross - self.expenses
        self.roi =int(((self.net *12)/self.investment) * 100)


if __name__ == "__main__":
    t1c = AppControl()
    t1 = AppView(t1c)
    t1.run()
