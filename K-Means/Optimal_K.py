import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans


def find_optimal_k(image_path, max_k):
    # Open and load the image
    image = Image.open(image_path)
    image_data = np.array(image)

    # Reshape the image data to be a list of RGB pixels
    pixels = image_data.reshape(-1, 3)

    # Calculate inertia for a range of K values
    inertias = []
    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(pixels)
        inertias.append(kmeans.inertia_)

    # Plot the inertia graph to find the optimal K
    plt.figure(figsize=(8, 4))
    plt.plot(range(1, max_k + 1), inertias, marker='o')
    plt.title('Elbow Method for Optimal K')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('Inertia')
    plt.show()

if __name__ == "__main__":

    input_image_path = "input_image.jpg"

    # Maximum number of clusters to test
    max_k = 20

    # Find the optimal K using the elbow method
    find_optimal_k(input_image_path, max_k)
