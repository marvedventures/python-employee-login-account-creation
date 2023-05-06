###########################################################################################################################################
# EMPLOYEE ACCOUNT MANAGEMENT
###########################################################################################################################################

# Input data: List of dictionaries
employee_list = [
    {'id': 12345, 'name': 'John', 'department': 'Kitchen'},
    {'id': 12456, 'name': 'Paul', 'department': 'House Floor'},
    {'id': 12478, 'name': 'Sarah', 'department': 'Management'},
    {'id': 12434, 'name': 'Lisa', 'department': 'Cold Storage'},
    {'id': 12483, 'name': 'Ryan', 'department': 'Inventory Mgmt'},
    {'id': 12419, 'name': 'Gill', 'department': 'Cashier'}
]


# Function to be passed to the map() function.
def mod(employee_list):
    temp = employee_list['name'] + '_' + employee_list['department']
    return temp


# Modifies the employee list of dictionaries into list of employee_department strings
def to_mod_list(employee_list):
    return list(map(mod, employee_list))


# Generates a list of usernames
def generate_usernames(mod_list):
    return [el.replace(' ', '_') for el in mod_list]


# Maps employee id to first 4 letters of name
def map_id_to_initial(employee_list):
    return {el['id']: el['name'][:4] for el in employee_list}


def main():
    mod_emp_list = to_mod_list(employee_list)
    # Modified employee list: ['John_Kitchen', 'Paul_House Floor', 'Sarah_Management', 'Lisa_Cold Storage', 'Ryan_Inventory Mgmt', 'Gill_Cashier']
    print(f'Modified employee list: {mod_emp_list} \n')

    # List of usernames: ['John_Kitchen', 'Paul_House_Floor', 'Sarah_Management', 'Lisa_Cold_Storage', 'Ryan_Inventory_Mgmt', 'Gill_Cashier']
    print(f'List of usernames: {generate_usernames(mod_emp_list)}\n')

    # Initials and ids: {12345: 'John', 12456: 'Paul', 12478: 'Sara', 12434: 'Lisa', 12483: 'Ryan', 12419: 'Gill'}
    print(f'Initials and ids: {map_id_to_initial(employee_list)}')


if __name__ == '__main__':
    main()
