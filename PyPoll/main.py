import os 
import csv

csvpath = os.path.join("Resources/election_data.csv")

total_votes = 0
candidates = []
candidate_number = {}
winning_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_number[candidate] = 1
        else:
            candidate_number[candidate] += 1

    candidate_percent = {candidate: (candidate_number[candidate] / total_votes) for candidate in candidates}

    for name in candidate_percent.items():
        if name[1] > winning_votes:
            winning_votes = name[1]
            winner = name[0]

    candidate_percent['Khan'] = "{:.3%}".format(candidate_percent['Khan'])
    candidate_percent['Correy'] = "{:.3%}".format(candidate_percent['Correy'])
    candidate_percent['Li'] = "{:.3%}".format(candidate_percent['Li'])
    candidate_percent['O\'Tooley'] = "{:.3%}".format(candidate_percent['O\'Tooley'])

    print(f'```text')
    print(f'Election Results')
    print(f'----------------------------')
    print(f'Total Votes: {total_votes}')
    print(f'----------------------------')
    print(f'{candidates[0]}: {candidate_percent["Khan"]} ({candidate_number["Khan"]})')
    print(f'{candidates[1]}: {candidate_percent["Correy"]} ({candidate_number["Correy"]})')
    print(f'{candidates[2]}: {candidate_percent["Li"]} ({candidate_number["Li"]})')
    print(candidates[3] + ": " + str(candidate_percent['O\'Tooley']) + " " + "(" + str(candidate_number['O\'Tooley']) + ")")
    print(f'----------------------------')
    print(f'Winner: {winner}')
    print(f'----------------------------')
    print(f'```')

    output_path = os.path.join("analysis/Analysis.txt")

    with open(output_path, 'w') as txt:
        
        txt.write(f'```text \n')
        txt.write(f'Election Results \n')
        txt.write(f'---------------------------- \n')
        txt.write(f'Total Votes: {total_votes} \n')
        txt.write(f'---------------------------- \n')
        txt.write(f'{candidates[0]}: {candidate_percent["Khan"]} ({candidate_number["Khan"]}) \n')
        txt.write(f'{candidates[1]}: {candidate_percent["Correy"]} ({candidate_number["Correy"]}) \n')
        txt.write(f'{candidates[2]}: {candidate_percent["Li"]} ({candidate_number["Li"]}) \n')
        txt.write(candidates[3] + ": " + str(candidate_percent['O\'Tooley']) + " " + "(" + str(candidate_number['O\'Tooley']) + ") \n")
        txt.write(f'---------------------------- \n')
        txt.write(f'Winner: {winner} \n')
        txt.write(f'---------------------------- \n')
        txt.write(f'``` \n')

