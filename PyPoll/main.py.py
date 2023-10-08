import csv
import os

# Initialize variables
total_votes = 0
candidates = {}
winner_name = ""
winner_votes = 0

#csv variables for reading files


#folder path for csv file
csv_folder = r"C:\Users\brightburn\Desktop\Data bootcamp\python-challenge\PyPoll\Resources"

#csv file name
csv_file = "election_data.csv"

#full path to csv file
csv_file_path = os.path.join(csv_folder, csv_file)


# Read data from CSV file using csv.DictReader
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # Loop through the data to calculate total votes and count votes for each candidate. Adds candidate name with total votes for each candidate
    for row in csvreader:
        
        total_votes += 1
        candidate_name = row['Candidate'] # extracts the value assoicated with the key [Candidate]. Assuming there is a column named "Candidate"
        candidates[candidate_name] = candidates.get(candidate_name, 0) + 1 # Checks if "candidate_name" is already a key in the "candidates" dictionary. If it is in the dictionary adds 1 to count and if it's not adds the key to the dictionary with 1 to the count 
    #print('before per:',candidates)#for better understanding 

    # Calculate the percentage of votes each candidate won. The candidates dictionary is transformed into a nested dictionary. New dictionary is created inside of the dictionary with values of votes and percentage. 
    for candidate, votes in candidates.items():#iterating over the [candidates] dictionary. 
        percentage = (votes / total_votes) * 100

        #print("dic:",candidates)#for better understanding

        candidates[candidate] = {"votes": votes, "percentage": percentage}

    # Find the winner based on popular vote. Iterates through the [candidates] dictionary. For each iteration,'candidate' represents the candidate name and 'infor' represents the inner dictionary containing their votes and percentage.  
    for candidate, info in candidates.items():
        if info["votes"] > winner_votes:
            winner_name = candidate
            winner_votes = info["votes"]
        #print('info',info)# for better understanding 

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, info in candidates.items():
    print(f"{candidate}: {info['percentage']:.3f}% ({info['votes']})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")


# folder for output
output_folder = 'analysis'

# if folder doesn't exist create folder
os.makedirs(output_folder, exist_ok=True)



# Output the election results to a text file
output_file = os.path.join(output_folder, "election_results.txt")
with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, info in candidates.items():
        txtfile.write(f"{candidate}: {info['percentage']:.3f}% ({info['votes']})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write("-------------------------\n")

print(f"Results have been saved to {output_file}")
