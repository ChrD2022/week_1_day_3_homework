def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string_length):
    return len(string_length)
    
def join_string(string_1, string_2):
    joined_string = string_1 + string_2
    return joined_string

def add_string_as_number(str_1, str_2):
    return int(str_1) + int(str_2)

def number_to_full_month_name(month_num):
    months = {
        1 : "January",
        2 : "February",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December"
    }
    return months.get(month_num)

def number_to_short_month_name(month_num):
    months = {
        1 : "Jan",
        2 : "Feb",
        3 : "Mar",
        4 : "Apr",
        5 : "May",
        6 : "Jun",
        7 : "Jul",
        8 : "Aug",
        9 : "Sep",
        10 : "Oct",
        11 : "Nov",
        12 : "Dec"    
    }
    return months.get(month_num)

def volume_of_cube(length):
    return length **3 
    
def reverse_string(string):
    return string[::-1]

def farenheit(temp):
    return (temp - 32) * 5/9
