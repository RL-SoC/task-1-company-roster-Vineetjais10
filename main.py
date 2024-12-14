"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import * # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))

        if last_input == 1:
            name = input("Name:")
            ID = input("ID:")
            city = input("City:")
            branchcodes = input("Branch(es):")
            # How will you convert this to a list, given that
            # the user will always enter a comma separated list of branch codes?
            # eg>   2,5
            branchcodes = [int(code) for code in branchcodes.split(',')]
            salary = input("Salary: ")
            # Create a new Engineer with given details.
            engineer = Engineer(name, age=int(input("Age: ")), ID=int(ID), city=city, branchcodes=branchcodes, salary=int(salary))

            engineer_roster.append(engineer) # Add him to the list! See people.py for definition
            
        
        elif last_input == 2:
            name = input("Name: ")
            ID = int(input("ID: "))  # ID should be an integer
            city = input("City: ")
            branchcodes = input("Branch(es): ")
            
            branchcodes = [int(code) for code in branchcodes.split(',')]
            position = input("Position (leave blank for default 'Rep'): ")
            if position.strip() == "":
                position = "Rep"

            superior = input("Superior ID (leave blank if none): ")
            if superior.strip() == "":
                superior = None
            else:
                superior = int(superior)
            
            # Gather input to create a Salesperson
            salesman = Salesman(name, age=int(input("Age: ")), ID=ID, city=city, branchcodes=branchcodes, position=position, superior=superior, salary=int(input("Salary: ")))
            # Then add them to the roster
            sales_roster.append(salesman)
            pass

        elif last_input == 3:
            ID = int(input("ID: "))
            # Print employee details for the given employee ID that is given. 
            
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            
            if not found_employee:
                print("No such employee")
            else:
                print(f"Name: {found_employee.name} and Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")

                ## Write code here to list the branch names to
                ## which the employee reports as a comma separated list
                ## eg> Branches: Goregaon,Fort
                branch_names = [branchmap[code]["name"] for code in found_employee.branches]
                print(f"Branches: {', '.join(branch_names)}")
                
                print(f"Salary: {found_employee.salary}")

        elif last_input == 4:
            #### NO IF ELSE ZONE ######################################################
            # Change branch to new branch or add a new branch depending on class
            # Inheritance should automatically do this. 
            # There should be no IF-ELSE or ternary operators in this zone
            ID = int(input("Enter Employee ID to change branch: "))
            new_branch_code = int(input("Enter new branch code: "))
            
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    if employee.migrate_branch(new_branch_code):
                        print("Branch migrated successfully.")
                    else:
                        print("Failed to migrate branch.")
            #### NO IF ELSE ZONE ENDS #################################################

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            # promote employee to next position
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    # Promote to the next position based on current position
                    positions_engineer = ["Junior", "Senior", "Team Lead", "Director"]
                    positions_salesman = ["Rep", "Manager", "Head"]
                    
                    if isinstance(employee, Engineer):
                        current_position = employee.position
                        new_position = positions_engineer[positions_engineer.index(current_position) + 1]
                        if employee.promote(new_position):
                            print(f"Promoted to {new_position} successfully.")
                        else:
                            print("Promotion failed.")
                    elif isinstance(employee, Salesman):
                        current_position = employee.position
                        new_position = positions_salesman[positions_salesman.index(current_position) + 1]
                        if employee.promote(new_position):
                            print(f"Promoted to {new_position} successfully.")
                        else:
                            print("Promotion failed.")

        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            # Increment salary of employee.
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    increment_amount = int(input("Enter increment amount: "))
                    employee.increment(increment_amount)
                    print(f"Salary incremented to {employee.salary}.")

        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            for employee in sales_roster:
                if employee.ID == ID:
                    superior_info = employee.find_superior()
                    if superior_info[0] is None:
                        print("No superior found.")
                    else:
                        print(f"Superior ID: {superior_info[0]}, Superior Name: {superior_info[1]}")

        elif last_input == 8:
            ID_E = int(input("Enter Employee ID to add superior: "))
            ID_S = int(input("Enter Employee ID of superior: "))
            # Add superior of a sales employee
            for employee in sales_roster:
                if employee.ID == ID_E:
                    if employee.add_superior(ID_S):
                        print("Superior added successfully.")
                    else:
                        print("Failed to add superior.")

        else:
            raise ValueError("No such query number defined")

            
            

            


            


        






