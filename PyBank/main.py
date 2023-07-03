# Code for PyBank
import os
import csv

# Initialize variables
budget_date_list = []
budget_pl_list = []
budget_change_list = []

# Set variables to the file location of the csv file
filename = "budget_data.csv"
folderpath = os.path.join ("Resources")
filepath = os.path.join (folderpath,filename)


# Open and read budget data from csv file
with open (filepath) as budgetdatacsv:
    budgetdata = csv.reader(budgetdatacsv)
    # Reading the header. This helps to iterate starting from the datarows instead of header row
    budgetheader = next(budgetdata)

    # Store the data from csv file in 2 lists - one for each column in the csv file
    for b_date,b_pl in budgetdata:
        budget_date_list.append(b_date)
        budget_pl_list.append(int(b_pl))

    # Total number of months
    total_months = len(budget_date_list)
    
    # Net Total Amount
    net_amount = sum(budget_pl_list)
    
    # Calculate and store change between consecutive entries of profit/loss list in a new list (budget_change_list)
    for counter in range(total_months):
        if counter != 0:
            change = budget_pl_list[counter] - budget_pl_list[counter-1]
            budget_change_list.append(change)

    # Calculate average of change in Profit/Loss
    average_change = sum(budget_change_list)/ len(budget_change_list)

    # Get greatest increase and decrease in Profit
    g_increase = max(budget_change_list)
    g_decrease = min(budget_change_list)

    # Get corresponding date for the greatest increase and decrease in Profit
    g_increase_date = budget_date_list[budget_change_list.index(g_increase)+1]
    g_decrease_date = budget_date_list[budget_change_list.index(g_decrease)+1]

    # Print the results
    print ("Financial Analysis")
    print ("-----------------------------------")
    print (f"Total Months: {total_months}")
    print (f"Total: ${net_amount}")
    print (f"Average Change: ${average_change:.2f}")
    print (f"Greatest Increase in Profits: {g_increase_date} (${g_increase})")
    print (f"Greatest Decrease in Profits: {g_decrease_date} (${g_decrease})")
        
# Create a text file to write the results
output_filename = "financial_results.txt"
output_folderpath = os.path.join("analysis")
output_filepath = os.path.join (output_folderpath,output_filename)
    
# Write the results to text file
with open (output_filepath,"w") as output_file:
    output_file.write ("Financial Analysis\n")
    output_file.write ("-----------------------------------\n")
    output_file.write (f"Total Months: {total_months}\n")
    output_file.write (f"Total: ${net_amount}\n")
    output_file.write (f"Average Change: ${average_change:.2f}\n")
    output_file.write (f"Greatest Increase in Profits: {g_increase_date} (${g_increase})\n")
    output_file.write (f"Greatest Decrease in Profits: {g_decrease_date} (${g_decrease})\n")

