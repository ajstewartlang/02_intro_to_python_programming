# Pandas for Data Analysis

In this third workshop we will focus on using the pandas library for data wrangling and analysis.

%%HTML
<div style="text-align: center">
<iframe width="560" height="315" src="https://youtube.com/embed/HjF98JryayQ" frameborder="0" allowfullscreen></iframe>

</div>

## Importing pandas

Fire up a Jupyter Notebook. In order to read in and then wrangle our data, the first thing we need to do once we've opened a new script in our `data_science` environment is to import the pandas library. You can read more about the library [here](https://pandas.pydata.org/).

import pandas as pd

We'll start by reading in some data using the pandas function `pd.read_csv`. The data are available via the http address below. This is the same data file that we looked at in the R workshop on ANOVA. 

24 participants responded to a word that was either common (i.e., high lexical frequency) or rare (i.e., low lexical frequency). This is our IV and is coded as ‘high’ vs. low’. Our DV is reaction time and is coded as ‘RT’. Subject number is coded as ‘Subject’. We want to know whether there is a difference between conditions (and if so, where that difference lies). 

We need to visualise the data, generate descriptives, and run the appropriate ANOVA to determine whether our independent variable (Condition) has an influence on our dependent variable (RT).

anova_data = pd.read_csv("https://raw.githubusercontent.com/ajstewartlang/02_intro_to_python_programming/main/data/ANOVA_data1.csv")

anova_data

## Visualising Our Data

