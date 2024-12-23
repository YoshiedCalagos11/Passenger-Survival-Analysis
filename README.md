# Data Analytics Project: Titanic Tragedy Analysis

## Goal of the Project
- Investigate if the survival rate is influenced by passenger class.
- Assess the age of passengers within each class to identify vulnerable age categories.

## Business Perspective

### Meeting with Management
- The company aims to build a ship and wants to investigate the Titanic tragedy to improve future designs.
- The goal is to ensure that in emergencies, all passengers, regardless of age and class, have equal access to equipment.
- Management believes that higher-class passengers had more opportunities to escape.
- The research will focus on whether age and class affected the survival rate during the Titanic tragedy.

### Follow-Up Questions to Manager
- Document tasks during the meeting.
- Formulate the goal: Determine if age and class influenced the survival rate.
- Ask what visualizations the manager wants.
- Inquire if they want to filter the data by age to see if the difference between classes grows or shrinks.

## Visualization

### Bar Plot 1
- **Numeric Column and Aggregation**: 
  - Survived: Sum
- **Categorical Column**: 
  - Pclass
- **Active Filter**: 
  - Age

### Bar Plot 2
- **Numeric Column and Aggregation**: 
  - Survived: Percentage
- **Categorical Column**: 
  - Pclass
- **Active Filter**: 
  - Age

### X Plot 3
- **Numeric Column and Aggregation**: 
  - Survived: Percentage
- **Categorical Columns**: 
  - Pclass
  - Age (Children, Adults, Seniors)
- **Active Filter**: 
  - None

### Additional Visualization
- **Pie Chart**: Shows the overall percentage for each class.

## Data Gathering
- Download the data from Kaggle: Titanic Dataset.
- Create a schema in MySQL and insert the tables from Kaggle.

## Data Description
| Variable | Definition | Key |
|----------|-------------|-----|
| survival | Survival | 0 = No, 1 = Yes |
| pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd |
| sex | Sex | |
| Age | Age in years | |
| sibsp | # of siblings / spouses aboard the Titanic | |
| parch | # of parents / children aboard the Titanic | |
| ticket | Ticket number | |
| fare | Passenger fare | |
| cabin | Cabin number | |
| embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton |

## Data Cleaning
- Using VSCode:
  - Clean the tables: if blank/null, set to none.
  - Combine data from three Excel sheets into one for easier SQL commands.
  - Set all blank ages to 0.
  - Round up all decimals.

### Categorize Age
- Create a new column to categorize age as Children, Youth&Adults, or Seniors using the following Python script:

```python
import pandas as pd

# Load the Excel file
df = pd.read_excel('firstsheet.xlsx')

# Define a function to categorize age
def categorize_age(age):
    if age <= 14:
        return 'Children'
    elif 15 <= age <= 64:
        return 'Youth&Adults'
    else:
        return 'Seniors'

# Apply the function to create a new column 'age_category'
df['age_category'] = df['Age'].apply(categorize_age)

# Save the updated DataFrame back to an Excel file
df.to_excel('firstsheet_with_age_category.xlsx', index=False)

print("The new column 'age_category' has been added and saved to 'firstsheet_with_age_category.xlsx'.")
