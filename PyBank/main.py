#First let's import os and csv since we will be utilizing that for the banking exercise.
import csv

#Let's open the file located in /resources.
csvpath = "C:\\Users\\DeWitt Tsai\\Desktop\\USC Bootcamp\\DT Week 3 - Homework\\python-challenge\\resources\\budget_data.csv"

#Create variables
totalmonths = 0 #this variable will be used as a counter. It will increment by one each time our loop starts!
totalamount = 0 #this variable will be a sum-bucket to collectively add the value @ row[1] during each loop iteration.
incValue = 0 #this variable will be used to keep track of GREATEST positive change between two months.
decValue = 0 #this variable will be used to keep track of GREATEST negative change between two months.
deltaList = [] #this list will be used to keep track of the 'difference' between the months. Difference will be notated as 'delta'.
delta1 = 0 #this variable will be used to hold the previous month's profit value.
delta2 = 0 #this variable will be used to hold the current month's profit value.
deltaValue = 0 #this variable will be used to find the difference of 'delta2' and 'delta1'. Will be used to append the delta into deltaList

#Now, we need to create a loop that will go through the entire csv file and will do the following:

with open(csvpath,newline='') as csvfile: #first, open the file.

    csvreader = csv.reader(csvfile,delimiter=',') #second, create a variable to keep track of which row we're at.
    
    next(csvreader) #third, let's skip the first row which is the header of the data set.
    
    for row in csvreader: #finally, let's get started with a for loop that will iterate throughtout the entire csv file.

        # 1. Count how many months we have gone through
        totalmonths += 1
        
        # 2. Get the total sum of the dollar amount of all month values
        rowamt = int(row[1]) #let's first pull the current value at row[1] and store it into "rowamt" as an integer to avoid any possible weird syntax errors.
        totalamount += rowamt #let's put the current rowamt value into the totalamount sum-bucket.
        
        # 3. Run a loop so we can create a list of changes between all values in the csv file.
        if delta1 == 0: #first, let's create a line of code to set up the first delta1 value at the start of the csv file.
            delta1 = rowamt
        
        elif delta1 != 0: #second, let's create the main elif statement that will happen for the rest of the data set.
            delta2 = rowamt
            deltaValue = delta2 - delta1
            deltaList.append(deltaValue)
            delta1 = rowamt

        # 4. Keep track of the highest profit value and take note of its date.
        if incValue < deltaValue:
            incValue = deltaValue
            incDate = row[0]

        # 5. Keep track of the lowest profit value and take note of its date.
        elif decValue > deltaValue:
            decValue = deltaValue
            decDate = row[0]
        

#Now, its time to do some math with the list we've created with #3 from our 'with' iteration.
deltaSum = sum(deltaList)
deltaAvg = deltaSum/len(deltaList)

summary = (
    f'\nFinancial Analysis\n'
    f'----------------------------\n'
    f'Total Months: {totalmonths}\n'
    f'Total: ${totalamount}\n'
    f'Average Change: ${deltaAvg}\n'
    f'Greatest Increase in Profits: {incDate} (${incValue})\n'
    f'Greatest Decrease in Profits: {decDate} (${decValue})\n')

print(summary)

#Let's output a text file with our results.
vomitPath = "C:\\Users\\DeWitt Tsai\\Desktop\\USC Bootcamp\\DT Week 3 - Homework\\python-challenge\\Pybank\\financial_analysis.txt"
with open(vomitPath, 'w', newline='') as text:
    vomitBucket = (
    f'\nFinancial Analysis\n'
    f'----------------------------\n'
    f'Total Months: {totalmonths}\n'
    f'Total: ${totalamount}\n'
    f'Average Change: ${deltaAvg}\n'
    f'Greatest Increase in Profits: {incDate} (${incValue})\n'
    f'Greatest Decrease in Profits: {decDate} (${decValue})\n')

    text.writelines(vomitBucket)