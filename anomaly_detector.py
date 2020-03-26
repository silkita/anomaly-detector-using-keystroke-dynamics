import pandas
from scipy.spatial.distance import euclidean, cityblock

keystroke = "DSL_strong_password_data.csv"
dataset = pandas.read_csv(keystroke)
subjects = dataset["subject"].unique()
print(subjects)

train_drop_index = []
test_drop_index = []
#for subject in subjects:
#    temp_data = dataset.loc[dataset.subject == subject,"H.period":"H.Return"]
    
#    print(temp_data)

temp_data = dataset.loc[:,"H.period":"H.Return"]

i=0
for sub in subjects:
    for j in range(10,400):
        train_drop_index.append(400*i+j)
    for k in range(0,400):
        if k!=10:
            test_drop_index.append(400*i+k)
    i+=1
   

train_set = temp_data.drop(temp_data.index[train_drop_index])
test_set = temp_data.drop(temp_data.index[test_drop_index])
print("Total Train Data: ",train_set.shape[0])
print("Total Test Data: ",test_set.shape[0])

mean_vector = train_set.mean().values
std_deviation_vector = train_set.std().values
print("Mean Vector: ",mean_vector)
print("Standard Deviation Vector: ",std_deviation_vector)


#training starts here
indices = []
for i in range(train_set.shape[0]):
    distance = euclidean(train_set.iloc[i].values,mean_vector)
    if (distance > 3*std_deviation_vector).all()==True:
         indices.append(i)
    #print(distance)
train_set = train_set.drop(train_set.index[indices])
trained_model = train_set.mean().values
print("Trained Model")
print(trained_model)


# testing starts here
for i in range(test_set.shape[0]):
        manhattan_dist = 1-(cityblock(test_set.iloc[i].values,trained_model))/test_set.iloc[i].shape[0]
        if manhattan_dist > 0.85:
            result = "Match"
        elif manhattan_dist == 1:
            result = "Perfect Match"
        elif manhattan_dist == 0:
            result = "No match"
        else:
            result = "Poor Match"
        print("Test Score for user ",str(i)+":",manhattan_dist," Result: ",result)





