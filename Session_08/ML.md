# 🤖 Lecture 12: Introduction to Machine Learning

This lecture provides a conceptual overview of **Machine Learning (ML)**, one of the most significant areas in modern computer science. The aim is not to teach ML in depth, but to introduce key ideas and spark curiosity for further study.

---

## 🎯 What is Machine Learning?

> "Machine learning is the field of study that gives computers the ability to learn without being explicitly programmed." – *Arthur Samuel*

### 🧠 Human Learning Analogy
| Human Learning     | Machine Learning Equivalent         |
|--------------------|--------------------------------------|
| Memorization       | Storing exact examples               |
| Generalization     | Learning patterns to make predictions |

ML aims to **generalize** from observed examples (training data) to make predictions about **unseen data** (test data).

---


## 🔧 Key Components of a Machine Learning System

1. **Feature Vector**:  
   - A list of measurable attributes for an instance.  
   - Example: `[age=20, score=85, studied_hours=10]`
   - This is a vector of numbers → enables mathematical processing.

2. **Distance Metric**:  
   - Quantifies similarity between feature vectors.  
   - Common types:
     - **Euclidean Distance**: Straight-line (Pythagorean)
     - **Manhattan Distance**: Grid-based, like navigating a city

3. **Objective Function**:  
   - What the algorithm tries to optimize (e.g., minimizing mean squared error or clustering variability)

4. **Optimization Algorithm**:  
   - Learns the model by adjusting parameters to minimize the objective

5. **Evaluation Method**:  
   - Assesses model quality and tunes parameters
   - Helps prevent underfitting and overfitting

---

## 🧠 Supervised Learning

Supervised learning uses **labeled data**: each feature vector has a corresponding output value (label).

### Two Types:

| Type           | Description                        | Example                          |
|----------------|------------------------------------|----------------------------------|
| **Regression** | Predicts a continuous value        | Predicting house price           |
| **Classification** | Predicts a category (label)   | Spam detection, disease diagnosis |

### 🧪 Example: Classifying Animals as Reptiles

- Each animal is represented by a **feature vector** (e.g., has legs, lays eggs, number of legs)
- Labels indicate reptile (`1`) or not (`0`)
- **Distance matrix** is used to find which animals are similar

<p align="center">
  <img src="Images/KNN.png" alt="Description" width="400"/>
</p
 

#### 📌 Nearest Neighbor (kNN) Classification

- **1-NN**: Assign label of the single closest training point
- **k-NN** (e.g., k=3): Take the **majority vote** among the k nearest neighbors

### ✅ Pros and Cons of kNN

| Pros                                       | Cons                                      |
|--------------------------------------------|-------------------------------------------|
| Simple, no training required               | Memory-intensive                          |
| Easy to explain and justify decisions      | Slow predictions; no interpretable model  |

---

## ⚠️ Feature Scaling

- Unequal value ranges can **distort distance calculations**
- Example: `number_of_legs` (range 0–4) dominates binary features (0/1)

<p align="center">
  <img src="Images/KNN3.png" alt="Description" width="400"/>
</p
 
- **Fixes**:
  - **Convert to binary** (e.g., has legs = 0/1)
  - **Z-scaling**: mean = 0, std = 1
  - **Min-max scaling**: values scaled to [0, 1]

---

## 🔍 Unsupervised Learning

No labels are provided. The goal is to **discover hidden structure** in the data.

### 🔹 Clustering

- Group similar examples based on feature vectors and distance metrics
- No "correct" clustering → depends on features and metric used

### 🎯 Objective Function: Dissimilarity

- Similar to variance, but **not normalized**
- Penalizes large incoherent clusters more heavily

#### ❗ Trivial Solution Risk:
- Putting each example in its own cluster gives perfect (but useless) score
- Add constraints:
  - Maximum number of clusters (`k`)
  - Minimum distance between clusters

---

## 🔢 k-Means Clustering Algorithm

A popular greedy clustering method that minimizes within-cluster dissimilarity.

### 📘 Algorithm Steps:

```plaintext
1. Choose k random points as initial centroids
2. Assign each point to the nearest centroid (form clusters)
3. Recompute centroids by averaging all points in a cluster
4. Repeat steps 2–3 until centroids no longer move (convergence)
