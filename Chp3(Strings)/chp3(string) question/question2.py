letter="Dear <|Name|>,\nYou are selected !\n<|Date|>"

from datetime import datetime

# Get the current date and time
current_date = datetime.now()

# Format the date as YYYY-MM-DD
formatted_date = current_date.strftime('%Y-%m-%d')

entered_name=input("You're name please: ")
letter=letter.replace("<|Name|>", entered_name )
letter=letter.replace("<|Date|>", formatted_date)
print(letter)