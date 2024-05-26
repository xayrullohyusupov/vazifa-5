def filter_gmail(email_list):
    gmail = [email for email in email_list if email.endswith('@gmail.com')]
    return gmail


email_list = [
    'xaker11@gmail.com',
    'xaker01@yahoo.com',
    'xaker_aka@hotmail.com',
    'xakerbek@gmail.com',
    'xaker@domain.com'
]

gmail = filter_gmail(email_list)
print("Gmail manzillar:")
for email in gmail:
    print(email)
