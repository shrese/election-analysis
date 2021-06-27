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

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
#    open(file_to_load, 'r')
    
#with open(file_to_save) as election_analysis:
#    txt_file = open(file_to_save, 'w')
#    txt_file.write(f"Counties in the Election\n")
#    txt_file.write(f"-------------------------\n")
#    txt_file.write(f"Arapahoe\nDenver\nJefferson")
        
    #read and print the header row
#    print(election_data)

# Read the file object with the reader function.
    #file_reader = csv.reader(election_data)
    #headers = next(file_reader)
     #   print(headers)

# Print each row of the csv file.
   
    #for row in file_reader:
     #   print(row)

election_data.close()
