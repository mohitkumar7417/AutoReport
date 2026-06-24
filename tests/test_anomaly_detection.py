import pandas as pd

from autoreport.anomaly_detection import (
    detect_zscore_outliers,
    detect_iqr_outliers
)

sales = pd.Series([50, 80, 30, 500])

print("Z-Score Outliers:")
print(detect_zscore_outliers(sales))

print("\nIQR Outliers:")
print(detect_iqr_outliers(sales))