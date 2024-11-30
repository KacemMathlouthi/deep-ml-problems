import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    standardized_data, normalized_data = [], []
    for column in data.T:
        min = np.min(column)
        max = np.max(column)
        mean = np.mean(column)
        std = np.std(column)

        standardized_column = (column - mean) / std
        standardized_data.append(standardized_column)

        normalized_column = (column - min) / (max - min)
        normalized_data.append(normalized_column)

    standardized_data = np.array(standardized_data).T
    normalized_data = np.array(normalized_data).T
        
    return standardized_data, normalized_data
