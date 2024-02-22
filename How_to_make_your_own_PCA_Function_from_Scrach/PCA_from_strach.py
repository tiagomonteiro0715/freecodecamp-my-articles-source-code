import numpy as np

def PCA_from_scratch(X, num_components):
    # Step 1: Standardize the data
    X_standardized = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    
    # Step 2: Compute the covariance matrix
    covariance_matrix = np.cov(X_standardized, rowvar=False)
    
    # Step 3: Calculate the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    
    # Step 4: Sort the eigenvalues and eigenvectors
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    
    # Step 5: Select a subset of the eigenvectors (dimensionality reduction)
    eigenvector_subset = sorted_eigenvectors[:, 0:num_components]
    
    # Step 6: Transform the original matrix
    X_reduced = np.dot(X_standardized, eigenvector_subset)
    
    return X_reduced

# Example usage
# Create a sample dataset
np.random.seed(0) # For reproducibility
X_sample = np.random.rand(10, 5) # Sample dataset with 10 instances and 5 features

# Apply our PCA function to reduce the dataset to 2 principal components
X_reduced = PCA_from_scratch(X_sample, 2)

X_reduced
