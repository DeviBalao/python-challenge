# Code for PyPoll
import os
import csv

# Initialize variables
ballot_Id_list = []
candidate_list = []
candidates = []
vote_count_list = []
vote_percent_list = []
total_votes = 0

filename = "election_data.csv"
#folderpath = os.path.join ("C:","Devi_Files","BootCamp","GitHub","python-challenge","PyPoll","Resources")
folderpath = "C:\Devi_Files\BootCamp\GitHub\python-challenge\PyPoll\Resources"
filepath = os.path.join (folderpath,filename)
#print (filepath)

# Read csv file
with open(filepath) as election_datafile:
    csvreader = csv.reader (election_datafile,delimiter=",")
    csvheader = next(csvreader)
    #print (f"CSV Header: {csvheader}")

    # Storing data from CSV file in lists
    for ballot_Id,county,candidate in csvreader:
        ballot_Id_list.append(ballot_Id)
        candidate_list.append(candidate)
   
   # Getting total votes
    total_votes = len(ballot_Id_list)

    # Unique candidates
    candidates = list(set(candidate_list))
    candidates.sort()
    
    for candidate in candidates:        
        # Getting  number of votes for each candidate and storing it in a list
        vote_count_list.append(candidate_list.count(candidate))

        # Getting percent of votes for each candidate and storing it in a list
        vote_percent_list.append((candidate_list.count(candidate) / total_votes) * 100)

    # Get the Winner
    maxvote = max(vote_count_list)
    winner = candidates[vote_count_list.index(maxvote)]    

    # Print the Election Results
    print ("Election Results")
    print ("-------------------------------")
    print (f"Total Votes: {total_votes}")   
    print ("-------------------------------")
    for candidate in zip(candidates,vote_percent_list,vote_count_list):        
        print(f"{candidate[0]}: {candidate[1]:.3f}% ({candidate[2]})")
    print ("-------------------------------")
    print(f"Winner: {winner}")
    print ("-------------------------------")

