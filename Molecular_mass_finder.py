#Liam Nagle-Cocco
#23 June 2017

###
#Atomic Masses:
###

element_symbols = ['Ac','Ag','Al','Am','Ar','As','At',
'Au','B','Ba','Be','Bh','Bi','Bk','Br','C','Ca','Cd','Ce',
'Cf','Cl','Cm','Co','Cr','Cs','Cu','Db','Dy','Er','Es','Eu',
'F','Fe','Fm','Fr','Ga','Gd','Ge','H','He','Hf','Hg','Ho',
'Hs','I','In','Ir','K','Kr','La','Li','Lr','Lu','Md','Mg',
'Mn','Mo','Mt','N','Na','Nd','Ne','Nh','Ni','No','Np','O',
'Os','P','Pa','Pb','Pd','Pm','Po','Pr','Pt','Pu','Ra','Re',
'Rf','Rh','Rh','Rn','Ru','S','Sb','Sc','Se','Sg','Si','Sm',
'Sn','Sr','Ta','Tb','Tc','Te','Th','Ti','Tl','Tm','U','V',
'W','Xe','Y','Yb','Zn','Zr']

element_masses = [227.0,107.8682,26.981539,243.0,39.948,
74.92159,210.0,196.96654,10.811,137.327,9.012182,
262.0,208.98037,247.0,79.904,12.011,40.078,112.411,140.115,
251.0,35.4527,247.0,58.9332,51.9961,132.90543,63.546,262.0,
162.5,167.26,254.0,151.965,18.9984032,55.847,257.0,223,69.723,
157.25,72.61,1.00794,4.002602,178.49,200.59,164.93032,265.0,
126.90447,114.82,192.22,39.0983,83.8,138.9055,6.941,261.0,174.967,
258.0,24.305,54.93805,95.94,266.0,14.00674,22.989768,
144.24,20.1797,92.90638,58.69,259.0,237.05,15.9994,190.2,30.973762,
231.03588,207.2,106.42,145.0,209.0,140.90765,195.08,244.0,226.03,
186.207,261,102.9055,85.4678,222.0,101.07,32.066,121.75,44.95591,
78.96,263.0,28.0855,150.36,118.71,87.62,180.9479,158.92534,98.0,
127.6,232.0381,47.88,204.3833,168.93421,238.0289,50.9415,183.85,
131.29,88.90585,173.04,65.39,91.224]

###
#User interface:
###

print """
When entering your molecular formula, put a space between all symbols and numbers.
If there is just one of an atom, write 1.
Ensure you write with standard capitalisation, as element symbols are case-sensitive.
For example, water or H2O must be written as 'H 2 O 1', not 'H2O' or 'h 2 o 1'.
You can write decimal numbers, such as 'Fe0.6Ni2.404' which must be written as 'Fe 0.6 Ni 2.404'.
Enter your formula here:
"""
formula = raw_input(">>>")
entry_list = formula.split()

#This while loop checks that the list contains an even number of entries.
while ((-1)**(len(entry_list))) == (-1):
        print """
Your formula is not written correctly. Check that:
*   There are spaces between each chemical symbol and number.

*   You have included the number "1" where only one atom is present.

For example, water or H2O must be written as 'H 2 O 1', not 'H2O' or 'h 2 o 1'.
"""
        formula = raw_input(">>>")
        entry_list = formula.split()

###
#This is where the magic happens:
###

import numpy as np
number_of_elements=len(entry_list)/2
element_range = np.arange(0,number_of_elements,1)
element_range_2 = element_range * 2

element_list = []
number_list = []
for i in element_range_2:
    element_list.append(entry_list[i])
    number_list.append(entry_list[i+1])

full_element_range=np.arange(0,len(element_symbols),1)

molecular_mass = 0

for i in element_range:
    for j in full_element_range:
        if str(element_list[i])==str(element_symbols[j]):
            molecular_mass += float(element_masses[j]) * float(number_list[i])

###
#Print results:
###

print "Molecular mass is %d grams per mole." % molecular_mass
