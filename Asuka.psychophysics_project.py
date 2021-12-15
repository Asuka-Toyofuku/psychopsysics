import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from statistics import mean
from scipy.stats import norm
from scipy.stats import ttest_ind
#from scikit_learn.linear_model import LinearRegression
#from statsmodels.stats.anova import AnovaRM

dataPath = "data_group_final/"
csvFiles = [dataPath + file for file in listdir(dataPath) if ".csv" in file]


meanRTs = pd.DataFrame({"participant" : [], "condition" : [], "response" : [],
                    "mean RT" : []})

counter = 0
for dataFile in csvFiles:
    #New ID for each participant
    counter += 1
    pNum = "P-" + str(counter)
    rawData = pd.read_csv(dataFile)
    

    expData2 = pd.DataFrame(rawData, columns = ["participant", "condition", "word",
                            "response", "key_response.rt", "key_response.keys"])

    expData2 = expData2.rename(columns = {"key_response.rt" : "RT", "key_response.keys" : "actual_response"})

    #only include trials with a response
    expData2 = expData2.drop(labels=range(0,15), axis=0)
    expData2 = expData2[expData2.RT.notnull()]
  

    if counter ==1:
        expData = expData2
    else:
        expData = expData.append(expData2)
    #axis = 0 indicate rows
    #axis = 1 indicate columns

    #only include trials with correct test responses for RT analysis
   
    posiRT_Data = expData[(expData.condition == "positive")]
    neutRT_Data = expData[(expData.condition == "neutral")]
    negaRT_Data= expData[(expData.condition == "negative")]

    #print(rtData.to_string())

#     #data frame for RTs for each condition
    positiveRTs = expData[(expData.condition == "positive") & (expData.actual_response == "p")] #only correct attributions
    neutralRTs = expData[(expData.condition == "neutral") & (expData.actual_response == "q")]
    negativeRTs = expData[(expData.condition == "negative") & (expData.actual_response == "n")]

    #lists for RTs for each condition
   

    # #loop over data
    # for index, row in rtData.iterrows():
    #     #filter data: correct response and non-empty RT

    #     if row["condition"] == "positive" and row["response"] == "p":
    #         positiveRTs.append(row["RT"])
    #     elif row["condition"] == "neutral" and row["response"] == "q":
    #         neutralRTs.append(row["RT"])
    #     elif row["condition"] == "negative" and row["response"] == "n":
    #         negativeRTs.append(row["RT"])


    #new data to add to meanRTs
    pNumList = [pNum, pNum, pNum]
    conditionList = ["positive", "neutral", "negative"]
    #responseList = ["p", "q", "n"]

    meanRTsList = [mean(positiveRTs.RT), mean(neutralRTs.RT), mean(negativeRTs.RT)]

    #new data --> data frame
    newLines = pd.DataFrame({"participant" : pNumList, "condition" : conditionList,
                              "mean RT" : meanRTsList})

    #append newLines to meanRTs
    #(note: unlike appending a list, this doesn't change the initial data frame)
    meanRTs = meanRTs.append(newLines, ignore_index=True) #don't want index duplicates

#print(meanRTs)

#group means
positiveMeans = meanRTs[(meanRTs.condition == "positive")]["mean RT"]
neutralMeans = meanRTs[(meanRTs.condition == "neutral")]["mean RT"]
negativeMeans = meanRTs[(meanRTs.condition == "negative")]["mean RT"]


print("positive mean RT:", mean(positiveMeans))
print("neutral mean RT:", mean(neutralMeans))
print("negative mean RT:", mean(negativeMeans))



# plt.hist(expData.RT, bins = 20)
# plt.ylabel("Frequency")
# plt.xlabel("RT (s)")
# plt.title("Distribution of Reaction Time for three-choice selection task")
# plt.show()

# plt.scatter(range(1,len(expData.RT) + 1), expData.RT)
# plt.ylabel("RT (s)")
# plt.xlabel("Trial Number")
# plt.title("Reaction Time Sequence")
# plt.show()


# fig, ax = plt.subplots()
# bars = ax.bar([1, 2.5, 4], [mean(positiveMeans), mean(neutralMeans), mean(negativeMeans)])
# ax.set_ylabel('RT (s)')
# ax.set_title('Mean Reaction Time by diffrent category of words')
# ax.set_xticks([1, 2.5, 4])
# ax.set_xticklabels(["Positive words", "Neutral words", "Negative words"])
# plt.show()



# #vizualizing with a boxplot
# fig, ax = plt.subplots()
# box = ax.boxplot([positiveMeans, neutralMeans, negativeMeans])
# ax.set_ylabel("RT (s)")
# ax.set_title('Reaction Time by diffrent category of words') 
# ax.set_xticklabels(["positive:p", "neutral:q", "negative:n"])
# plt.show()

