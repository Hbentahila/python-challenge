# Importing OS and CSV modules 
import os
import csv

# Creating dictionaries/variables to store data
candidates_votes={}
total_votes= 0

# Command prompt should be opened in Folder PyPoll
election_csv= os.path.join("Resources", "election_data.csv")

# Opening the csv file election_data.csv
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Reading and skipping the header row
    csv_header = next(csvreader)

    # Looping through our csv file and using conditional statements to: 
    # For each unique candidate, store in the dictionary "candidates_votes" : 
    #     * The candidate name as "Key" and
    #     * The total number of votes as "value" and 
    # Calculating the total number of votes (total_votes)
    for row in csvreader:
        if row[2] in candidates_votes:
            candidates_votes[row[2]]+= 1
        else: candidates_votes[row[2]]= 1
        total_votes+= 1
    
    # Determining the winner of the election based on popular vote
    winner=max(candidates_votes, key=candidates_votes.get)

    # Printing to the terminal the first section of the results including :
    # The title and and total number of votes
    print(f"""Election Results\n\n--------------------------
    \nTotal Votes: {total_votes}
    \n--------------------------\n""")

    # Looping through our dictionary and printing to the terminal:
    #   * The list of candidates who received votes
    #   * Their percentage and total number of votes 
    for a in candidates_votes: 
        print(f"{a} : {round(((candidates_votes[a]/total_votes)*100), 3)}% ({candidates_votes[a]})\n")

    # Printing to the terminal the last section of the results including the winner
    print(f"""--------------------------
    \nWinner: {winner}
    \n--------------------------""")


# Exporting a text file with the results 
# (3 sections similar to results printed to the terminal)
votes_output= "Analysis/votes_results.txt"
writer= open(votes_output, "w") 

writer.write(f"""Election Results\n\n--------------------------
            \nTotal Votes: {total_votes}
            \n--------------------------\n\n""")

for a in candidates_votes: 
    writer.write(f"{a} : {round(((candidates_votes[a]/total_votes)*100), 3)}% ({candidates_votes[a]})\n\n")

writer.write(f"""--------------------------
            \nWinner: {winner}
            \n--------------------------""")