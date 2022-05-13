# Toggle which scripts to run (1 to run, 0 to skip)
usingLists = 1
usingDicts = 0

if usingLists:
    print('\n===== Using Lists =====\n')

    # Script for analyzing votes (using lists)

    # Import modules
    import os
    import csv

    # Set path for file
    poll_csv = os.path.join('Pyroll\election_data.csv')

    # Open csv file in read mode
    with open(poll_csv, 'r') as pollf:
        poll_data = csv.reader(pollf, delimiter=',')
        
        # Set header
        header = next(poll_data)
        
        # Initialize list for candidates
        cand_l = []

        # Loop through file and add candidates to list
        for row in poll_data:
            cand_l.append(row[2])

    # Count all votes for each candidate
    # using list comprehensions with count function and set
    votes_count = [[c, cand_l.count(c)] for c in set(cand_l)]

    # Sort list of votes per votes count in descending order
    votes_count = sorted(votes_count, key = lambda k: k[1], reverse = True)
    # Calculate total number of votes
    total_votes = len(cand_l)
    # Find winner --> top candidate in sorted list of votes
    winner = votes_count[0][0]

    # === Display and export to text file election results ===
    # Set string variable for a line
    line = f"-------------------------\n"

    # Initialize variable for keeping votes results for all candidates
    out = ""
    # Calculate percent of votes for each candidate and place
    # votes results for all candidates in string variable "out"
    for name, count in votes_count:
        percent_votes = (count / total_votes) * 100
        out = out + f"{name}: {percent_votes:.3f}% ({count})\n"

    # Prepare output with election results
    output = (f"\nElection Results\n" \
        + line +
        f"Total Votes: {total_votes}\n" 
        + line
        + out 
        + line +
        f"Winner: {winner}\n"
        + line
            )

    # Display election results
    print (output)

    # Export election results to text file
    results = os.path.join('election_results.txt')
    with open(results, 'w') as f:
        print(output, file=f)


if usingDicts:
    print('\n===== Using Dictionaries =====\n')

    # Script for analyzing votes (using dictionaries)

    # Import modules
    import os
    import csv

    # Set path for file
    poll_csv = os.path.join('Pyroll\election_data.csv')

    # Set dictionary value increment (1 row = 1 vote)
    n = 1

    # Open csv file in read mode
    with open(poll_csv, 'r') as pollf:
        poll_data = csv.reader(pollf, delimiter=',')

        # Set header
        header = next(poll_data)

        # Initialze dictionary for candidates
        cand_d = {}

        # Loop through file, find candidates (keys), count their votes (values) and add them to dictionary
        # Use get() method to help with first time occurance of keys
        for row in poll_data:
            cand_d[row[2]] = cand_d.get(row[2], 0) + n

    # Calculate total number of votes
    total_votes = sum(cand_d.values())
    # Find winner --> candidate with max votes
    # k[1] is dictionary value, that is equal to count of votes
    winner, _ = max(cand_d.items(), key = lambda k: k[1])

    # === Display and export to text file election results ===
    # Set string variable for a line
    line = f"-------------------------\n"

    # Initialize variable for keeping votes results for all candidates
    out = ""
    # Calculate percent of votes for each candidate and place
    # votes results for all candidates in string variable "out"
    for name in cand_d.keys():
        percent_votes = (cand_d[name] / total_votes) * 100
        out = out + f"{name}: {percent_votes:.3f}% ({cand_d[name]})\n"

    # Prepare output with election results
    output = (f"\nElection Results\n" \
        + line +
        f"Total Votes: {total_votes}\n" 
        + line
        + out 
        + line +
        f"Winner: {winner}\n"
        + line
            )

    # Display election results
    print (output)

    # Export election results to text file
    results = os.path.join('election_results.txt')
    with open(results, 'w') as f:
        print(output, file=f)


