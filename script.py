from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from string import Template


# Function to read the contacts from a given contact file and return a
# list of names and email addresses
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


# import the smtplib module. It should be included in Python by default
# set up the SMTP server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('my_email_address', 'my_pass')

names, emails = get_contacts('mycontacts.txt')  # read contacts
message_template = read_template('message.txt')


# For each contact, send the email:
for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title())

    # setup the parameters of the message
    msg['From'] = "my_email_address"
    msg['To'] = email
    msg['Subject'] = "This is TEST"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)

    del msg
