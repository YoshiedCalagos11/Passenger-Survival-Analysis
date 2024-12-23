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