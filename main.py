from attr import attrib


class User:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.portfolio = {}

    def display_portfolio(self):
        for name, prop_obj in self.portfolio.items():
            print(
                f"""\n{name.title()}
    -----------------------------------------
    Initial Investment: {prop_obj.investment}
    Monthly Gross Income: {prop_obj.gross}
    Monthly Expenses: {prop_obj.expenses}
    Montly Net Income: {prop_obj.net}
    ==========================================
    Cash on Cash Return on Investment: %{prop_obj.roi}\n"""
            )

class AppControl:
    def __init__(self):
        self.all_users = {}
        self.active_user = None

    def control_create_user(self, user):
        self.all_users[user.profile_name] = user

    def control_toggle_user(self, user_obj):
        self.active_user = user_obj

    def control_edit_user(self, user_obj, option, new_name=None):
        if option == "delete":
            if user_obj is self.active_user:
                self.active_user = None
            del self.all_users[user_obj.profile_name]
        if option == "rename" and new_name != None:
            user_obj.profile_name = new_name

    def control_add_property(self, property):
        self.active_user.portfolio[property.address] = property
        return self.active_user

    def control_edit_property(
        self,
        property,
        option,
        *,
        upd_address=None,
        upd_gross=None,
        upd_expenses=None,
        upd_investment=None,
    ):
        if option == "revise":
            if upd_address is not None:
                property.address = upd_address
            if upd_gross is not None:
                property.gross = int(upd_gross)
            if upd_expenses is not None:
                property.expenses = int(upd_expenses)
            if upd_investment is not None:
                property.investment = int(upd_investment)
        if option == "delete":
            del self.active_user.portfolio[property.address]


