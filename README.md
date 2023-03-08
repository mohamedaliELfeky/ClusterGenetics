# DBSCAN-GA: Maximizing Clustering Performance with Genetics Algorithm


This project is a genetics algorithm that optimizes DBscan parameters `eps` and `min_samples`. The algorithm was built from scratch using Python and deployed using Flask and Plotly Dash.

## Requirements
The following modules are required to run this project:

- Python 3.8 or later
- Scikit-learn (sklearn)
- Dash
- Plotly

## Project Overview

DBscan is a density-based clustering algorithm that requires two parameters: `eps` and `min_samples`. The objective of this project is to find the optimal values for these parameters using a genetics algorithm.

The genetics algorithm works by starting with a population of randomly generated solutions, which are essentially different combinations of `eps` and `min_samples` values. The algorithm then evaluates each solution by running DBscan on a given dataset and calculating the corresponding silhouette score. The top solutions are then selected to "mate" and produce a new generation of solutions with slight variations of their parent solutions. The process is repeated for several generations until an optimal solution is found.

The project was implemented entirely from scratch, without the use of pre-existing libraries for genetics algorithms or parameter optimization.


## Project Structure
The project is divided into three main components:

1- Genetics Algorithm: This component contains the code for the genetics algorithm, including the initialization of the population, the evaluation of solutions, the selection of top solutions, and the creation of new generations. The genetics algorithm code is implemented in the `Genatics_hyperprameter_tuning.py` file.

2- Web Application: This component contains the code for the Flask and Plotly Dash web application that allows users to interact with the genetics algorithm. The web application allows users to select range of values to get the best of them, and view the results of the optimization. The web application code is implemented in the `clustring_dashboard.py` file.

3- Helper Function to organize code to make it easy to be read



## Deployment
The project is deployed using Flask and Plotly Dash. To run the application locally, follow these steps:


1- Clone the repository
2- Install the required packages
3- Start the Flask server: python clustring_dashboard.py
Open a web browser and go to http://localhost:8050



## Conclusion
The genetics algorithm for optimizing DBscan parameters `eps` and `min_samples` provides a flexible and customizable way to find the optimal parameters for any given dataset. The implementation from scratch provides a deep understanding of the underlying algorithm and allows for customization and extension as needed. The deployment using Flask and Plotly Dash provides a user-friendly interface for interacting with the algorithm and visualizing the results.

![image](https://user-images.githubusercontent.com/48560237/223807351-aa9d30d9-ebce-41c4-8f57-83ffe1c34064.png)


![image](https://user-images.githubusercontent.com/48560237/223807288-21f79c3a-515f-40a0-8854-10e24814d4c4.png)
