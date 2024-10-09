import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#loading the data
HID_df=pd.read_csv('https://health.data.ny.gov/resource/5dtw-tffi.csv')
print (HID_df.info())
###length_of_stay
#transform string tpye to numeric type
HID_df['length_of_stay']=pd.to_numeric(HID_df['length_of_stay'],errors='coerce')
#calculate length of stay for mean, median, sd, min,max, percentile and quartiles
mean_len_stay=HID_df['length_of_stay'].mean()
print(mean_len_stay)
median_leb_stay=HID_df['length_of_stay'].median()
print(median_leb_stay)
sd_len_stay=HID_df['length_of_stay'].std()
print(sd_len_stay)
min_len_stay=HID_df['length_of_stay'].min()
print(min_len_stay)
max_len_stay=HID_df['length_of_stay'].max()
print(max_len_stay)
percentiles_len_stay = HID_df['length_of_stay'].quantile([0.25, 0.50, 0.75])
print(percentiles_len_stay)
###total charge and total cost
#transform string tpye to numeric type
HID_df['total_charges'] = HID_df['total_charges'].str.replace('[\$,]', '', regex=True)
HID_df['total_charges']=pd.to_numeric(HID_df['total_charges'],errors='coerce')
HID_df['total_costs'] = HID_df['total_costs'].str.replace('[\$,]', '', regex=True)
HID_df['total_costs']=pd.to_numeric(HID_df['total_costs'],errors='coerce')
#caculate mean, median, sd, min,max, percentile and quartiles
#total charges
mean_total_charges=HID_df['total_charges'].mean()
print(mean_total_charges)
median_total_charges=HID_df['total_charges'].median()
print(median_total_charges)
sd_total_charges=HID_df['total_charges'].std()
print(sd_total_charges)
min_total_charges=HID_df['total_charges'].min()
print(min_total_charges)
max_total_charges=HID_df['total_charges'].max()
print(max_total_charges)
percentiles_total_charges = HID_df['total_charges'].quantile([0.25, 0.50, 0.75])
print(percentiles_total_charges)
##total cost
mean_total_costs=HID_df['total_costs'].mean()
print(mean_total_costs)
median_total_costs=HID_df['total_costs'].median()
print(median_total_costs)
sd_total_costs=HID_df['total_costs'].std()
print(sd_total_costs)
min_total_costs=HID_df['total_costs'].min()
print(min_total_costs)
max_total_costs=HID_df['total_costs'].max()
print(max_total_costs)
percentiles_total_costs = HID_df['total_costs'].quantile([0.25, 0.50, 0.75])
print(percentiles_total_costs)

##	Count the distribution of Age Group, Gender, and Type of Admission.
age_group_count = HID_df['age_group'].value_counts()
print(age_group_count)
gender_count = HID_df['gender'].value_counts()
print(gender_count)
type_of_admission_count = HID_df['type_of_admission'].value_counts()
print(type_of_admission_count)

##	Create a bar plot to visualize the counts of Age Group, Gender, and Type of Admission.
##age_group
plt.figure(figsize=(6, 4))
sns.countplot(x='age_group', data=HID_df, order=HID_df['age_group'].value_counts().index)
plt.title('Distribution of Age Group')
plt.xlabel('Age Group')
plt.ylabel('Frequency')
plt.show()

##gender
plt.figure(figsize=(6, 4))
sns.countplot(x='gender', data=HID_df, order=HID_df['gender'].value_counts().index)
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.show()

##type of admission
plt.figure(figsize=(6, 4))
sns.countplot(x='type_of_admission', data=HID_df, order=HID_df['type_of_admission'].value_counts().index)
plt.title('Distribution of type of submission')
plt.xlabel('Type of submission')
plt.ylabel('Frequency')
plt.show()

##	Create at least 3 visualizations to summarize the dataset:
##  Histogram of Length of Stay to show its distribution
plt.figure(figsize=(6, 4))
sns.histplot(HID_df['length_of_stay'], bins=30, kde=True)
plt.title('Distribution of Length of Stay')
plt.xlabel('Length of Stay (Days)')
plt.ylabel('Frequency')
plt.show()

##	Boxplot for Total Charges to identify outliers.
print(HID_df['total_charges'].isnull().sum())

plt.figure(figsize=(6, 4))
sns.boxplot(x='total_charges', data=HID_df)
plt.title('Boxplot of Total Charges')
plt.xlabel('total_charges ($)')
plt.show()


##  Bar plot for Type of Admission to analyze admission trends (e.g., Emergency, Elective, Trauma).
plt.figure(figsize=(6, 4))
sns.countplot(x='type_of_admission', data=HID_df, order=HID_df['type_of_admission'].value_counts().index)
plt.title('Distribution of Type of Admission')
plt.xlabel('Type of Admission')
plt.ylabel('Count')
plt.show()

##6.	Handling Missing Data:
print(HID_df.loc[HID_df['length_of_stay'].isnull()])
HID_df.loc[HID_df['length_of_stay'].isnull(),'length_of_stay']=HID_df['length_of_stay'].mean()
print(HID_df.info())

##7.Summary Report:
## What is the average length of stay?
## The average length of stay is 5.97 days. Based on the mean value of the length of stay.
## How does the total cost vary by age group or type of admission?
print(HID_df.groupby('age_group')['total_costs'].mean())
print(HID_df.groupby('type_of_admission')['total_costs'].mean())

print(HID_df.groupby('age_group')['total_costs'].max())
print(HID_df.groupby('type_of_admission')['total_costs'].max())



## Any noticeable trends in admissions or charges?

