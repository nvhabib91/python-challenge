#dependecies
import csv, os

#file path
pybank_path = os.path.join("Resources", "budget_data.csv")

#variables
months = 0
next_month = []
net_change = []
max_increase = ["", 0]
max_decrease = ["", 99999999999999999999999999999999999999999999999]
net_total = 0

#read csv and definitions
with open(pybank_path) as pybank:
    csv_reader = csv.reader(pybank, delimeter = ",")

#read and remove the header from calc
    csv_header = next(csv_reader)
    
    row_one = next(csv_reader)
    months = months + 1
    net_total = net_total + int(row_one[1])
    prev_net_total = int(row_one[1])

    for row in csv_reader:
#find total
        months = months + 1
        net_total = net_total + int(row_one[1])

#find net delta
        net_change = int(row[1]) - prev_net_total
        prev_net_total = int(row[1])
        prev_net_change_list = prev_net_change_list + [net_change]
        change_month = change_month + [[row[0]]

#calc biggest dec
        if net_change > max_decrease[1]:
            max_decrease[0] = row[0]
            max_decrease[1] = net_change

#calc highest inc
        if net_change > max_increase[1]:
            max_increase[0] = row[0]
            max_increase[1] = net_change
             
#calc avg net change
net_avg_by_month = sum(prev_net_change_list) / len(prev_net_change_list)

#generate the summary into text:
output_summary = (
    print("Total Months: " + str(months))
    print("Total: $" + str(net_total))
    print("Average Change: " + str(avg_change))
    print("Greatest Increase in Profits: " + str(period) + str(max_increase))
    print("Greatest Decreas e in Profits: " + str(period) + str(max_decrease))
)

#output the summary to txt
text_output = os.path.join("budget_analysis.txt")
with open(text_output) as txt_file:
    txt_file.write(output_summary)
