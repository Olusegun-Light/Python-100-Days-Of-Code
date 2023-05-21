# Functions with output

# def format_name():
#     f_name = input("What's your first name? ").capitalize()
#     l_name = input("What's your last name? ").capitalize()
#     print(f_name + " " + l_name)

format_name()

def format_name(f_name, l_name):
    formattted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formattted_f_name} {formatted_l_name}"


formated_string = format_name("LiGHt", "OlUsEguN")
print(formated_string)





