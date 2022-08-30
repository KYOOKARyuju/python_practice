#%%
import pandas as pd
import numpy as numpy

train_data= pd.read_csv("train.csv")
train_data = pd.DataFrame(train_data)
train_data
# %%
test_data= pd.read_csv("test.csv")
test_data = pd.DataFrame(test_data)
test_data
# %%
train_data.info()
#%%
test_data.info()
# %%
#nullの数を調べる
train_data["Age"].isnull().sum()

#nullの割合を調べる
# %%
train_data["Age"].isnull().sum()/len(train_data["Age"])*100

# %%
