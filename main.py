history = []
print("Welcome to the retail store chatbot")
name = input("What is your name? ")
email = input("What is your email? ")

while True:
    response = input("Are you returning or exchanging an item? ").lower()
    if response in ["returning", "exchanging"]:
        break
    else:
        print("Invalid response. Please enter 'returning' or 'exchanging.")

# Add the user's response to the history
history.append(response)

while True:
    retOption = input("Do you want to go back to the previous option or view history? (yes, no, history) ").lower()
    if retOption == "yes" and history:
        response = history.pop()
    elif retOption == "history":
        print("Here is your chat history:")
        for i, entry in enumerate(history, 1):
            print(f"{i}. {entry.capitalize()}")
    else:
        break

if response == "returning":
    retWhy = input("Why are you returning this item? ")
    item = input("What will you be returning? ")
    print("We will return your item soon (THANK YOU).")
elif response == "exchanging":
    excWhy = input("Why are you exchanging this item? ")
    item = input("What will you be exchanging? ")
    excItem = input("What item would you like to exchange for? ")
    print("That's good for us; your trade was approved.")
    print("We will exchange your item soon (THANK YOU).")

feedBack = input("Would you like to give us feedback? (yes or no) ").lower()
if feedBack == "yes":
    feedback = input("Please give us feedback: ")
    print("Thank you for your feedback.")
else:
    print("Thank you for your time.")

print("Thank you for using the retail store chatbot (We have sent you an email).")
