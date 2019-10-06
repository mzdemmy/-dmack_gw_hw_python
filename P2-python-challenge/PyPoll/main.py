# -*- coding: UTF-8 -*-
"""PyPoll Homework Solution."""

# Incorporated the csv module
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Vote Counter
vote_counter = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
    
    # For each row...
    for row in reader:

        # Run the loader animation
        print(". ", end=""),

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        
        if candidate_name not in candidate_options:
            #reset and add count to vote_counter
            vote_counter = 1
            
            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)  

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
            
#sanity check
# print(candidate_options)
# for x,y in candidate_votes.items():
#     print (x, ":", y)
    

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    print(f"\nElection Results\n")
    print(f"----------------------------\n")
    print(f"Total Votes: {total_votes}")

    # Save the final vote count to the text file
    txt_file.write("Election Results\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}")
                
    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)  
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
        
        # Print each candidate's voter count and percentage (to terminal)
        print(f"\n{candidate}: {vote_percentage} ({votes})")
                
        # Save each candidate's voter count and percentage to text file
        txt_file.write(f"\n{candidate}: {vote_percentage} ({votes})")

    # Print the winning candidate (to terminal)
    print(f"\nWinning Candidate: {winning_candidate}")

    # Save the winning candidate's name to the text file
    txt_file.write(f"\nWinning Candidate: {winning_candidate}")

    txt_file.close()