In order to visualise the data we need to use the `matplotlib` library. This library contains a range of tools for visualising data. You can read more about it [here](https://matplotlib.org/stable/). 

import matplotlib.pyplot as plt

In the code below we used the `plot` function from `pyplot`. We build our final plot layer be layer (similar to how we do things in `R` with `ggplot2`. We define our plot initially in terms of what's on the x-axis, what's on the y-axis, and then what marker we want to use - which in this case is blue circles.

After this, we then add an x-axis label, a y-axis label, and a title. We also set the margins to make the plot like nice.

plt.plot(anova_data['Condition'], anova_data['RT'], 'bo')
plt.xlabel('Condition')
plt.ylabel('RT (ms.)')
plt.title('Reaction Time by Condition')
plt.margins(.5, .5)

Let's now work out some descriptive statistics using `pandas`  functions. We'll use the `groupby` function to group our RT data by condiiton, and we'll map this onto a new variable I'm calling `grouped`.

grouped = anova_data.groupby(['Condition'])

We can then generate some descriptives about this grouped data frame. We can use the `count` function to work out how many observations we have for each of our two conditions.

grouped.count()

If we wanted just to output the count for our `RT` column we could do the following.

grouped.count()['RT']

From the above we can see we have 12 observations in each condition, and our variable RT is type integer. We can use other `pandas` functions such as `mean()` and `std()` in a similar way.

grouped.mean()['RT']

grouped.std()['RT']

We can map our means onto a new variable I'm calling `my_means` and then we can plot these means as a bar graph.

my_means = grouped.mean()['RT']
my_means.plot(kind='bar')
plt.ylabel('RT (ms.)')
plt.title('Reaction Time by Condition')

## One-Way ANOVA

To run a between participants one-way ANOVA to determine whether there is a difference between our two conditions we're going to use the `stats` module from the `scipy` library. We import it as follows... 

from scipy import stats

We are now going to subset our `anova_data` data frame. We are going to do that by using a logical condition `[anova_data['Condition']=='high']`. If we were to run the following we'd see we have the subset of the data frame where Condition is equal to 'high'.

anova_data[anova_data['Condition']=='high']

But what we really want is to just select the `RT` column.

anova_data[anova_data['Condition']=='high']['RT']

By builing on the above we can create two new variables, one corresponding to the data for the `high` condition group and the other for the `low` condition group.

high_group = anova_data[anova_data['Condition']=='high']['RT']
low_group = anova_data[anova_data['Condition']=='low']['RT']

We are now in a position to run a 1-way ANOVA. We use the`f_oneway` function in the `stats` module to do this. The two parameters that it needs are the two groups that we are wanting to compare to test the null hypothesis that the two groups have the same population mean. If we had three groups, we would just pass the three groups to the function.  

stats.f_oneway(high_group, low_group)

Remember, the p-value is the probability of obtaining test results at least as extreme as the results observed, under the assumption that the null hypothesis is true. Note, the output above gives us the F-value and the p-value but not the degrees of freedom. As we just have two groups, we could also run an independent sample t-test using the `ttest_ind` function from `stats`.

stats.ttest_ind(high_group, low_group)

Note that the p-value is the same as we found with our ANOVA - and if we square the t-value we get the F-value.

9.550751765227444 * 9.550751765227444

If we had three groups in our study, we could run the 1-way ANOVA as we did above and then if that it significant run multiple t-tests with a manually adjusted alpha level (e.g., using the Bonferroni correction). One of the limitations with using the `stats` module is that degrees of freedom are not reported, nor is information about the residuals. In order to generate an ANOVA table more like the type we're familiar with we are going to use the statsmodels package. This isn't a package we yet have in our `data_science` environment so we need to install it using the Terminal shell.  

Go into your shell and activate the `data_science` environment using `conda activate data_science`. You then need to install the library using `conda install statsmodels`. Once that library is installed, go back to your Jupyer Notebook and you should be able to import the statsmodels library and the ols modules (for ordinary least squares models) as follows.

import statsmodels.api as sm
from statsmodels.formula.api import ols

We define our model below using syntact not too disimilar from how we did the same in R. We are going to fit an OLS model to our data where our outcome variable `RT` is predicted by `Condition`. We then present the results in an ANOVA table using Type 3 Sums of Squares. This is much closer to the level of detail that we need.

model = ols('RT ~ Condition', data=anova_data).fit()
anova_table = sm.stats.anova_lm(model, typ=3)
anova_table

Add challenge here using 1 factor with 3 levels:
    
    anova_data = pd.read_csv("https://raw.githubusercontent.com/ajstewartlang/02_intro_to_python_programming/main/data/ANOVA_data2.csv")

## Factorial ANOVA

In many types of experiments we are interested in how two (or more) experimental factors interact with each other. For example, in a typical priming paradigm experiment we might be interested in whether people's response times to a positively or negatively valenced target stimulus are influenced by whether it was preceded by a positively or negatively valenced prime. 

factorial_anova_data = pd.read_csv("https://raw.githubusercontent.com/ajstewartlang/02_intro_to_python_programming/main/data/ANOVA_data3.csv")

factorial_anova_data

grouped = factorial_anova_data.groupby(['Prime', 'Target'])
group_means = grouped.mean()['RT']
group_means

group_means.plot(kind="bar")

While the above plot looks *ok*, it's a little tricky seeing the nature of the interaciton. Luckily the `statsmodels` library has a function for plotting the kind of interaction we are interested in looking at.

from statsmodels.graphics.factorplots import interaction_plot

We need to create a pandas data frame that contains the means for our four conditions, and captures the 2 x 2 nature of our design. We can use `pd.DataFrame` to turn our object of means by condition into a data frame that we can then use in our interaction plot.

group_means = grouped.mean()
pd.DataFrame(group_means)

We need to reset the grouping in the data frame above so that we can use it in our plot. We do that using the `reset_index()` method.

to_plot = pd.DataFrame(group_means).reset_index()
to_plot

The above now looks much more like a standard data frame.

my_interaction_plot = interaction_plot(x=to_plot['Target'], trace=to_plot['Prime'], 
                                       response=to_plot['RT'], colors=['red', 'blue'], 
                                       markers=['D', '^'])
plt.xlabel('Target')
plt.ylabel('RT (ms.)')
plt.title('Reaction Times to Target Type as a Function of Prime Type')
plt.ylim(0)
plt.margins(.5, 1)

To build the factorial ANOVA model, we use the `AnovaRM` function from the `statsmodels` library. We need to specify our outcome variable (RT), our grouping variable (this is our random effect) plus our within participant effects. 

from statsmodels.stats.anova import AnovaRM

factorial_model = AnovaRM(data=factorial_anova_data, depvar='RT', within=['Prime', 'Target'], subject='Subject').fit()

print(factorial_model)

We can also use this function to build ANOVAs with between participant factors. We just need to specifiy those with the parameter `betweeen` much in the same way we have done above with `within`. We see from the above that both main effects, plus the interaction are significant at p < .001. In order to interpret the interaction, we need to conduct pairwise comparisions. There are 2 key comparisons that will tell us where we have a priming effect. The first is comparining RTs to Positive Targets for Positive vs. Negative Primes, and the second is comparing RTs to Negative Targets following Positive vs. Negative Primes. We can effectively run these comparisons as t-tests and adopt a critical alpha level of .025 to control for the familywise error associated with running two tests.

One way to run the t-tests is to filer out data frame and create new variables for each of the condition combinations we want to compare. In the code below, I create a boolean index (i.e., True and False values) corresponding to cases where the Prime AND the Target are both Positive. I then apply this logical index to the data frame and map the RT column of that filtered data frame onto a new variable I am calling PP. 

index = (factorial_anova_data['Prime']=='Positive') & (factorial_anova_data['Target']=='Positive')
PP = factorial_anova_data[index]['RT']

I then do the same for cases where the Prime is Negative and the Target is Positive. I can now run a t-test using the `stats.ttest_rel` function for paired samples t-tests.

index = (factorial_anova_data['Prime']=='Negative') &(factorial_anova_data['Target']=='Positive')
NP = factorial_anova_data[index]['RT']

stats.ttest_rel(PP, NP)

We can see that this comparison is significant. Your challenge now is to write the code for the other comparison - in other words, comparing RTs to Negative Targets following Positive vs. Negative Primes.

```{admonition} Click the button to reveal answer
:class: dropdown 
    my_favourite_number = 25
    my_favourite_number_text = "is my favourite number."
    print(my_favourite_number, my_favourite_number_text)
```

index = (factorial_anova_data['Prime']=='Positive') & (factorial_anova_data['Target']=='Negative')
PN = factorial_anova_data[index]['RT']

index = (factorial_anova_data['Prime']=='Negative') &(factorial_anova_data['Target']=='Negative')
NN = factorial_anova_data[index]['RT']

stats.ttest_rel(PN, NN)

PP.mean()



NP.mean()