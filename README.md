# Image-Compression-Using-K-Means
Image Compression with K-Means Clustering and Elbow Method

This project demonstrates the use of the K-Means clustering algorithm for compressing an image, while incorporating the elbow method to determine the optimal number of clusters (K). The elbow method is a technique to find the inflection point in the inertia graph, indicating the suitable number of clusters.

Overall, this project contains four Python scripts. First, there is a 2-Dimensional script that performs K-Means clustering in a 2-dimensional space for a range of K values (from 1 to max_k) and plots the inertia (sum of squared distances) against the number of clusters. Then, there is a 3-Dimensional script which extends the first script into 3-dimensional space. After applying the elbow method in 2 and 3-dimensional spaces, I used it to find the optimal number of clusters for an image in the 'optimal_K' script. The result plot showed that the optimal number for K would be 3. So, I provided 3 as an input in the 'Compress_Image' script and compressed the file
