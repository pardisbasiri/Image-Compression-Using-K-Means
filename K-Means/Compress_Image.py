import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans

def compress_image(image_path, output_path, k):
    # Open and load the image
    image = Image.open(image_path)
    image_data = np.array(image)

    # Reshape the image data to be a list of RGB pixels
    pixels = image_data.reshape(-1, 3)

    # Apply K-Means clustering to reduce the number of colors
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    labels = kmeans.predict(pixels)
    centers = kmeans.cluster_centers_.astype(int)

    # Create a compressed image by assigning each pixel to its nearest cluster center
    compressed_pixels = centers[labels].reshape(image_data.shape)

    # Convert the numpy array back to an image
    compressed_image = Image.fromarray(compressed_pixels.astype('uint8'))

    compressed_image.save(output_path)

    # Display the original and compressed images
    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    plt.title("Original Image")
    plt.imshow(image)
    plt.axis('off')

    plt.subplot(122)
    plt.title(f"Compressed Image (K={k})")
    plt.imshow(compressed_image)
    plt.axis('off')

    plt.show()

if __name__ == "__main__":

    input_image_path = "input_image.jpg"
    output_image_path = "compressed_image.jpg"

    optimal_k = int(input("Enter the optimal K value from the graph: "))

    compress_image(input_image_path, output_image_path, optimal_k)


