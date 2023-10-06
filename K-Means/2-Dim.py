import random
import math
import matplotlib.pyplot as plt


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def initialize_centers(k, min_value, max_value):
    centers = [(random.uniform(min_value, max_value), random.uniform(min_value, max_value)) for _ in range(k)]
    return centers


def assign_to_clusters(points, centers):
    clusters = {i: [] for i in range(len(centers))}

    for point in points:
        min_distance = float('inf')
        cluster_index = None

        for i, center in enumerate(centers):
            distance = euclidean_distance(point, center)
            if distance < min_distance:
                min_distance = distance
                cluster_index = i

        clusters[cluster_index].append(point)

    return clusters


def k_means(points, k, max_iterations=100):
    centers = initialize_centers(k, 0, 100)

    for _ in range(max_iterations):
        clusters = assign_to_clusters(points, centers)

        new_centers = []
        for cluster_points in clusters.values():
            if cluster_points:
                num_points = len(cluster_points)
                x_sum = sum(point[0] for point in cluster_points)
                y_sum = sum(point[1] for point in cluster_points)
                new_centers.append((x_sum / num_points, y_sum / num_points))
            else:
                new_centers.append(centers[len(new_centers)])  # Reuse old center if no points in cluster

        if new_centers == centers:
            break

        centers = new_centers

    return clusters, centers


def calculate_inertia(points, centers, clusters):
    inertia = 0
    for i, cluster_points in clusters.items():
        for point in cluster_points:
            inertia += euclidean_distance(point, centers[i]) ** 2
    return inertia


if __name__ == "__main__":
    # Generate some random 2D points
    random.seed(0)
    points = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(100)]

    # Determine the optimal number of clusters (K) using the elbow method
    max_k = 10
    inertias = []
    for k in range(1, max_k + 1):
        clusters, centers = k_means(points, k)
        inertia = calculate_inertia(points, centers, clusters)
        inertias.append(inertia)

    # Plot the elbow graph
    plt.figure(figsize=(8, 4))
    plt.plot(range(1, max_k + 1), inertias, marker='o')
    plt.title('Elbow Method for Optimal K')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('Inertia')
    plt.show()


