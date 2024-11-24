# Project Birch - Clustering Algorithm

This project implements the Birch clustering algorithm and tests it on the digits dataset from scikit-learn.

## Key Parameters
- `threshold`: Maximum radius of clusters.
- `branching_factor`: Maximum number of subclusters in each node of the clustering tree.

## Project Structure
- `birch.py`: Implementation of the Birch algorithm.
- `test_birch.py`: Unit tests for the Birch implementation.
- `Birch_analysis.ipynb`: Notebook for analyzing and visualizing clustering results.

## Results of the Birch Algorithm on the `digits` Dataset

- **Parameters:**
  - `threshold`: 15
  - `branching_factor`: 50
- **Metrics:**
  - Homogeneity Score: 1.0
  - Completeness Score: 0.32

### Visualization:
![Clusters by Birch](clusters.png)

### Results for `threshold=10` and `branching_factor=30`
- **Metrics:**
  - Homogeneity Score: 1.00
  - Completeness Score: 0.30
- **Visualization:**
  ![Clusters by Birch](clusters_threshold_10_branching_30.png)

### Results for `threshold=12` and `branching_factor=40`
- **Metrics:**
  - Homogeneity Score: 1.00
  - Completeness Score: 0.31
- **Visualization:**
  ![Clusters by Birch](clusters_threshold_12_branching_40.png)

| Threshold | Branching Factor | Homogeneity Score | Completeness Score |
|-----------|------------------|-------------------|--------------------|
| 10        | 30               | 1.00              | 0.30               |
| 12        | 40               | 1.00              | 0.31               |
| 15        | 50               | 1.00              | 0.32               |

## Conclusions

Based on the tested configurations of the Birch algorithm on the `digits` dataset:

1. **Homogeneity Score**:
   - All tested configurations achieved a perfect homogeneity score of 1.00, indicating that each cluster contains only data points from a single class.

2. **Completeness Score**:
   - The completeness score slightly improves with higher values of `threshold` and `branching_factor`.
   - The best completeness score (0.32) was achieved with `threshold=15` and `branching_factor=50`.

3. **Optimal Configuration**:
   - The most balanced configuration is:
     - **Threshold**: 15
     - **Branching Factor**: 50
     - This configuration provides the best completeness score while maintaining a perfect homogeneity score.

4. **Impact of Parameters**:
   - **Threshold**: Lower values create more clusters, which might reduce the completeness score.
   - **Branching Factor**: Lower values can lead to a more detailed clustering structure but may slightly impact completeness.
