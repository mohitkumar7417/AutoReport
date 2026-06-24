def z_score(series):
    mean = series.mean()
    std = series.std()

    return (series - mean) / std

def detect_zscore_outliers(series, threshold=2):
    z_scores = z_score(series)

    return series[abs(z_scores) > threshold]

def detect_iqr_outliers(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    return series[
        (series < lower_bound) |
        (series > upper_bound)
    ]