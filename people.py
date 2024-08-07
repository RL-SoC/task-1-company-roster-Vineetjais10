"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str 
    age : int
    ID : int
    city : int
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
    
    def change_city(self, new_city:str) -> bool:
        # Change the city 
        # Return true if city change, successful, return false if city same as old city
        if self.city != new_city:
            self.city = new_city
            return True
        return False
        pass

    def migrate_branch(self, new_code:int) -> bool:
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        # Change old branch to new if it is in the same city, else return false.
        if len(self.branches) == 1:
            old_branch = self.branches[0]
            old_city = branchmap[old_branch]["city"]
            new_city = branchmap[new_code]["city"]
            if old_city == new_city:
                self.branches[0] = new_code
                return True
        return False
        pass

    def increment(self, increment_amt: int) -> None:
        # Increment salary by amount specified.
        self.salary += increment_amt
        pass





class Engineer(Employee):
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        # Only then set the position. 
        valid_positions = ["Junior", "Senior", "Team Lead", "Director"]
        if position in valid_positions:
            self.position = position

    
    def increment(self, amt:int) -> None:
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        self.salary +=(amt+amt*0.10)
        pass
        
    def promote(self, position:str) -> bool:
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        
        valid_positions = ["Junior", "Senior", "Team Lead", "Director"]
        if position in valid_positions and valid_positions.index(position) > valid_positions.index(self.position):
            # Calculate 30% of the present salary
            increment_amt = int(0.30 * self.salary)
            # Call the increment function
            self.increment(increment_amt)
            # Update the position
            self.position = position
            return True
        return False 
        pass



class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to
    position: str

    def __init__(self, name, age, ID, city, branchcodes, position="Rep", superior=None, salary=None):
        # Complete all this! Add arguments
        # Check if position is one of "Rep", "Manager", "Head"
        valid_positions = ["Rep", "Manager", "Head"]
        if position in valid_positions:
            self.position = position
        else:
            raise ValueError("Invalid position for Salesman")
        
        super().__init__(name, age, ID, city, branchcodes, salary)
        self.superior = superior
        
    def promote(self, new_position: str) -> bool:
        valid_positions = ["Rep", "Manager", "Head"]
        
        # Check if the new position is valid and a promotion
        if new_position in valid_positions and valid_positions.index(new_position) > valid_positions.index(self.position):
            # Call the increment function
            self.increment()
            # Update the position
            self.position = new_position
            # Set superior to None if promoted to "Head"
            if new_position == "Head":
                self.superior = None
            return True
        return False
        
    def increment(self) -> None:
        increment_amt = int(0.05 * self.salary)
        self.salary += increment_amt

    def find_superior(self) -> tuple[int, str]:
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        if self.superior is None:
            return (None, None)
        for employee in sales_roster + engineer_roster:
            if employee.ID == self.superior:
                return (employee.ID, employee.name)
        return (None, None)

    def add_superior(self, superior_id: int) -> bool:
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,
        valid_positions = ["Rep", "Manager", "Head"]
        if self.position == "Head":
            return False
        
        for employee in sales_roster + engineer_roster:
            if employee.ID == superior_id and valid_positions.index(employee.position) > valid_positions.index(self.position):
                self.superior = superior_id
                return True
        return False

    def migrate_branch(self, new_code: int) -> bool:
        # This should simply add a branch to the list; even different cities are fine
        if new_code not in self.branches:
            self.branches.append(new_code)
            return True
        return False

    





    
    
