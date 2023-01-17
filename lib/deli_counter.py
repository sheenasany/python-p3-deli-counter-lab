katz_deli = []

def line(line_list):
    if len(line_list) == 0:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for place_num in range(len(line_list)):
            message += f' {place_num + 1}. {line_list[place_num]}'
        print(message)
    # if len(katz_deli) == 0:
    #     print(f'The line is currently empty.')
    # elif len(katz_deli) > 0:
    #     print(f'The line is currently:')

def take_a_number(line_list, new_person):
    line_list.append(new_person)
    print(f'Welcome, {new_person}. You are number {len(line_list)} in line.')

def now_serving(line_list):
    if len(line_list) == 0:
        print(f'There is nobody waiting to be served!')
    else: 
        len(line_list) > 0
        print(f'Currently serving {line_list[0]}.')
        del(line_list[0])