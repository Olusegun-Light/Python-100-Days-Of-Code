import random
import smtplib
import datetime as dt


################## Starting up with sending emails ##################
my_email = "your email"
my_password = "your email password"
to_email = "recipient email"

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    # tls -> transport layer security, tls makes the connection secure
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=to_email,
                        msg="Subject:Hello\n\nThis the body of the email")


################## Send Monday Motivation Quotes emails ##################
now = dt.datetime.now()
weekday = now.weekday()
# The line `
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com",  port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject: Monday Motivation\n\n{quote}")
