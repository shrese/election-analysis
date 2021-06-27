#Data that needs to be received
#1. Total number of regisgered voters
#2. A complete list of candidates that received votes
#3. Total number of votes each candidate received
#4. A list of counties that we will analyze
#5. Percentage of votes for each candidate
#6. The winner of the race

# add dependencies
import os
import csv

#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter 
total_votes = 0

#Candidate options and candidate votes (LIST)
candidate_options = []

#declare the empty dictionary.
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    
    #print each row in the csv file
    for row in file_reader:
        total_votes += 1
    
        #print the candidate name for each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            
            #add the candidate's name to the candidate list
            candidate_options.append(candidate_name)
  
            #begin tracking the candidate's votes
            candidate_votes[candidate_name] = 0
            
        #add votes to the candidate's count
        candidate_votes[candidate_name] += 1
        
    #calculate the percentage of votes for each candidate
    #iterrate through the candidate list
    for candidate_name in candidate_votes:
        
        #retrieve vote count for candidates
        votes = candidate_votes[candidate_name]
        
        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100    
                      
        #determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        
            #if true then set winning count = votes and set winning percentage =  vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            
            #AND set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
            
        #print candidate name and percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)