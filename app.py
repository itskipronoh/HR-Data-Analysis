import pandas as pd
import matplotlib.pyplot as plt

hr_df = pd.read_csv('hr_data.csv')

bins = [18, 30, 40, 50, 60, 70]
labels = ['18-29', '30-39', '40-49', '50-59', '60-69']

hr_df['Age_Group'] = pd.cut(hr_df['Age'], bins=bins, labels=labels, right=False)
attrition_by_gender_age = hr_df.groupby(['Gender', 'Age_Group'])['Attrition'].value_counts(normalize=True).unstack()

for age_group in labels:

    plt.figure()  
    plt.title(f'Attrition Rate by Gender for Age Group {age_group}')
    attrition_slice_sizes = attrition_by_gender_age.loc[:, age_group].values  
    num_slices = len(attrition_slice_sizes)  

    plt.gcf().set_size_inches(num_slices * 3, 4)
    attrition_by_gender_age.loc[:, age_group].plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen'])
    plt.ylabel('')
    plt.legend(title='Attrition', loc='upper right', labels=['No', 'Yes'])
    plt.show()
