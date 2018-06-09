
import keras
import os
import gc
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten

import ExtractionFeatures

def classifier(df):


    featuers_name=[f for f in train_df.columns if f not in ['TARGET','SK_ID_CURR','SK_ID_BUREAU','SK_ID_PREV']] 
    # Setting 
    train_x, train_label = train_df[featuers_name], train_df['TARGET']
    test_x = test_df[featuers_name]



    print(test.shape)
    input()

    model=Sequential()
    model.add(Activation('relu'))
    model.add(Dense())

    del train_x,train_y, test_x
    gc.collect

    return model


if __name__ == "__main__":
    submission_file_name = "submission.csv"
    training_file='../data/training.csv'
    testing_file ='../data/testing.csv'
    # read file
    if (os.path.exists(training_file)==False or os.path.exists(testing_file)==False):
        ExtractionFeatures.main() # Extraction Features
    
    print('Reading training date...')
    training=pd.read_csv(training_file)
    print(training.shape)
    input()

    # train classifier
    submission_file=classifier(training)
    submission_file.to_csv(submission_file_name, index=False)
