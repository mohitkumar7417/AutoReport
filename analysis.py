def count_records(df):
    return len(df)


def total_sum(df, column):
    return df[column].sum()


def average(df, column):
    return df[column].mean()


def minimum(df, column):
    return df[column].min()


def maximum(df, column):
    return df[column].max()

def median(df, column):
    return df[column].median()

def standard_deviation(df, column):
    return df[column].std()

def percentile(df, column, value):
    return df[column].quantile(value)

def group_by_sum(df, group_column, value_column):
    return df.groupby(group_column)[value_column].sum()