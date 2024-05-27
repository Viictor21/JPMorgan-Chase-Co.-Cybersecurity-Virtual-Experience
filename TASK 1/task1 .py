import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    pass

def exercise_1(df):
    pass

def exercise_2(df, k):
    pass

def exercise_3(df, k):
    pass

def exercise_4(df):
    pass

def exercise_5(df):
    pass

def exercise_6(df):
    pass

def exercise_7(df):
    pass

def visual_1(df):
    pass

def visual_2(df):
    pass

def exercise_custom(df):
    pass
    
def visual_custom(df):
    pass

df = exercise_0('transactions.csv')
# Step 1: Load the dataset
def exercise_0(file):
    df = pd.read_csv(file)
    return df

# Step 2: Return the column names as a list
def exercise_1(df):
    return df.columns.tolist()

# Step 3: Return the first k rows from the dataframe
def exercise_2(df, k):
    return df.head(k)

# Step 4: Return a random sample of k rows from the dataframe
def exercise_3(df, k):
    return df.sample(n=k)

# Step 5: Return a list of the unique transaction types
def exercise_4(df):
    return df['type'].unique().tolist()

# Step 6: Return a Pandas series of the top 10 transaction destinations with frequencies
def exercise_5(df):
    return df['nameDest'].value_counts().head(10)

# Step 7: Return all the rows from the dataframe for which fraud was detected
def exercise_6(df):
    return df[df['isFraud'] == 1]

# Bonus: Return a dataframe that contains the number of distinct destinations that each source has interacted with, sorted in descending order
def exercise_7(df):
    return df.groupby('nameOrig')['nameDest'].nunique().reset_index().rename(columns={'nameDest': 'distinct_destinations'}).sort_values(by='distinct_destinations', ascending=False)

# Load the dataset
df = exercise_0('C:/Users/aksha/JPMC_Project/transactions.csv')

# Test each function
column_names = exercise_1(df)
first_5_rows = exercise_2(df, 5)
random_5_sample = exercise_3(df, 5)
unique_transaction_types = exercise_4(df)
top_10_destinations = exercise_5(df)
fraud_detected_rows = exercise_6(df)
distinct_destinations_per_source = exercise_7(df)

(column_names, first_5_rows, random_5_sample, unique_transaction_types, top_10_destinations, fraud_detected_rows, distinct_destinations_per_source)
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
sum()
    def exercise_0(file):
    df = pd.read_csv(file)
    return df

# Plot transaction types bar chart
def plot_transaction_types(df):
    # Count the transaction types
    transaction_counts = df['type'].value_counts()
    
    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    transaction_counts.plot(kind='bar', color='skyblue')
    plt.title('Transaction Types')
    plt.xlabel('Transaction Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()
    
    return "This bar chart shows the distribution of different transaction types in the dataset. It helps identify the most common and least common types of transactions."

# Plot transaction types split by fraud bar chart
def plot_transaction_types_by_fraud(df):
    # Count the transaction types split by fraud
    transaction_fraud_counts = df.groupby('type')['isFraud'].
    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    transaction_fraud_counts.plot(kind='bar', color='orange')
    plt.title('Transaction Types Split by Fraud')
    plt.xlabel('Transaction Type')
    plt.ylabel('Count of Fraudulent Transactions')
    plt.xticks(rotation=45)
    plt.show()
    
    return "This bar chart shows the distribution of fraudulent transactions across different transaction types. It highlights which types of transactions are more prone to fraud."

# Plot scatter plot for Cash Out transactions
def plot_cash_out_scatter(df):
    # Filter for Cash Out transactions
    cash_out_df = df[df['type'] == 'CASH_OUT']
    
    # Calculate deltas
    origin_delta = cash_out_df['oldbalanceOrg'] - cash_out_df['newbalanceOrig']
    destination_delta = cash_out_df['oldbalanceDest'] - cash_out_df['newbalanceDest']
    
    # Plot the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(origin_delta, destination_delta, alpha=0.5, color='green')
    plt.title('Origin vs. Destination Account Balance Delta for Cash Out Transactions')
    plt.xlabel('Origin Account Balance Delta')
    plt.ylabel('Destination Account Balance Delta')
    plt.show()
    
    return "This scatter plot shows the relationship between the changes in the origin and destination account balances for Cash Out transactions. It helps identify patterns or anomalies in these transactions."

# Load the dataset
df = exercise_0('C:/Users/aksha/JPMC_Project/transactions.csv')

# Plot and describe the graphs
desc1 = plot_transaction_types(df)
print(desc1)

desc2 = plot_transaction_types_by_fraud(df)
print(desc2)

desc3 = plot_cash_out_scatter(df)
print(desc3)
def visual_1(df):
    def transaction_counts(df):
        # TODO
        pass
    def transaction_counts_split_by_fraud(df):
        # TODO
        pass

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('TODO')
    axs[0].set_xlabel('TODO')
    axs[0].set_ylabel('TODO')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('TODO')
    axs[1].set_xlabel('TODO')
    axs[1].set_ylabel('TODO')
    fig.suptitle('TODO')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return 'TODO'

visual_1(df)
def visual_2(df):
    def query(df):
        # TODO
        pass
    plot = query(df).plot.scatter(x='TODO',y='TODO')
    plot.set_title('TODO')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return 'TODO'

visual_2(df)
def exercise_custom(df):
    # TODO
    pass
    
def visual_custom(df):
    # TODO
    pass