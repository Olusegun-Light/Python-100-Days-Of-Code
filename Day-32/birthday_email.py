import random
import smtplib
import datetime as dt
import pandas

today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")

my_email = "your email"
my_password = "your password"

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",  port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email, to_addrs=birthday_person['email'], msg=f"Subject:Happy Birthday!\n\n{contents}")
