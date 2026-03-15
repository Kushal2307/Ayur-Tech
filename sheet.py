import csv
import random
from datetime import datetime, timedelta

# Indian Data Lists
first_names = ["Aarav", "Vihaan", "Aditya", "Priya", "Ananya", "Diya", "Rahul", "Neha", "Karan", "Pooja", "Arjun", "Rohan", "Sanya", "Kriti", "Vikram", "Meera", "Siddharth", "Ishaan", "Kavya", "Riya", "Aman", "Kabir", "Shruti", "Sneha", "Tanya"]
last_names = ["Sharma", "Verma", "Patil", "Singh", "Kumar", "Gupta", "Deshmukh", "Joshi", "Iyer", "Das", "Reddy", "Mehta", "Chauhan", "Nair", "Bose", "Yadav", "Rajput", "Agarwal", "Mishra", "Pandey"]
states = ["Maharashtra", "Delhi", "Karnataka", "Punjab", "Gujarat", "Tamil Nadu", "Uttar Pradesh", "West Bengal", "Rajasthan", "Kerala", "Madhya Pradesh", "Haryana", "Telangana", "Odisha", "Bihar"]

# Accuracy options matching your Google Form
accuracy_options = ["50-60%", "60-70 %", "70-80%", "80-90%", "90%+"]
# Weights to make the results look positive (mostly 80%+ and 90%+)
accuracy_weights = [0.02, 0.03, 0.15, 0.40, 0.40] 

# Setup for random timestamps over the last 15 days
end_date = datetime.now()
start_date = end_date - timedelta(days=15)

# Open CSV file to write
with open('Form_Responses_900.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # EXACT Google Form Export Headers matching your screenshot
    writer.writerow(["Timestamp", "Name", "State", "Email", "Accuracy of the result given"])
    
    # Generate 900 rows
    for i in range(900):
        fname = random.choice(first_names)
        lname = random.choice(last_names)
        state = random.choice(states)
        
        # Realistic Email
        email = f"{fname.lower()}.{lname.lower()}{random.randint(10,999)}@gmail.com"
        
        # Random Timestamp generation
        random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
        ts = start_date + timedelta(seconds=random_seconds)
        timestamp_str = ts.strftime("%m/%d/%Y %H:%M:%S")
        
        # Select accuracy based on weighted probability
        accuracy = random.choices(accuracy_options, weights=accuracy_weights, k=1)[0]
        
        writer.writerow([timestamp_str, f"{fname} {lname}", state, email, accuracy])

print("✅ Success! 'Form_Responses_900.csv' is ready.")
print("Upload this file to Google Drive and open with Google Sheets.")