import csv

                                  
def frequency_counter(year1, year2):
"""
The following function determines the frequency of hurricanes between two
specified years. I will call it for each decade, as per the assignment.
"""           
    storm_id_freq = []
    with open("/Users/jacobmagers/Documents/Classes/Oregon/Spring 2014/Programming/HW 2/master1.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if ((str(row[8]) == "HURRICANE-1") or (str(row[8]) == "HURRICANE-2") or (str(row[8]) == "HURRICANE-3") or(str(row[8]) == "HURRICANE-4") or (str(row[8]) == "HURRICANE-5")) and ((float(row[6]) >= float(year1)) and (float(row[6]) <= float(year2))):
                storm_id_freq.append(float(row[0]))
                frequency = len(set(storm_id_freq))
    return frequency
    
print "The number of hurricanes between 1900 and 1909, 1910 and 1919, ... , 2000 and 2010 was:"
print frequency_counter(1900, 1909)
print frequency_counter(1910, 1919)
print frequency_counter(1920, 1929)
print frequency_counter(1930, 1939)
print frequency_counter(1940, 1949)
print frequency_counter(1950, 1959)
print frequency_counter(1960, 1969)
print frequency_counter(1970, 1979)
print frequency_counter(1980, 1989)
print frequency_counter(1990, 1999)
print frequency_counter(2000, 2010)

def minimum_finder(storm_id):
"""
The following function will get the minimum measured central pressure for any
hurricane, but not every hurricane. To get every hurricane, we need to make a 
loop that iterates over every storm id associated with a hurricane and a central
pressure measurement and calls this function, and then appends the output of the
function to a list. To present the data, we zip the two lists together and 
present them as tuples or something, i.e. [(stormID1, minPressure1),
(stormID2, minPressure2),...].
"""
    pressure_list = []
    minimum_pressure = 0
    with open("/Users/jacobmagers/Documents/Classes/Oregon/Spring 2014/Programming/HW 2/master1.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if ((str(row[8]) == "HURRICANE-1") or (str(row[8]) == "HURRICANE-2") or (str(row[8]) == "HURRICANE-3") or(str(row[8]) == "HURRICANE-4") or (str(row[8]) == "HURRICANE-5")) and (float(row[0]) == float(storm_id)) and (float(row[5])) != 0:
                pressure_list.append(row[5])
                minimum_pressure = min(pressure_list)
    return minimum_pressure

"""
This part of the code finds and prints the minimum central pressure for every
hurricane.
"""
storm_id_list = []
with open("/Users/jacobmagers/Documents/Classes/Oregon/Spring 2014/Programming/HW 2/master1.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if (float(row[5])) != 0:
                storm_id_list.append(int(row[0]))
storm_id_list = list(set(storm_id_list))

minimum_pressure_list = []
for i in storm_id_list:
    minimum_pressure_list.append(minimum_finder(i))
combined_minimum_plot = [storm_id_list, minimum_pressure_list]
transposed_combined_plot = [[row[i] for row in combined_minimum_plot] for i in range(len(minimum_pressure_list))]
print " "
print "The minimum central pressure for every hurricane is as follows (Storm ID, minimum Central Pressure in mBar):"
print transposed_combined_plot

labels = ["Decades", "880-889", "890-899", "900-909", "910-919", "920-929", "930-939", "940-949", "950-959", "960-969", "970-979", "980-989", "990-999", "1000-1009", "1010-1019", "1020-1029"]
def plot_list_maker(year1, year2):
"""
The following function is for the plotting part of the assignment. It produces
a list in the form of each row in the google code playground API. Calling the
function for each decade gives all the necessary lists. 
"""
    storm_id_list = []
    with open("/Users/jacobmagers/Documents/Classes/Oregon/Spring 2014/Programming/HW 2/master1.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if ((str(row[8]) == "HURRICANE-1") or (str(row[8]) == "HURRICANE-2") or (str(row[8]) == "HURRICANE-3") or(str(row[8]) == "HURRICANE-4") or (str(row[8]) == "HURRICANE-5")) and ((float(row[5])) != 0) and (int(row[6]) >= int(year1) and int(row[6]) <= int(year2)):
                    storm_id_list.append(int(row[0]))
    storm_id_list = list(set(storm_id_list))
    minimum_pressure_list = []
    for i in storm_id_list:
        minimum_pressure_list.append(int(minimum_finder(i)))    
    bin1 = []
    bin2 = []
    bin3 = []
    bin4 = []
    bin5 = []
    bin6 = []
    bin7 = []
    bin8 = []
    bin9 = []
    bin10 = []
    bin11 = []
    bin12 = []
    bin13 = []
    bin14 = []
    bin15 = []
    for i in minimum_pressure_list:
        if int(880) <= int(i) and int(889) >= int(i):
            bin1.append(i)
        elif int(890) <= int(i) and int(899) >= int(i):
            bin2.append(i)
        elif int(900) <= int(i) and int(909) >= int(i):
            bin3.append(i)
        elif int(910) <= int(i) and int(919) >= int(i):
            bin4.append(i)
        elif int(920) <= int(i) and int(929) >= int(i):
            bin5.append(i)
        elif int(930) <= int(i) and int(939) >= int(i):
            bin6.append(i)
        elif int(940) <= int(i) and int(949) >= int(i):
            bin7.append(i)
        elif int(950) <= int(i) and int(959) >= int(i):
            bin8.append(i)
        elif int(960) <= int(i) and int(969) >= int(i):
            bin9.append(i)
        elif int(970) <= int(i) and int(979) >= int(i):
            bin10.append(i)
        elif int(980) <= int(i) and int(989) >= int(i):
            bin11.append(i)
        elif int(990) <= int(i) and int(999) >= int(i):
            bin12.append(i)
        elif int(1000) <= int(i) and int(1009) >= int(i):
            bin13.append(i)
        elif int(1010) <= int(i) and int(1019) >= int(i):
            bin14.append(i)
        elif int(1020) <= int(i) and int(1029) >= int(i):
            bin15.append(i)
    bin1count = len(bin1)
    bin2count = len(bin2)
    bin3count = len(bin3)
    bin4count = len(bin4)
    bin5count = len(bin5)
    bin6count = len(bin6)
    bin7count = len(bin7)
    bin8count = len(bin8)
    bin9count = len(bin9)
    bin10count = len(bin10)
    bin11count = len(bin11)
    bin12count = len(bin12)
    bin13count = len(bin13)
    bin14count = len(bin14)
    bin15count = len(bin15)
    return [str(year1) + "s", bin1count, bin2count, bin3count, bin4count, bin5count, bin6count, bin7count, bin8count, bin9count, bin10count, bin11count, bin12count, bin13count, bin14count, bin15count] 

print " "
print "Paste this into the Google Code Plaground API:"
print labels
print plot_list_maker(1920,1929)
print plot_list_maker(1930,1939)
print plot_list_maker(1940,1949)
print plot_list_maker(1950,1959)
print plot_list_maker(1960,1969)
print plot_list_maker(1970,1979)
print plot_list_maker(1980,1989)
print plot_list_maker(1990,1999)
print plot_list_maker(2000,2010)