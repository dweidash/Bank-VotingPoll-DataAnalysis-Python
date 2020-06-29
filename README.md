# Bank and Poll Data - Python Analysis and Evaluation

## Background

Both projects, Bank and Poll, involves using Python script in the scenario that our company is requesting data to be read and analysis to be drawn in an outputted text file for ease of access.

For the Bank project, the script is designed to calculate, notate, and export the following:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The average of the changes in "Profit/Losses" over the entire period
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in losses (date and amount) over the entire period

Meanwhile, for the Poll project, the script is tasked on a dataset containing vote results for their elections. The script is required to analyze the votes and calculate the following:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote



### Instructions

1. Download the repository from https://github.com/dweidash/Bank-VotingPoll-DataAnalysis-Python/tree/master/project-python-bankdata
2. For either project, run main.py

### Output and Explanations

Output for the Bank project:

```
Financial Analysis
----------------------------

Total Months: 86
Total: $38382578
Average Change: $-2315.1176470588234
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
```

Output for the Poll project:

```
Election Analysis
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
```

To satisfy the goal, exporting the findings in a text file would be the best option given that the requested information is in a raw format and can be easily be presented in a website or other media per request from upstairs.

However, that doesn't mean that we need to be savages and present the data in a meaningless slog. A basic data has been added with multiple dashes to block out portions of the information.

No commas have been added for the numbers to avoid formatting shenanigans.