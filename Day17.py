# python3 -m pip install pandas
# python3 -m pip install --upgrade pip
# python3 -m pip install numpy
# python3 -m pip install matplotlib
# python3 -m pip install scikit-learn
# We just need to call the function once to install the library
# python3 -m pip install seaborn
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
sns.lineplot(data=tips, x="size", y="tip")
sns.barplot(data=tips, x="day", y="total_bill")
sns.scatterplot(data=tips, x="total_bill", y="tip")
sns.histplot(data=tips, x="total_bill")
plt.show()
