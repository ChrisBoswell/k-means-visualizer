# K Means Visualizer
Simple 2D visualization for the k-means clustering algorithm

![K-Means Visualizer Gif](https://raw.githubusercontent.com/ChrisBoswell/k-means-visualizer/main/content/k_means_visualizer.gif)

# What is the K-Means algorithm?
K-Means is an iterative, unsupervised machine learning algorithm that clusters data into groups. The algorithm works by initially grouping the data points to randomly placed centroids, and then iteratively improving the error. Assignments are chosen based on the closest centroid. Once all data points are assigned, the centroid then moves to the new center of all the data points in the grouping. This process is repeated until no further improvements to the average distance can be made. A more in-depth explanation can be found [here](https://en.wikipedia.org/wiki/K-means_clustering)


Here is an example showing the k-means algorithm over 5 iterations with 2 clusters

![](https://stanford.edu/~cpiech/cs221/img/kmeansViz.png)


## This visualizer 
Normally, the k-means algorithm uses random starting centroids. This visualizer, however, starts the centroids in a pseudo-random area in the top left of the screen, creating a clearer animation of the centroids moving toward the optimal position. This impacts the clusters' final accuracy but helps the visualization, which is the whole point!

The error in a clustering algorithm is associated with the average distance of each data point to its assigned centroid. This error is printed in the top left corner of the pygame screen. You will see how the error monotonically decreases after each iteration, eventually settling (called convergence) at a local optimum. 

## Setup

Run `pip install pygame`

Run `python main.py`

## Usage

You will be prompted to choose the number of data points, the number of clusters, and then the speed at which you would like the algorithm to progress. 

![](https://raw.githubusercontent.com/ChrisBoswell/k-means-visualizer/main/content/k_means_visual_inputs.png)
![K-Means Visualizer Gif](https://raw.githubusercontent.com/ChrisBoswell/k-means-visualizer/main/content/k_means_visualizer.gif)
