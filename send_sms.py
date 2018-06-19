from twilio.rest import Client
from credentials import account_sid, auth_token, twilio_cell

def removeChar(cellphone, index):
	return cellphone[:index] + cellphone[index + 1:]

def main():
	client = Client(account_sid, auth_token)

	my_cell = input("Enter a verified cell phone number beginning with \"+1\": ")
	
	# continue prompting user until "+1" is prefixed
	while my_cell.find("+1") == -1:
		print("ERROR: phone number does not contain prefix \"+1\"")
		my_cell = input("Enter a verified cell phone number beginning with \"+1\": ")

	# remove all whitespace in phone number
	while my_cell.find(" ") != -1:
		my_cell = removeChar(my_cell, my_cell.find(" "))

	# remove dashes in phone number
	while my_cell.find("-") != -1:
		my_cell = removeChar(my_cell, my_cell.find("-"))

	user_message = input("Enter body of text message ('exit' to leave): ")
	user_message = "\"" + user_message + "\""
	while user_message != "\"exit\"":
		message = client.messages.create(to=my_cell, from_=twilio_cell, body=user_message)
		user_message = input("Enter body of text message ('exit' to leave): ")
		user_message = "\"" + user_message + "\""

if __name__ == "__main__":
	main()