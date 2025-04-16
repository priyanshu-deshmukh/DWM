import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

dataset = pd.read_excel('Treating_Missing_values/Employee_Data.xls')
x = dataset.iloc[:, 3:6].values

# First impute with mean
imputer_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
x[:, 1:3] = imputer_mean.fit_transform(x[:, 1:3])
print(x)

# Then impute with median (overwriting the above)
imputer_median = SimpleImputer(missing_values=np.nan, strategy='median')
x[:, 1:3] = imputer_median.fit_transform(x[:, 1:3])

print(x)
