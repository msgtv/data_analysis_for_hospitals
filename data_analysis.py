import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 8)

general = pd.read_csv('test/general.csv', encoding='utf-8')
prenatal = pd.read_csv('test/prenatal.csv', encoding='utf-8')
sports = pd.read_csv('test/sports.csv', encoding='utf-8')

prenatal.columns = general.columns
sports.columns = general.columns
union = pd.concat([general, prenatal, sports], ignore_index=True, join='inner')

union.drop(columns='Unnamed: 0', inplace=True)

union = union.dropna(axis=0, how='all')

union['gender'] = union['gender'].replace(['female', 'woman', np.nan], 'f')
union['gender'] = union['gender'].replace(['male', 'man'], 'm')

for x in ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']:
    union[x] = union[x].fillna(0)
ages_list = [15, 35, 55, 70, 80]
ages = dict()

# Below the code for first question!
for i in range(len(ages_list)):
    if ages_list[i] != 15:
        ages[str(ages_list[i - 1]) + ' - ' + str(ages_list[i])] = union.age[union['age'] < ages_list[i]].count() - union.age[union['age'] < ages_list[i - 1]].count()
    else:
        if ages_list[i] == 15:
            ages['0 - 15'] = union.age[union['age'] < 15].count()

pd.Series(ages).plot(kind='bar')
plt.show()
# Second question
union.diagnosis.value_counts().plot(kind='pie')
plt.show()
# Third question
#sns.set_theme(style="whitegrid")

ax = sns.violinplot(x="hospital", y="age", data=union)
plt.show()

print('The answer to the 1st question:', max(ages, key=ages.get))
print('The answer to the 2nd question:', union.diagnosis.value_counts().index[0])
print('The answer to the 3rd question: ages')
