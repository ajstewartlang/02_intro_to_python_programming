import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

four_levels_anova_data = pd.read_csv("https://raw.githubusercontent.com/ajstewartlang/02_intro_to_python_programming/main/data/ANOVA_data2.csv")

model = ols('RT ~ Condition', data=four_levels_anova_data).fit()
anova_table = sm.stats.anova_lm(model, typ=3)
print(anova_table)

group1 = four_levels_anova_data[four_levels_anova_data['Condition'] == 'very high']['RT']
group2 = four_levels_anova_data[four_levels_anova_data['Condition'] == 'high']['RT']
group3 = four_levels_anova_data[four_levels_anova_data['Condition'] == 'low']['RT']
group4 = four_levels_anova_data[four_levels_anova_data['Condition'] == 'very low']['RT']

print(stats.ttest_ind(group1, group2))
print(stats.ttest_ind(group1, group3))
print(stats.ttest_ind(group1, group4))
print(stats.ttest_ind(group2, group3))
print(stats.ttest_ind(group2, group4))
print(stats.ttest_ind(group3, group4))

