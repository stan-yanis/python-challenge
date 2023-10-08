import csv
import os


# Path to CSV folder
csv_folder = r"C:\Users\brightburn\Desktop\Data bootcamp\python-challenge\PyBank\Resources"

#CSV file name
csv_file = "budget_data.csv"

# Full path to CSV file
csv_file_path = os.path.join(csv_folder, csv_file)

#Initialize varibles 

total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
dates = []

# Open the CSV file in read mode
with open(csv_file_path, 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.DictReader(csvfile)


    # Iterate through each row in the csv file 
    for row in csvreader:
        # Calulate total months and net total
        total_months += 1

        net_total += int(row['Profit/Losses'])


        # Calculate changes in profit/loss

        current_profit_loss = int(row['Profit/Losses'])

        if total_months > 1:
            change = current_profit_loss - previous_profit_loss

            changes.append(change)
            dates.append(row['Date'])

        previous_profit_loss = current_profit_loss


# Calculate average change
average_change = round(sum(changes) / len(changes), 2)


# Find greatest increase and decrease in profits

greatest_increase  = max(changes)
greatest_increase_index = changes.index(greatest_increase)
greatest_increase_date = dates[greatest_increase_index]

greatest_decrease = min(changes)
greatest_decrease_index = changes.index(greatest_decrease)
greatest_decrease_date = dates[greatest_decrease_index]


# print the financial analysis on the screen

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")





#The name of the folder for the output
output_folder = "analysis"

#If folder doesn't exist creates folder
os.makedirs(output_folder, exist_ok=True)

#Outputs the text file to the specified folder
output_file = os.path.join(output_folder, "Financial Analysis.txt")
with open(output_file, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")


# Displays location of the text file
print(f"Results have been saved to {output_file}")


