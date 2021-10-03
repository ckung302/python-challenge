import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

total_profit = 0
previous_profit = None
total_months = 0
current_change = 0
total_changes = 0
greatest_increase = 0
greatest_decrease = 0
increase_month = ""
decrease_month = ""


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_months += 1
        current_month = row[0]
        current_profit = int(row[1])

        total_profit = total_profit + current_profit
        
        if previous_profit is not None:
            current_change = current_profit - previous_profit
        
        total_changes = total_changes + current_change

        if current_change > greatest_increase:
            greatest_increase = current_change
            increase_month = current_month

        if current_change < greatest_decrease:
            greatest_decrease = current_change
            decrease_month = current_month

        previous_profit = current_profit
    
    avg_change = round(total_changes/(total_months - 1), 2)

    print('```text')
    print('Financial Analysis')
    print('------------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: {total_profit}')
    print(f'Average Change: {avg_change}')
    print(f"Greatest Increase in Profits: {increase_month} ({greatest_increase})")
    print(f'Greatest Decrease in Profits: {decrease_month} ({greatest_decrease})')
    print('```')

output_path = os.path.join("analysis/Analysis.txt")

with open(output_path, 'w') as txt:

    txt.write('```text \n')

    txt.write('Financial Analysis \n')

    txt.write('------------------------------ \n')

    txt.write(f'Total Months: {total_months} \n')

    txt.write(f'Total: {total_profit} \n')

    txt.write(f'Average Change: {avg_change} \n')

    txt.write(f"Greatest Increase in Profits: {increase_month} ({greatest_increase}) \n")
    
    txt.write(f'Greatest Decrease in Profits: {decrease_month} ({greatest_decrease}) \n')
    
    txt.write('```') 


