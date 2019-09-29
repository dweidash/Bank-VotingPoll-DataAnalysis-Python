#Set-Up: Import csv library.
import csv

#Set-Up: Set variable csvpath to the pathway to our csv file containing our data.
csvpath = "C:\\Users\\DeWitt Tsai\\Desktop\\USC Bootcamp\\DT Week 3 - Homework\\python-challenge\\resources\\election_data.csv"

#Set-Up: Create a blank dictionary
voteIndex = {}

#Set-Up: Create variables (Maybe... i can define these as custom functions once I get more comfortable with Python?)
totalVotes = 0

#Time to get started - Let's open the previously set up 'csvpath' csv pathway ainto a variable to use in our script as 'csvfile'.
with open(csvpath,newline='') as csvfile:

    #and then use csvfile to create csvreader.
    csvreader = csv.reader(csvfile,delimiter=',')
    
    #skip the header, and don't forget it! (Spongebob Reference)
    next(csvreader)

    # We COULD create an interation with a if-else logic that creates a list... but i want to create a dictionary instead.
    #I want to be able to reference to the dictionary with the candidate's name and count upwards each time their name is seen in the candidate row.
    #The plan is to get a count of votes for each candidate. We will need a total vote count to help generate our summary information.
    #We can either sum all the counts or we could possibly weave in a counter.

    # Make an iteration through the csv file.
    for row in csvreader:
        
        #Let's take care of the total vote counter while we're here. This will count up from 0 after each row. This is playing on the assumption that there are no duplicate rows...
        #Random thoughts for the future - Maybe there is a library that can help as a data checker to "authenticate" that a voter ID's first vote will be counted and their second vote will be ignored?
        totalVotes += 1

        #Now, let's get cracking to make our dictionary with an if-else statement. This will start off to check if the candidate (on column 3 of the current row) is in our dictionary.
        #It will first check to see if we haven't already made a "page" in our dictionary for him/her and create their page with a starting value of 1.
        if row[2] not in voteIndex.keys():

            #This is due to the logic where "If we encounter them for the first time, and create a page, we technically experienced their first vote!"
            #Remember, if we note a 'page' in our dictionary without the name or a value, it will add it in for us!
            #here, we're using row[2] since it will copy the string from the csv file as the index value.
            #the :1 will assign that index value to a integer of 1.
            voteIndex.update({row[2]:1}) 

        #Then, we'll use an else statement where the candidate's name is indeed in our dictionary.
        else:
            # If this condition is met, then the following script will use row[2] to refer to our current row's candidate string value to our dictionary and increase their counter value by +1.
            voteIndex[row[2]] += 1


#Now, we have created a complete dictionary. Each candidate has their own vote count.


#The first challenge is how we can do the following:
# 1. How can we calculate the percentage of a candidate's votes without noting each candidate by name?
# 2. How can we print/export a script that is FLEXIBLE and AUTOMATED without any knowledge of the data set?
# Elaboration: Let's say there are 6 candidates instead and we had no idea!

#Let's create a list of candidate names by referencing our dictionary.
#k is simply a variable, but the trick is, when we write like this, it will create a list based on the 'page' titles AKA the candidate's names and will not contain their vote counts.
listCandidate = [ k for k in voteIndex ]
 
#Let's create a list of the candidate votes by referencing our dictionary.
#this time, using .values() will spit out the candidate's votes one by one.
listVotes = [v for v in voteIndex.values()]

#The reason why this works is that, while there isn't a specified index # for each candidate, they're sorted in the same order.
#For example, if the candidates are listed, by default, as Jon, Rick, and Casper, their votes will match the order of their names as well! Convenient!
#Now, we're going to create an interation. While we could probably refer to our dictionary, I want to do this in a clean and easy-to-follow way.

#We're going to use len() to count how many candidates there are in our dictionary and save it as 'listCountdown' int variable to use into our iteration.
listCountdown = len(voteIndex)#ticker down counter

#We'll then create a new list, using our same naming convention as our previous lists, for our percentages that we'll be calculating per candidate(s).
listPercentages = []#defining the empty list for percentages



#Z is a variable to countdown between the values of 0 to the length of our index.
for z in range(0,listCountdown):
    
    #Step 1: Calculate the percentage value by referencing the first count that we're on, at this moment of the iteration.
    percBase = (listVotes[z]/totalVotes*100)
    
    #Step 2: Format the value to 3 decimal places
    percForm = format(percBase,'.3f')
    
    #Step 3: Insert new value into the list as a string including the '%' symbol
    #SPECIAL_NOTE: By the way, we can get away with this since this value is going to be printed/exported out as is. If we were going to do more math, we'd do without the percentage sign and keep as an int.
    listPercentages.append(percForm+'%')


#NOW we have another challenge... how can we determine the winner by looking at these percentages or by the votes?
#The simplest and obvious way is using the votes per candidate to determine the winner.

#So.... let's use another iteration!

#Define these variables as ints at 0. We'll be using both of these variables to keep track of who has the highest vote count.
winVotes = 0 #Test will be used to fuel the if statement.
winPosition = 0 #Tag will be used to keep track of which # in the list the highest value is located at.

#Once again, we'll iterate using the help of listCountdown.
for z in range(0,listCountdown):
    
    #The logic here is basically saying, "Let's do some specified actions if the current value held in variable winVotes is less than the vote list's current count of votes."
    if  winVotes < listVotes[z]:
        
        #Basically, winVotes is indeed smaller, and therefore we found a new contender for highest voted, we'll then save the vote count of the candidate to winVotes to use for later.
        winVotes = listVotes[z]
        
        #We'll then also notate the integer of the countdown each time we have a higher value. Keeping this value, we'll be able to refer to our previously set up lists to pinpoint the proper candidate...
        # ...to notate as the winner.
        winPosition = z



#PRINT SECTION

#First, lets print out the first section that does not require any iterations.
print(
    f'\nElection Analysis\n'
    f'-------------------------\n'
    f'Total Votes: {totalVotes}\n'
    f'-------------------------')

#Second, let's make an iteration that goes from 0 to 3 (thanks to listCountdown) and print out the results per candidate.
for y in range(0,listCountdown):
    
    print(f"{listCandidate[y]}: {listPercentages[y]} ({listVotes[y]})")

#Lastly, lets print out the grand winner. No iteration required means that this part is very simple.
print(
    f'-------------------------\n'
    f'Winner: {listCandidate[winPosition]}\n'
    f'-------------------------')

#EXPORT SECTION
#Let's export a text file that is named ElectionAnalysis.txt and open it into write mode.

#First part is to set the path to the file to a specific variable
exportPath = "C:\\Users\\DeWitt Tsai\\Desktop\\USC Bootcamp\\DT Week 3 - Homework\\python-challenge\\PyPoll\\election_analysis.txt"

#Second part is to then open the path, which will create a new txt file if one doesn't exist already in my folder.
with open(exportPath, 'w', newline='') as text:

    #Let's then write into the text file the first section...
    text.writelines(
        f'\nElection Analysis\n'
        f'-------------------------\n'
        f'Total Votes: {totalVotes}\n'
        f'-------------------------\n')

    #And then continue to write (using the same format as the PRINT section but using .write instead) the data results.
    for y in range(0,listCountdown):
        
        #Basically, this will iterate as y goes from 0 to 3 and will spit out a report one by one.
        text.writelines(f"{listCandidate[y]}: {listPercentages[y]} ({listVotes[y]})\n")

    #Finally, it will write the last bit to notate who is the winner.
    text.writelines(
        f'-------------------------\n'
        f'Winner: {listCandidate[winPosition]}\n'
        f'-------------------------')