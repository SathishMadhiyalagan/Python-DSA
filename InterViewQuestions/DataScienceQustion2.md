
### **Machine Learning Algorithms**

#### **Decision Tree**
1. What is a Decision Tree? How does it work?
2. How are splits determined in a Decision Tree?
3. What are the key parameters in building a Decision Tree?
4. How do you handle overfitting in Decision Trees?
5. Explain the difference between Gini Impurity and Entropy.
6. What is pruning, and why is it important in Decision Trees?

#### **Support Vector Machine (SVM)**
1. What is the objective of SVM?
2. Explain the concept of a hyperplane and support vectors.
3. What is the difference between a hard margin and a soft margin in SVM?
4. How do kernel functions work in SVM? Name a few commonly used kernel functions.
5. How would you handle imbalanced datasets when using SVM?
6. How does SVM perform in high-dimensional data spaces?

---

### **Deep Learning Algorithms**

#### **Convolutional Neural Networks (CNNs)**
1. What is a CNN, and how is it different from a traditional neural network?
2. Explain the roles of convolutional layers, pooling layers, and fully connected layers.
3. What are the differences between max pooling and average pooling?
4. How do stride and padding affect the output of a convolutional layer?
5. What is a receptive field in a CNN?
6. How would you apply CNNs in a real-world problem like image classification?

#### **LSTM (Long Short-Term Memory)**
1. What is an LSTM, and how does it differ from a traditional RNN?
2. Explain the components of an LSTM cell, such as forget gate, input gate, and output gate.
3. How do LSTMs handle the vanishing gradient problem?
4. Compare LSTM and GRU (Gated Recurrent Unit).
5. How would you use LSTMs for a time-series forecasting problem?
6. What are some real-world applications of LSTMs?

---

### **Gradient Descent**
1. What is Gradient Descent, and why is it used in optimization?
2. Explain the differences between batch gradient descent, stochastic gradient descent, and mini-batch gradient descent.
3. What is the role of the learning rate in gradient descent?
4. How can you avoid getting stuck in local minima during optimization?
5. What are exploding and vanishing gradients, and how can they be mitigated?
6. How do momentum and Adam optimizers improve gradient descent?

---

### **XGBoost**
1. What is XGBoost, and why is it popular in machine learning competitions?
2. Explain the difference between bagging and boosting.
3. What are the main hyperparameters in XGBoost, and how do they affect the model?
4. How does XGBoost handle missing data?
5. What is the role of regularization in XGBoost?
6. Compare XGBoost with other gradient boosting algorithms like LightGBM and CatBoost.

---

### **ROC Curve**
1. What is a ROC curve, and why is it used?
2. How do you calculate the Area Under the Curve (AUC)?
3. What does a high AUC-ROC score signify?
4. How does the ROC curve change with imbalanced datasets?
5. Compare ROC curves with Precision-Recall curves.
6. How would you interpret a ROC curve where the AUC is 0.5?

---

### **Large Language Models (LLMs)**
1. What are Large Language Models, and how are they trained?
2. Explain the architecture of a Transformer model used in LLMs.
3. How do LLMs handle tasks like text generation and summarization?
4. What is transfer learning, and how is it applied in LLMs?
5. What are the challenges in training large language models?
6. Compare GPT and BERT in terms of architecture and use cases.

---

### **Generative AI**
1. What is Generative AI, and how is it different from traditional AI?
2. Explain the architecture of a Generative Adversarial Network (GAN).
3. What are Variational Autoencoders (VAEs), and how do they work?
4. How are generative models used in applications like image synthesis or text generation?
5. What are some challenges associated with Generative AI models?
6. How do you evaluate the quality of outputs from a generative model?

---

### **Deep Learning Models**
1. What are the key components of a deep learning model?
2. How do activation functions like ReLU, sigmoid, and tanh work?
3. What are vanishing and exploding gradients in deep learning?
4. Compare feedforward neural networks and recurrent neural networks.
5. How do you select the number of layers and neurons in a deep learning model?
6. What is transfer learning, and how is it applied in deep learning?

---

### **Natural Language Processing (NLP)**
1. What is tokenization in NLP, and why is it important?
2. How does Word2Vec work, and what are the differences between CBOW and Skip-gram?
3. What are attention mechanisms in NLP?
4. Explain the concept of embeddings in NLP models.
5. How would you preprocess text data for NLP tasks?
6. Compare traditional NLP models with Transformer-based models.

---

