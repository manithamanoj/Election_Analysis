# Add our dependencies
import csv
import os


# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of  votes each candidates won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
 # Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize the total vote counter
total_votes=0
# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file
    #for row in file_reader:
       # for row in file_reader:
         # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
         # 2. Add to the total vote count.
         total_votes += 1
         # 3. Print the total votes.
         #print(total_votes)
         # Print the candidate name from each row.
         candidate_name = row[2]
         # If the candidate does not match any existing candidate...
         if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

         candidate_votes[candidate_name] += 1
         

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
 print(total_votes)
 print(candidate_options)

 print(candidate_votes)

# 1. Iterate through the candidate list.
 for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    candidate_results = (f"{candidate_name}: received {round(vote_percentage,1)}% of the vote.\n")

  #Print candidate list
   
#  Save the candidate results to our text file.
    print(candidate_results)
# Determine if the votes is greater than the winning count.
    txt_file.write(candidate_results)

    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
       winning_count = votes
       winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
       winning_candidate = candidate_name
 winning_candidate_summary = (
 f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
 print(winning_candidate_summary) 
 txt_file.write(winning_candidate_summary)
 
 # Print the final vote count to the terminal.
 election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
 print(election_results, end="")
# Save the results to our text file.

    # Save the final vote count to the text file.
 txt_file.write(election_results)
  
 
 
    