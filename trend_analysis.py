def moving_average(df, column, window=2):
    return df[column].rolling(window=window).mean()

def growth_rate(previous_value, current_value):
    return ((current_value - previous_value) / previous_value) * 100

def cumulative_growth(series):
    return ((series.iloc[-1] - series.iloc[0]) / series.iloc[0]) * 100