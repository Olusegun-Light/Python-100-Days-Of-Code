# from turtle import Turtle, Screen

# my_turtle =Turtle()
# my_turtle.color("coral")
# my_turtle.forward(100)

# my_screen = Screen()
# my_screen.exitonclick()


from prettytable import PrettyTable

# Create Object 
table = PrettyTable()

#  Addd objects to the table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electruc", "Water", "Fire"])

#  Aligh table
table.align = "l"

print(table)