# DATA-RELATED JOBS IN US
* Dataset found on Kaggle: https://www.kaggle.com/datasets/mohamedsiika/data-related-jobs-in-us

The author of this data set made a search on data-related jobs in the US on the Glassdoor webpage. He applied web scraping, performed some data cleaning and used some Machine Learning models to make predictions.

* The goal for this project has been to improve the data cleaning, to do data analysis with meaningful plots about the cleaned dataset and finally apply the required transformations in order to perform Machine Learning models.

## Data cleaning
* Cleaning NaN values and performing a lot of manual data cleaning making searches on the Internet to find missing information.
* Dropping the jobs considered not directly related to the roles established in the column 'job_simpl'.
* I realized at the end of the data cleaning that there were a lot of duplicates.
* Cardinality reduced on the categorical columns.

## Exploratory data analysis (EDA)
* Checking outliers, distributions and collinearity of the columns.
* Insightful information obtained about the average salary depending on the category being analyzed.

## Transformations
* Removing outliers from the few numerical columns available and performeing the necessary transformations to be able to run my models.

## Models
* Several models were tried alongside Grid and Bayes search cross-validation to iterate and try to get the best possible model.
* In the end no model performed especially well to make predictions.

### Next steps:
* To collect a higher sample.
* To perform a more detailed data cleaning in case I had more time.
* To use other techniques in order to get better prediction models. 