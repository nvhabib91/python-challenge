#dependecies
import csv, os

#file path
pypoll_path = os.path.join("election_data.csv")

#variables
runners = []
votes = {}
winner_name = ""
winning_vote_count = 0

#read csv and definitions
with open(pypoll_path) as pypoll:
    csv_reader = csv.reader(pypoll, delimeter = ",")

#read headers
    csv_header = next(csv_reader)
    
    for row in csv_reader:

        print(". ", end = "")

# add up vote count
        vote_total = vote_total + 1

#get runner names
        runner_name = row[2]

# runner vote count
if runner_name not in runners:
    runners.append(runner_name)
    votes[runner_name] = 0
votes[runner_name] = votes[runner_name] + 1


#generate the summary into text:

#output the summary to txt