### **Image Processing**
1. What are some common preprocessing techniques in image processing?
2. How does edge detection work, and what are some common algorithms for it?
3. Explain the differences between image classification and object detection.
4. What are the applications of histogram equalization in image processing?
5. How do convolutional filters work in image processing?
6. What are some challenges in processing high-resolution images?



### **What is a Decision Tree? How does it work?**
A **Decision Tree** is a supervised learning algorithm used for both classification and regression tasks. It models decisions based on input features by splitting data into branches based on conditions, ultimately leading to decision points (leaves). 

- **Working:** 
  1. The root node represents the entire dataset.
  2. The dataset is split recursively into subsets based on feature values that result in the best information gain (classification) or least mean squared error (regression).
  3. The process continues until a stopping criterion is met (e.g., maximum depth or a minimum number of samples per node).
  4. The leaves represent the final prediction (class or value).

---

### **How are splits determined in a Decision Tree?**
Splits are determined using a criterion that evaluates the quality of the split. The goal is to maximize homogeneity (classification) or minimize variance (regression). Common criteria include:

1. **Gini Impurity:** Measures the likelihood of misclassification if a random sample is classified based on the distribution in the node.
   \[
   Gini = 1 - \sum_{i=1}^{n} p_i^2
   \]
   where \( p_i \) is the proportion of class \( i \) samples in the node.

2. **Entropy (Information Gain):** Measures the reduction in entropy before and after a split.
   \[
   Information \, Gain = Entropy_{parent} - \sum_{children} \left( \frac{|child|}{|parent|} \cdot Entropy_{child} \right)
   \]

3. **Variance Reduction (for regression):** Measures the decrease in variance after the split:
   \[
   Variance \, Reduction = Variance_{parent} - \sum_{children} \left( \frac{|child|}{|parent|} \cdot Variance_{child} \right)
   \]

---

### **What are the key parameters in building a Decision Tree?**
1. **Criterion:** The function used to measure the quality of splits (e.g., `gini`, `entropy`, `mse`).
2. **Max Depth:** The maximum depth of the tree to control its size.
3. **Min Samples Split:** The minimum number of samples required to split an internal node.
4. **Min Samples Leaf:** The minimum number of samples required to be at a leaf node.
5. **Max Features:** The maximum number of features to consider when splitting a node.
6. **Max Leaf Nodes:** The maximum number of leaf nodes in the tree.
7. **Random State:** A seed to ensure reproducibility.

---

### **How do you handle overfitting in Decision Trees?**
Overfitting occurs when the tree becomes too complex and captures noise in the data. Techniques to handle it include:

1. **Pruning:** Remove unnecessary branches (post-pruning) or limit tree growth (pre-pruning) by setting parameters like max depth, min samples per split, etc.
2. **Minimum Samples:** Use `min_samples_split` and `min_samples_leaf` to ensure sufficient data in each split.
3. **Maximum Features:** Limit the number of features considered for splits.
4. **Ensemble Methods:** Use bagging (e.g., Random Forests) or boosting (e.g., XGBoost).
5. **Cross-Validation:** Validate performance on a separate dataset to ensure generalization.

---

### **Explain the difference between Gini Impurity and Entropy.**

| **Aspect**         | **Gini Impurity**                                         | **Entropy**                                              |
|---------------------|----------------------------------------------------------|----------------------------------------------------------|
| **Definition**      | Measures the likelihood of misclassification.            | Measures the impurity or randomness in the data.          |
| **Formula**         | \( 1 - \sum_{i=1}^{n} p_i^2 \)                          | \( -\sum_{i=1}^{n} p_i \log_2(p_i) \)                   |
| **Range**           | [0, 0.5] (binary classification)                        | [0, 1] (binary classification)                          |
| **Computation**     | Faster to compute.                                       | Slightly more computationally intensive.                |
| **Preference**      | Often preferred in decision tree implementations.        | Used when more focus on information gain is needed.      |

Both measures are used to decide splits, but Gini is computationally less expensive and often preferred in practice.

---

### **What is pruning, and why is it important in Decision Trees?**
**Pruning** is a technique used to simplify a Decision Tree by removing branches that have little importance or predictive power. It helps in reducing overfitting and improving generalization.

- **Types:**
  1. **Pre-pruning:** Stops the tree from growing beyond a certain point (e.g., setting max depth or minimum samples per split).
  2. **Post-pruning:** Trims branches after the tree has fully grown, usually based on a validation set.

- **Importance:**
  - Reduces model complexity.
  - Improves accuracy on unseen data.
  - Prevents overfitting by eliminating redundant splits.


