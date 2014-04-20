THE ASSIGNMENT:

The data is contained in the file 'master1.txt'. The columns contain the following information:

1. Storm ID
2. Storm Name
3. Latitude
4. Longitude
5. Wind Speed
6. Central Pressure
7. Year
8. Running Date in Hours
9. Descriptor

The assignment was to write a program that would determine the following:

1. The frequency of hurricane events (exluding systems that remain as tropical storms) 
i.e. find the number of hurricanes per decade.

2. The minimum value of central pressure in each of these hurricanes

Additionally, the program must extract and format the data such that it can be pasted into
the following Google Code Playground API:

https://code.google.com/apis/ajax/playground/?type=visualization#column_chart

The X-axis would be the decade starting in 1920 and ending in 2010. The y-axis would be
binned categories of central pressure with a bin width of 10 units (millibars). The bar 
heights would be the number of storms in each bin. i.e. if storm 523 had a minimum central
pressure of 952 mBar and occured in 1921, it would add one count to the 950-959 bin in the 
1920s decade. 

MY APPROACH:

I got the data into a cvs file by opening the text file in Excel with fixed-width delimitation.

My program works by selectively reading data from the cvs. I used if statements to only
get data from the rows where the descriptor contained the word "hurricane" and where
row 6 had a number not equal to 0. Zeros indicate no measurement was taken. I got the syntax
for the cvs reader from Daniel Mulkey. 

The 'frequency_counter' function uses the above critera and iterates between the two years
with which the function gets called. It then counts the number of unique storm IDs read into
the program. 

The 'minimum_finder' function computes the minimum central pressure for any storm. The function
is called for a storm ID. I then called the function repeatedly using a for loop to get the
minimum central pressure for every hurricane. 

The 'plot_list_maker' function is built from 'minimum_finder'. It initializes fifteen
empty lists (one for each bin) and populates the bin lists with unique storm IDs. The function 
gets called with a starting year and ending year. The output is a list containing the lengths 
of each bin list. Calling the function for each decade prints the lists which can then be 
copied into the Google Code Playground API. I added the commas manually. 
