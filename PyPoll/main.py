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
folderpath = os.path.join ("Resources")
filepath = os.path.join (folderpath,filename)


# Read csv file
with open(filepath) as election_datafile:
    csvreader = csv.reader (election_datafile,delimiter=",")
    csvheader = next(csvreader)    

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


analysisfilename = "results.txt"
analysisfolderpath = os.path.join ("analysis")
analysisfilepath = os.path.join(analysisfolderpath, analysisfilename)


# Write results to a file
with open(analysisfilepath,"w") as analysisfile:
    # Write the Election Results
    analysisfile.write("Election Results\n")
    analysisfile.write ("------------------------------------------------\n")
    analysisfile.write (f"Total Votes: {total_votes}\n")   
    analysisfile.write ("------------------------------------------------\n")
    for candidate in zip(candidates,vote_percent_list,vote_count_list):        
        analysisfile.write(f"{candidate[0]}: {candidate[1]:.3f}% ({candidate[2]})\n")
    analysisfile.write ("------------------------------------------------\n")
    analysisfile.write(f"Winner: {winner}\n")
    analysisfile.write ("------------------------------------------------")
