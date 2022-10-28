# FOOTBALL POOL CONSOLE

This takes an Excel type file with columns (name | game1...game15 | points) and uses pandas to turn the information into a CSV. Then it loads all rows and columns into memory and checks against an API for final scores ranking how many teams were picked correctly to win. It then prints this to the console. I may route it to a results.txt file as well.

## How to use
'''
python xlsx_to_csv.py spreadsheet_name.xlsx week_number
'''

week_number will turn into a csv file in your root directory but I may remove this when testing is done.

## Why
The football pool I am in consists of a large amount of people and I get tired of counting row by row and the group admin I am sure hates counting up everyones scores.

## Caution
This is still in testing and was done in 1 night. Only a very specific dataset was accounted for and this may only work with a specific file Excel file type. I will improve in areas I can but this was never meant to be used for any other data but mine. The code is also terrible and I plan on going through and optimizing both speed and readability.

I am leaving debugging print statements in the code for now.

### Todo
- Organize everything within a main function

- Add functionality for ties for first place where whoever guesses closest to the total number of points scored for the last game of the week will win the pool. 

- clean and optimize code
