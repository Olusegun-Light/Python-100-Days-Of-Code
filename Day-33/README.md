# Application Programming Interface (API)

## ISS Tracker and Kanye Quote Generator

This repository contains two Python scripts:

### ISS Tracker (main.py)

This script tracks the International Space Station (ISS) and sends an email notification if the ISS is overhead at night. The script uses the Open Notify API to get the current position of the ISS and the Sunrise Sunset API to determine if it's night at your specified location.

#### Usage

1. Get your current location's latitude and longitude from [LatLong.net](https://www.latlong.net/).
2. Replace `MY_LAT` and `MY_LONG` with your latitude and longitude.
3. Configure your email credentials by setting `My_Email` and `My_Password`.
4. Run the script. If the ISS is overhead and it's night, you'll receive an email notification to look up.

### Kanye Quote Generator (kanye/main.py)

This script creates a simple Tkinter GUI that displays random Kanye West quotes. It uses the Kanye.rest API to fetch quotes and updates the GUI with a new quote each time you click the Kanye image.

#### Usage

1. Ensure you have Tkinter installed (`pip install tk`).
2. Run the script to open the GUI.
3. Click the Kanye image to get a new Kanye quote.

Feel free to explore and customize these scripts for your needs. If you encounter any issues or have suggestions, feel free to contribute or open an issue.

**Note**: For the ISS Tracker, if you face any authentication errors while using Gmail, consider [this alternative method](https://levelup.gitconnected.com/an-alternative-way-to-send-emails-in-python-5630a7efbe84).

Happy coding!
