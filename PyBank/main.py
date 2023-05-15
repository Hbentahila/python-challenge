# Importing OS and CSV modules 
import os
import csv

# Command prompt should be opened in Folder PyBank
budget_csv= os.path.join("..", "Resources", "budget_data.csv")
print(budget_csv)

# Creating lists to store data
date= []
profit_loss= []
change_profit_loss= []

# Opening the csv file budget_data.csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    # Reading the header row first
    csv_header = next(csvreader)
    
    # Looping through our csv file and adding:
    # The dates and the profit/loss amounts to their respective lists
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(int(row[1]))
    
    # Calculating the total number of months and 
    # The net total amount of "Profit/Losses" over the entire period
    total_months= len(date)
    total_profit_loss= sum(profit_loss)

    # Looping through the profil_loss newly created list and 
    # Calculating the changes in "Profit/Losses" over the entire period
    # Amounts are added to the list change_profit_loss
    for i in range(1, len(profit_loss)):
        change_profit_loss.append(int(profit_loss[i]-profit_loss[i-1]))

    # Calculating the average of the changes and
    # The greatest increase in profits and
    # The greatest decrease in profits
    average_change= round(sum(change_profit_loss) / len(change_profit_loss), 2)
    greatest_increase= max(change_profit_loss)
    greatest_decrease= min(change_profit_loss)

    # Finding the dates of the greatest increase/decrease in profits
    greatest_increase_date= date[(change_profit_loss.index(greatest_increase))+1]
    greatest_decrease_date= date[(change_profit_loss.index(greatest_decrease))+1]

    # Results / Output
    output= f"""Financial Analysis\n\n---------------------------------
    \nTotal Months: {total_months}
    \nTotal: ${total_profit_loss}
    \nAverage Change: ${average_change}
    \nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
    \nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
    """
    
    # Printing the ouput/analysis to the Terminal
    print(output)

# Exporting a text file with the results
analysis_output= "../Analysis/financial_analysis.txt"
writer= open(analysis_output, "w") 
writer.write(output)