class AppView:
    def __init__(self, controller, team):
        self.controller = controller
        self.team = team
        self.teams_list = {}
        self.teams.append(self)
        print("="*10, "Welcome to your Portfolio!", "="*10)

    def view_create_user(self):
        profile_name = input("What would you like your account name to be? ")
        u = User(profile_name.strip().lower())
        self.controller.control_create_user(u)
        print(f"\nAdded {profile_name} to the co-op account")
        return

    def view_toggle_user(self):
        choice_dict = {}
        for i, profile_name in enumerate(self.controller.all_users.items()):
            print(f"[{i+1}] {profile_name[0].title()}")
            choice_dict[str(i + 1)] = profile_name[1]
        toggle = input("\nWhich profile would you like to view? ")
        try:
            self.controller.control_toggle_user(choice_dict[toggle])
            print(f"Switched user to {choice_dict[toggle].profile_name.title()}")
            return
        except Exception as err:
            print("\nInvalid input. Please try again")
            self.view_toggle_user()

    def view_edit_user(self):
        choice_dict = {}
        for i, profile_name in enumerate(self.controller.all_users.items()):
            print(f"[{i+1}] {profile_name[0].title()}")
            choice_dict[str(i + 1)] = profile_name[1]
        toggle = input("\nWhich profile would you like to edit? ")
        print("Which would you like to do?")
        option = input("\n[1] Change profile name? [2] Delete Profile? ")
        if option == "2":
            print(
                "Are you sure? This is permanent and your profile cannot be retrieved again after deleting. Type your profile name to confirm"
            )
            confirm = input("")
            if confirm.lower() == choice_dict[toggle].profile_name:
                self.controller.control_edit_user(choice_dict[toggle], "delete")
            print(f"{choice_dict[toggle]} was deleted")
            return

        if option == "1":
            new_name = input("What would you like to change your name to?")
            self.controller.control_edit_user(choice_dict[toggle], "rename", new_name)

    def display_portfolio(self):
        if not self.controller.active_user.portfolio:
            print("Your portfolio is currently empty. Add some properties!")
        else:
            self.controller.active_user.display_portfolio()

    def view_new_property(self):
        address = input("\nWhat is the address for this property? ")
        investment = input(
            "\nFor this property, what is the total for your initial investment? "
        )
        gross = input(
            "\nFor this property, what is the total for your monthly gross income? "
        )
        expenses = input("\n For this property, what is your total monthly expenses? ")
        p = Property(address.lower(), int(gross), int(expenses), int(investment))
        self.controller.control_add_property(p)
        print(
            f"\nExcellent, we added {p.address.title()} to your investment portfolio. You are getting a %{p.roi} return on investment. Neat.\n"
        )
        return

    def view_edit_property(self):
        if not self.controller.active_user:
            print("Your portfolio is currently empty. Add some properties!")
            return
        choice_dict = {}
        for i, property in enumerate(self.controller.active_user.portfolio.items()):
            print(f"[{i+1}] {property[0].title()}")
            choice_dict[str(i + 1)] = property[1]
        toggle = input("\nWhich property would you like to edit? ")
        option = input("[1] Change details\n[2] Delete the property from your portfolio? ")
        if option == "2":
            print("Are you sure? This cannot be undone ")
            check = input("Type the address of your property to confirm ")
            if check.lower() == choice_dict[toggle].address:
                self.controller.control_edit_property(choice_dict[toggle], "delete")
                print(f"Deleted {choice_dict[toggle].address}")
        if option == "1":
            editing = True
            while editing == True:
                print("Which detail would you like to change? ")
                edit = input("[1]Address [2]Investment [3]Expenses [4]Income")
                revision = input("What is your new value? ")
                if edit == "1":
                    self.controller.control_edit_property(
                        choice_dict[toggle], "revise", upd_address=revision
                    )
                    print(f"Updated {choice_dict[toggle].address} address")
                if edit == "2":
                    self.controller.control_edit_property(
                        choice_dict[toggle], "revise", upd_investment=revision
                    )
                    print(f"Updated {choice_dict[toggle].address} investment")
                if edit == "3":
                    self.controller.control_edit_property(
                        choice_dict[toggle], "revise", upd_expenses=revision
                    )
                    print(f"Updated {choice_dict[toggle].address} expenses")
                if edit == "4":
                    self.controller.control_edit_property(
                        choice_dict[toggle], "revise", upd_income=revision
                    )
                    print(f"Updated {choice_dict[toggle].address} income")
                loop = input("\nWould you like to make more revisions to this property? [Y/N] ")
                if loop.lower() == "n":
                    break
                    editing = False
                if loop.lower() == "y":
                    continue

    def run(self):
        run = True
        while run == True:
            if not self.controller.all_users:
                print("Let's add a user to get you started.\n")
                self.view_create_user()
            if self.controller.active_user is None:
                print(
                    "You currently don't have an active user chosen. Please set one\n"
                )
                self.view_toggle_user()
            print("\nWhat would you like to do?")
            print(f"Active User: {self.controller.active_user.profile_name.title()}") 
            print(
                """
[1] Change Profile
[2] Add Profile
[3] Edit Profiles
[4] View your portfolio
[5] Add a new property to your portfolio
[6] Edit your portfolio
[7] Quit
        """
            )
            menu_select = input("")
            if menu_select == "1":
                self.view_toggle_user()
            elif menu_select == "2":
                self.view_create_user()
            elif menu_select == "3":
                self.view_edit_user()
            elif menu_select == "4":
                self.display_portfolio()
            elif menu_select == "5":
                print("Just a few questions...")
                self.view_new_property()
            elif menu_select == "6":
                self.view_edit_property()
            elif menu_select == "7":
                print("Cash money! Have a nice day!")
                run = False
                break


class Property:
    def __init__(self, address, gross, expenses, investment):
        self.address = address
        self.gross = gross
        self.expenses = expenses
        self.investment = investment
        self.net = self.gross - self.expenses
        self.roi = int(((self.net * 12) / self.investment) * 100)

def main():
    team_name = input("What is your team name? ")
    if team_name.lower().strip() in AppView.teams: 
        print("Welcome Back!")
        team_name.run
    else:
        control = AppControl()
        team_name = AppView(control, team_name)
        team_name.run()

if __name__ == "__main__":
    main()