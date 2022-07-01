

Organization Ideas

class Property: 
    Attributes: 
        -Name/Address 4242 drurey ln  
        -Gross Income(calulated from list of variables? do we want to edit these?)
            -Rent
            -Etc
        -Expenses
            -List of a million things
        -Initial Investment 
            -Downpay/ Closing/ Rehabilitation/ Misc
    Methods: (handled in the init logic) 
        - Calculate Net Income 
        - Calculate ConCROI 

class App: 
*Does it need to maintain state? Reaccess the user everytime?
    Attributes: 
        -Active User
        -Collection of all Users
    Methods: 
        - Accesses User portfolio and information 
        - Toggle Active User
        - Gathers input to create property object
        - Run 
            Create User and User List
            Collect Property Information (million inputs)
            Manage menus for input and viewing 

class Users: 
    Attributes: 
        - Name/Username 
        - Portfolio (Dictionary?) 
        -   {"Property.name" : Property }
    Methods:
        - Maintain crud? portfolio of objects 
        - Edit Own User Account information

    