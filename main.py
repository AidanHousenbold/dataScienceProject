#Aidan Housenbold November 16 2021

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv("HappinessData.csv").iloc[0:75, 1:12]

#test to make sure file is read in correctly
#print(df.shape)
#print(df)

#***************************Boxplot Code**************************************

#Gathering Data
freshman_happiness_score = df.loc[df["grade"] == "Freshman"].iloc[:, 1]
#print(freshman_happiness_score)
sophomore_happiness_score = df.loc[df["grade"] == "Sophomore"].iloc[:, 1]
#print(sophomore_happiness_score)
junior_happiness_score = df.loc[df["grade"] == "Junior"].iloc[:, 1]
#print(junior_happiness_score)
senior_happiness_score = df.loc[df["grade"] == "Senior"].iloc[:, 1]
#print(junior_happiness_score)

#***************************** Happiness Box Plot ***************************************************
fig1, ax1 = plt.subplots()
ax1.set_title("Happiness Scores")
ax1.boxplot([freshman_happiness_score, sophomore_happiness_score, junior_happiness_score,senior_happiness_score])
ax1.set_xticklabels(["Freshmen","Sophomores","Juniors","Seniors"])
#fig1.savefig('FinalFigure1.png', transparent=True, dpi=1200)
plt.show()

#**************************Pie Chart Code****************************************
happiness_characterized_dict= Counter(df["happiness_characterized"])
#print(happiness_characterized_dict)

plt.pie(happiness_characterized_dict.values(), labels=happiness_characterized_dict.keys(),
        autopct='%.1f%%')
plt.title("What Students Think are the Characterization of Happiness ")
#plt.savefig('piechart1.png', transparent=True, dpi=1200)
plt.show()

#******************Line graphs for comparison to happiness trend based on grade level************************************
#grades data
freshman_qgrades = round(df.loc[df["grade"] == "Freshman"].iloc[:, 8].mean(), 2)
sophomore_qgrades = round(df.loc[df["grade"] == "Sophomore"].iloc[:, 8].mean(), 2)
junior_qgrades = round(df.loc[df["grade"] == "Junior"].iloc[:, 8].mean(), 2)
senior_qgrades = round(df.loc[df["grade"] == "Senior"].iloc[:, 8].mean(), 2)

dict_qgrades = {"Freshmen": freshman_qgrades, "Sophomores": sophomore_qgrades,
                "Junior": junior_qgrades, "Senior": senior_qgrades}

print(dict_qgrades)

plt.xlabel("Grade Level")
plt.ylabel("Weight of Grades")
plt.title("Average for Each Grade Level in Response to Asking How Much Grades Effected Happiness")
plt.plot(dict_qgrades.keys(), dict_qgrades.values())
plt.savefig('QFigure1.png', transparent=True, dpi=1200)
plt.show()

#Popularity data
freshman_qpopularity = round(df.loc[df["grade"] == "Freshman"].iloc[:, 9].mean(), 2)
sophomore_qpopularity = round(df.loc[df["grade"] == "Sophomore"].iloc[:, 9].mean(), 2)
junior_qpopularity = round(df.loc[df["grade"] == "Junior"].iloc[:,9].mean(), 2)
senior_qpopularity = round(df.loc[df["grade"] == "Senior"].iloc[:, 9].mean(), 2)

dict_qpopularity = {"Freshmen": freshman_qpopularity, "Sophomores": sophomore_qpopularity,
                "Junior": junior_qpopularity, "Senior": senior_qpopularity}

print(dict_qpopularity)

plt.xlabel("Grade Level")
plt.ylabel("Weight of Popularity")
plt.title("Average for Each Grade Level in Response to Asking How Much Popularity Effected Happiness")
plt.plot(dict_qpopularity.keys(), dict_qpopularity.values())
#plt.savefig('QFigure2.png', transparent=True, dpi=1200)
plt.show()

#Body data
freshman_qbody = round(df.loc[df["grade"] == "Freshman"].iloc[:, 10].mean(), 2)
sophomore_qbody = round(df.loc[df["grade"] == "Sophomore"].iloc[:, 10].mean(), 2)
junior_qbody = round(df.loc[df["grade"] == "Junior"].iloc[:,10].mean(), 2)
senior_qbody = round(df.loc[df["grade"] == "Senior"].iloc[:, 10].mean(), 2)

dict_qbody = {"Freshmen": freshman_qbody, "Sophomores": sophomore_qbody,
                "Junior": junior_qbody, "Senior": senior_qbody}

print(dict_qbody)

plt.xlabel("Grade Level")
plt.ylabel("Weight of Body Image")
plt.title("Average for Each Grade Level in Response to Asking How Much Body Image Effected Happiness")
plt.plot(dict_qbody.keys(), dict_qbody.values())
#plt.savefig('QFigure3.png', transparent=True, dpi=1200)
plt.show()

#overall happiness score grades data
freshman_happiness = round(df.loc[df["grade"] == "Freshman"].iloc[:, 1].mean(), 2)
sophomore_happiness = round(df.loc[df["grade"] == "Sophomore"].iloc[:, 1].mean(), 2)
junior_happiness = round(df.loc[df["grade"] == "Junior"].iloc[:, 1].mean(), 2)
senior_happiness = round(df.loc[df["grade"] == "Senior"].iloc[:, 1].mean(), 2)

dict_happiness = {"Freshmen": freshman_happiness, "Sophomores": sophomore_happiness,
                "Junior": junior_happiness, "Senior": senior_happiness}

print(dict_happiness)

plt.xlabel("Grade Level")
plt.ylabel("Happiness Score")
plt.title("Average Happiness Score for Each Grade Level")
plt.plot(dict_happiness.keys(), dict_happiness.values())
#plt.savefig('QFigure4.png', transparent=True, dpi=1200)
plt.show()


