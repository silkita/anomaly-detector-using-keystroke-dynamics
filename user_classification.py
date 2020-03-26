import pandas
from scipy.spatial.distance import euclidean, cityblock

keystroke = "DSL_strong_password_data.csv"
dataset = pandas.read_csv(keystroke)
subjects = dataset["subject"].unique()
print(subjects)

user_result = {}
for subject in subjects:
    user_result[subject]=list()
    subject_data = dataset.loc[dataset.subject == subject,"H.period":"H.Return"]
    other_user_data = dataset.loc[dataset.subject != subject,"H.period":"H.Return"]    
    subject_test_data = subject_data[:1]
    


    index = 0
    train_drop_index = []
    test_drop_index = []

    index = 0
    i=0
    user_scores = 0
    for drp in subjects:
        if index > 0:
                test_drop_index = []
                train_user_data = other_user_data[400*i:400*i+10]
                i+=1

                mean_vector = train_user_data.mean().values
                std_deviation_vector = train_user_data.std().values
                #print("Mean Vector: ",mean_vector)
                #print("Standard Deviation Vector: ",std_deviation_vector)
                indices = []
                for l in range(train_user_data.shape[0]):
                        distance = euclidean(subject_data.iloc[l].values,mean_vector)
                        if (distance > 3*std_deviation_vector).all()==True:
                                indices.append(l)
                
                train_user_data = train_user_data.drop(train_user_data.index[indices])
                trained_model = train_user_data.mean().values
                for m in range(subject_test_data.shape[0]):
                        manhattan_dist = 1-(cityblock(subject_test_data.iloc[m].values,trained_model))/subject_test_data.iloc[m].shape[0]
                        #user_result[subject].append(manhattan_dist)
                        if manhattan_dist > 0.85:
                                user_scores+=1

        index+=1
    user_result[subject] = user_scores
print(user_result)
wolf = 0
lamb = 0
goat = 0
sheep = 0
for ur in user_result:
    res = float(int(user_result[ur])/50)
    if res>0.8:
        wolf+=1
    elif res >0.6 and res<0.8:
        lamb+=1
    elif res >0.0 and res<0.6:
        sheep+=1
    else:
        goat+=1
print("No. of wolf: ",wolf)
print("No. of lamb: ",lamb)
print("No. of goat: ",goat)
print("No. of sheep: ",sheep)
              
    


    

