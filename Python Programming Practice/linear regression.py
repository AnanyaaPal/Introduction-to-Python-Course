#importing necessary libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics

#import the dataset
df=pd.read_csv('C:\Users\Ananya Pal\Documents\TUD\1st semester\Introduction to Python\Lessons\Introduction-to-Python-Course\Python Programming Practice\HousingPrices.csv')

