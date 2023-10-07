# Email Automation Scripts

This repository contains Python scripts for automating email tasks using the `smtplib` library. Whether you want to send motivational quotes every Monday or birthday wishes, these scripts provide a foundation for automating your email communications.

## Motivation Monday Emails

The script in `main.py` sends a motivational quote every Monday. The quotes are sourced from a file named `quotes.txt`, and a random quote is selected each Monday to be sent via email. Ensure you have your email credentials set up in the script, and don't forget to replace `"your email"` and `"your email password"` with your actual email address and password.

### Usage

1. Open `quotes.txt` and add motivational quotes, each on a new line.
2. Configure your email credentials in the script.
3. Run the script. If it's Monday, a motivational quote will be sent to the specified email address.

## Birthday Emails

The `birthday_email.py` script sends birthday wishes to individuals whose birthdays match the current date. The script reads birthday data from a CSV file named `birthdays.csv` and sends personalized birthday emails using templates from the `letter_templates` folder. Make sure to update your email credentials and provide accurate file paths.

### Usage

1. Update the `birthdays.csv` file with the names, emails, and birthdays of the individuals you want to send birthday wishes to.
2. Customize the birthday email templates in the `letter_templates` folder.
3. Configure your email credentials in the script.
4. Run the script. If it's someone's birthday, a personalized email will be sent.

## Note

If you encounter any issues with signing into your Gmail account, refer to [this article](https://levelup.gitconnected.com/an-alternative-way-to-send-emails-in-python-5630a7efbe84) for alternative methods.

To run these scripts on the cloud and send daily emails, consider using [pythonanywhere.com](https://www.pythonanywhere.com/).

Feel free to customize and extend these scripts to suit your specific use case. Happy automating!
