#Data that needs to be received
#1. Total number of regisgered voters
#2. A complete list of candidates that received votes
#3. Total number of votes each candidate received
#4. A list of counties that we will analyze
#5. Percentage of votes for each candidate
#6. The winner of the race

#opening a file in read view
import csv
import os

#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)
    
    #read and print the header row
    headers = next(file_reader)
    print(headers)