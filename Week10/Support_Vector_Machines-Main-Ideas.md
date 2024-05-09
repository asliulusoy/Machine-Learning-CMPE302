# Support Vector Machines 1- Main Ideas

This is a summary note based on the information I obtained from [Support Vector Machines - StatQuest with Josh Starmer](https://www.youtube.com/watch?v=efR1C6CvhmE)

## Maximal Margin Classifier
The shortest distance between the observations and the threshold is called the **margin**.
* when the threshold is halfway between the two observations, the **margin** is as large as it can be.
* when we use the threshold that gives us the largest **margin** to make classifications, we are using a **Maximal Margin Classifier**.

![MaximalMarginClassifier](https://github.com/asliulusoy/Machine-Learning-CMPE302/assets/132180090/6e265b5b-aeed-4e20-95cb-574343cf1bc3)

### Problem with the Maximal Margin Classifier

What if our training data looks like this?
![MaximalMarginClassifierProblem](https://github.com/asliulusoy/Machine-Learning-CMPE302/assets/132180090/9766e6c2-abe7-4f4f-908f-0af20a7d19b0)

If we use the same method here, the Maximum Margin Classifier would be very close to the right side of the observations.

![MaximalMarginClassifierClose](https://github.com/asliulusoy/Machine-Learning-CMPE302/assets/132180090/50018dcd-b66c-40f3-890a-ca2dbb9e1694)

If we had a new observation, we would classify it as red. However, as can be seen, the new observation is closer to the greens than to the reds. Therefore, classifying it as red would mean it is misclassified.

![MaximalMarginClassifierMisclassified](https://github.com/asliulusoy/Machine-Learning-CMPE302/assets/132180090/58cfb233-c8f5-4b73-8714-ef6d69637c1d)

### Conclusions
1. The Maximal Margin is found at the midpoint between the closest observations of different classes.
2. If the observations are not completely separated into distinct classes, that is, if there are outliers, Maximal Margin Classification is not the ideal method. This method is sensitive to outliers.

### What is the solution?
We should allow missclassifications.

## Soft Margins

When we allow missclassifications, the distance between the observations and the threshold is called a **Soft Margin**

Here, we allow for the misclassification of red. However, when we find a new observation like the one below, we correctly classify it as green.

![SoftMarginClassifications](https://github.com/asliulusoy/Machine-Learning-CMPE302/assets/132180090/579c94f8-b0a8-4325-b28b-692b22aa9f89)

This is an example of Bias/Variance tradeoff.
* Before we allowed missclassifications:
  - we picked a threshold that was very sensitive to the training data -> **low bias**
  - and it performed pporly when we got new data -> **high variance**
* After we allowed missclassifications:
  - we picked a threshold that was less sensitive to the training data --> **higher bias**
  - and it performed better when we got new data -> **low variance**

### Determining the Soft Margin

We use **Cross-Validation** to determine the soft margin that provides the best classification.

When we use a Soft Margin to determine the location of a threshold, we use a Soft Margin Classifier **(a.k.a. Support Vector Classifier)** to classify observations.

### Conclusions

1.The soft margin aims to classify the majority of the data correctly, even if it misclassifies some, by using the bias-variance tradeoff.
2. Data outside the margin are correctly classified, while those inside the margin may be misclassified.
3. Cross-validation is used to find the margin that yields the best results, and the soft margin classifier, also known as the support vector classifier, is used to determine the best threshold.


## Support Vector Classifier

* If the data has 2 properties then it would be 2-Dimensional.
  - Support Vector Classifier --> **Line**
* If the data has 3 properties then it would be 3-Dimensional.
  - Support Vector Classifier --> **Plane**
* If the data has 4 properties then it would be 4-Dimensional.
  - Support Vector Classifier --> **Hyperplane**

### Problem with the Support Vector Classifier

What if our training data looks like this?

![SupportVectorClassifierProblem](https://github.com/asliulusoy/Machine-Learning-CMPE302/assets/132180090/521881fb-dbd5-494f-b00f-7346280da344)

### What is the solution?
Support Vector Machines.

## Support Vector Machines
1. Start with data in a relatively low dimension
2. Move the data to higher dimention
3. Find a Support Vector Classifier that seperates the higher dimensional data into two groups.
