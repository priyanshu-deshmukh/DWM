import pandas as pd
#Input Data
data = {
    'ID': [1,2,3,4,5,6],
    'Name': ['Arjun', 'Sonam', 'Raju', 'Tushar', 'Akshay', 'Rishil'],
    'Age': [25, 30, 35, 40, 22, 29],
    'Country': ['Maharashtra', 'UP', 'Gujrat', 'Rajasthan', 'Kerela', 'Punjab'],
    'Sales': [200, 450, 300, 800, 150, 400]
}
#Create Dataframe
df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

#Data Flow Transformations
#Character Map
#Description: Transform text data by changing the case of characters.
# Here, we will convert the name column to uppercase
df['Name_Upper'] = df['Name'].str.upper()
print("\nCharacter Map (Uppercase Names):")
print(df[['ID', 'Name', 'Name_Upper']])

# Multicast: Create two copies of the dataset
df_copy1 = df.copy()
df_copy2 = df.copy()

#Transformations on each copy
df_copy1['Sales'] *= 1.1 #Increase sales by 10%
df_copy2['Age'] += 5 #Increase age by 5 years

print("\nMulticast (Modified Copies:")
print("Copy 1 (Sales Increased):")
print(df_copy1)
print("\nCopy2 (Age Increased):")
print(df_copy2)

# Conditional Split
#Description: Split data based on a condition
#Conditional Split: Sales > 300
high_sales = df[df['Sales']>300]
low_sales = df[df['Sales']<=300]
print("\nConditional Split:")
print("High Sales:")
print(high_sales)
print("Low Sales:")
print(low_sales)

#Aggregation
#Description: Aggregate data, e.g., cakculate total sales by country.
# Aggregation : Total sales by Country
agg_df = df.groupby('Country')['Sales'].sum().reset_index()
print("\nAggregation (Total Sales by Country):")
print(agg_df)

#sort
#Description: Sort the dataset by Sales in descending order.
#Sort: Sort by Sales in descending order
sorted_df = df.sort_values(by='Sales', ascending = False)
print("\n Sort (Descending Sales):")
print(sorted_df)

#Derived Column
#Description: Create a new column by deriving information from existing data.
#Derived Column: Categorize sales as 'High' or 'Low'
df['Sales_Category'] = df['Sales'].apply(lambda x: 'High' if x > 300 else 'Low')
print("\nDerived Column (Sales Category):")
print(df[['ID', 'Name', 'Sales', 'Sales_Category']])