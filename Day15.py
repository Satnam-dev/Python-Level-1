# # These are internal libraries that are commonly used in Python for various tasks

# #  Random => Random number generation
# import random
# print(random.randint(1, 10))


# # datetime => Date and time manipulation
# import datetime
# now = datetime.datetime.now()
# print("Current date and time:", now)    

# # math => Mathematical functions
# import math 
# print(math.sqrt(16))   # we can use different mathematical functions like sqrt, sin, cos, etc.


# # These are external libraries that are commonly used in Python for various tasks

# # os => Operating system interaction
# import os
# print(os.getcwd())  # Get current working directory

# # Numpy => Numerical computation and arrays 
# # used to perform mathematical operations and numerical operartons


# import numpy as np
# arr =  np.array([1, 2, 3,4, 5, 6])
# print(arr.mean())

# import numpy as np
# arr =  np.array([1, 2, 3,4, 5, 6])
# print(arr.reshape(2,3))

# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# resultant_arr = arr1 + arr2 # we can use different mathematical operations like addition, subtraction, multiplication, etc. on numpy arrays
# print(resultant_arr)  

# # pandas => Data manipulation and analysis

# import pandas as pd
# data = {'Name': ['Mannat','Anjali','Rama'],
#         'id': [20, 21, 19]}
# df = pd.DataFrame(data)
# print(df)


# import pandas as pd
# data = {'Name': ['Mannat','Anjali','Rama'],
#         'id': [21, 21, 24]}
# df = pd.DataFrame(data)
# print(df['Name'])

# import pandas as pd
# data = {'Name': ['Mannat','Anjali','Rama'],
#         'Age': [21, 21, 24]}
# df = pd.DataFrame(data)
# print(df[df['Age']>20]) # it will filter the data and return only those rows whose age is greater than 20


# # matplotlib => to create graphs,charts & plots from data

# import matplotlib.pyplot as plt
# months = ['jan','feb','mar','apr']
# sales = [100,200,300,50]

# plt.plot(months,sales)
# plt.title("monthly sales")
# plt.xlabel("months")
# plt.ylabel("sales")
# plt.title("sales data")
# plt.show()

# import matplotlib.pyplot as plt
# months = ['jan','feb','mar','apr']
# sales = [100,200,300,50]

# plt.bar(months,sales)
# plt.title("monthly sales")
# plt.xlabel("months")
# plt.ylabel("sales")
# plt.title("sales data")
# plt.show()

# import matplotlib.pyplot as plt
# months = ['jan','feb','mar','apr']
# sales = [100,200,300,50]

# plt.pie(sales,labels = months,autopct = '%1.1f%%')
# plt.title("sales data")
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
# load dataset 
tips = sns.load_dataset('tips')
sns.lineplot(data=tips,x="size",y="tip")
sns.barplot(data=tips,x="day",y="total_bill")
sns.scatterplot(data=tips,x="total_bill",y="tip")
sns.histplot(data=tips,x="total_bill")
plt.show()
