'''
histogram_age_income.py 
reads data from the age_income_feb14.csv
and creates two histograms: the age distribution and the income 
distribution. The data are from U.S. Census Bureau's February 2014 
Current Population Survey. 

(c) 2014 Project Lead The Way
'''
import matplotlib.pyplot as plt
import numpy as np
import os.path

# A generic helper function for matplotlib.pyplot graphics
def make_PLTW_style(axes):
    for item in ([axes.title, axes.xaxis.label, axes.yaxis.label] +
             axes.get_xticklabels() + axes.get_yticklabels()):
        item.set_family('Georgia')
        item.set_fontsize(16)

# Build an absolute filename from directory + filename
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'obesity.csv')
datafile = open(filename,'r')
data = datafile.readlines()

#Initialize aggregators
obesity=[]
ped=[]
for line in data[1:]: # Omit 0, 1, 2 because _______
    obese, pe, state = line.split(',')
    obesity.append(obese)
    ped.append(pe)
datafile.close()

#Make display
fig_age, ax = plt.subplots(1, 1)
ax.scatter(ped,obesity, c="red")
ax.set_title('Percentage Obesity vs. Percentage participating in P.E ')
ax.set_xlabel('Percent Participation in P.E')
ax.set_ylabel('Percent Overweight/Obese')
make_PLTW_style(ax)

fig_age.show()
'''
The data consists of household sizes in the states. Transformations done include reordering the sets of data into states and sizes.
Once they were separated the size data was consolidated into the histogram. while state data was ignored due to it not being relevant 
to the topic of household size. Then the x and y axis were edited to correspond with the data. The visualizations produced involved
editing the code in the histogram code to involve both household size and number of households.
'''