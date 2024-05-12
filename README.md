![K-Means Visualizer Gif](https://raw.githubusercontent.com/ChrisBoswell/k-means-visualizer/main/content/k_means_visualizer.gif)
# K Means Visualizer
Simple 2D visualization for the k-means clustering algorithm


# What is the K-Means algorithm?
K-Means is an unsupervised machine learning algorithm used to cluster data into groups. The algorithm works by initally randomly grouping the data points, then iteratively improving the error. Each grouping is made by assigning the data points to the closest centroid. Once all data points are assigned, the centroid then moves to the center of all the data points in the grouping. This process is repeated until no further improvements to the average distance can be made. A more in depth explaination can be found [here](https://en.wikipedia.org/wiki/K-means_clustering)


Here is an example showing the k-means algorithm over 5 iterations

![](https://stanford.edu/~cpiech/cs221/img/kmeansViz.png)


## This visualizer 
Normally, the k-means algorithm uses random starting centroids. This visualizer, however, starts the centroids in a pseudo
random area in the top left of the screen, creating a more clear animation of the centroids moving towards the optimal position. This does impact the final accuracy of the clusters but helps the visualization, which is the whole point!

The error in a clustering algorithm is associated with the average distance of each data point to its assigned centroid. This error is printed in the top left corner of the pygame screen. You will be able to see how the error monotonically decreases after each iteration, eventually settling (called convergence) at a local optima. 

## Setup

Run `pip install pygame`

Run `python main.py`

## Usage

You will be prompted to choose the number of data points, number of clusters and then the speed at which you would like the algorithm to progess. 

![](https://raw.githubusercontent.com/ChrisBoswell/k-means-visualizer/main/content/k_means_visual_inputs.png)
![K-Means Visualizer Gif](https://raw.githubusercontent.com/ChrisBoswell/k-means-visualizer/main/content/k_means_visualizer.gif)
