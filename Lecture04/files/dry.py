# Repetitive code
def get_user_age():
    age = input("Enter your age: ")
    if int(age) < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")
        
def get_user_height():
    height = input("Enter your height: ")
    if int(height) < 160:
        print("You are short.")
    else:
        print("You are tall.")

# DRY version
def get_user_info(prompt, threshold, low_message, high_message):
    value = input(prompt)
    if int(value) < threshold:
        print(low_message)
    else:
        print(high_message)

get_user_info("Enter your age: ", 18, "You are a minor.", "You are an adult.")
get_user_info("Enter your height: ", 160, "You are short.", "You are tall.")