# fig, ax = plt.subplots()
# violin = ax.violinplot(dataset = [positiveMeans, neutralMeans, negativeMeans], positions = [1,2,3], showmeans=True, showextrema=True, showmedians=False)
# ax.set_ylabel('RT (s)')
# ax.set_title('Reaction Time by diffrent category of words') 
# ax.set_xticks([1,2,3])
# ax.set_xticklabels(["Positive words", "Neutral words", "Negative words"])
# plt.show()

print(ttest_ind(positiveRTs.RT, neutralRTs.RT))
print(ttest_ind(neutralRTs.RT, negativeRTs.RT))

#これは無理そうw
#repeated measures anova
#model = AnovaRM(data = meanRTs, depvar = "mean RT", subject = "participant", within = ["condition", "response"]).fit()
#print(model)

#SDT
#d' function
def dPrime(hitRate, FArate):
    stat = norm.ppf(hitRate) - norm.ppf(FArate)

    return stat

#criterion function
def criterion(hitRate, FArate):
    stat = -.5*(norm.ppf(hitRate) + norm.ppf(FArate))

    return stat


##Ways to view and select data in the data frame
#print(rawData) #truncated
#print(rawData.to_string()) #every entry

#print(rawData.columns) #column labels

#select a specific column
# print(rawData["Trial"])
print(rawData.Trial)

#select a specific entry
print(rawData.loc[0,"Trial"])

#select a range of entries
print(rawData.loc[0:4,"condition":"color"])

#select rows that meet certain conditions
#print(rawData[rawData.condition == "positive"])
#print(rawData[(rawData.condition == "positive") & (rawData.key_response.keys == "p")]) #and
# print(rawData[(rawData.condition == "positive") | (rawData.key_response.keys == "p")]) #or

#make a new data frame only with the data we need
expData3 = pd.DataFrame(expData, columns = ["condition", "response", "actual_response", "RT"])

#rename to make things easier
expData3 = expData3.rename(columns = {"response" : "correct_response"})

##calculate hit, false alarm, correct rejection, and miss rates (for each condition)

#the data frame we'll be using
accuracy = pd.DataFrame({"hits" : [0], "misses" : [0], "CRs" : [0], "FAs" : [0]})

#updating the data frame for each entry
for index, row in expData3.iterrows():
    #condition: positive
    if row["condition"] == "positive":
        rowInd = 0
        #Hit
        if row["actual_response"] == "p":
            accuracy.loc[rowInd,"hits"] += 1
        #Miss
        elif row["actual_response"] != "p":
            accuracy.loc[rowInd,"misses"] += 1

    #condition: not positive
    elif row["condition"] == "neutral" or "negative":
        rowInd = 0
        if row["actual_response"] == "p":
            accuracy.loc[rowInd,"FAs"] += 1
        #Miss
        elif row["actual_response"] != "p":
            accuracy.loc[rowInd,"CRs"] += 1

    #condition: negative
    
print(accuracy)

print(accuracy.loc[0,"hits"])

accuracy_nega = pd.DataFrame({"hits" : [0], "misses" : [0], "CRs" : [0], "FAs" : [0]})

#updating the data frame for each entry
for index, row in expData3.iterrows():
    #condition: negative
    if row["condition"] == "negative":
        rowInd = 0
        #Hit
        if row["actual_response"] == "n":
            accuracy_nega.loc[rowInd,"hits"] += 1
        #Miss
        elif row["actual_response"] != "n":
            accuracy_nega.loc[rowInd,"misses"] += 1

    #condition: not negative
    elif row["condition"] == "neutral" or "negative":
        rowInd = 0
        if row["actual_response"] == "p":
            accuracy_nega.loc[rowInd,"FAs"] += 1
        #Miss
        elif row["actual_response"] != "p":
            accuracy_nega.loc[rowInd,"CRs"] += 1

    
print(accuracy_nega)



#Calculate rates from response counts
hitRateLow = accuracy.loc[0,"hits"]/15
FArateLow = accuracy.loc[0,"FAs"]/15

hitRateHigh = accuracy.loc[0,"hits"]/15 #positive
#FArateHigh = accuracy.loc[1,"FAs"]/15
FArateHigh = (accuracy.loc[0,"FAs"]+1)/15 #negative

#Cacluate d' and criterion
print("d' (low):", dPrime(hitRateLow, FArateLow))
print("criterion (low):", criterion(hitRateLow, FArateLow))

print("d' (high):", dPrime(hitRateHigh, FArateHigh))
print("criterion (high):", criterion(hitRateHigh, FArateHigh))
