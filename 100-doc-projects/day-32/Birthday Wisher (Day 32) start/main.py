import smtplib
import datetime as dt
import random

my_email = "swetsagar7@gmail.com"
password ="dylx byvi qcxw dxmo"

now = dt.datetime.now()  # Get the current date
weekday = now.weekday()  # Get the current day of the week (0=Monday, 6=Sunday)

if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)  # Randomly select a quote from the list
        
    print(quote)
    
    with  smtplib.SMTP("smtp.gmail.com", 587) as connection : 
        connection.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        connection.login(user=my_email, password=password)  # Replace with your actual password
        connection.sendmail(from_addr=my_email, to_addrs="swet.sagar93@gmail.com", msg=f"Subject:Happy Birthday \n\n{quote}")  # Replace with the recipient's email address and your message")
        connection.close()  # Close the connection after sending the email
