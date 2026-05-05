# Predict Frog Toxicity with Python and XGBoost

## Technologies Used
<p style='font-weight: bold'>
ONNX | Python | XGBoost | Scikit-learn
</p>

## Project Description

Poisonous or toxic organisms often present bold colorations and flashy patterns, which serve as a defense mechanism. The bold colors serve as an advertisement for their toxicity, shouting out “Don’t eat me!” to any potential predators. Although there’s not a lot of concrete research on the correlation between visual warning signals and animals’ toxicity, a research paper was published in The American Naturalist in 2011 that detailed how the color and brightness of a certain species of poison frogs are reliable indicators of their toxicity levels.

In this project, we’ll learn how to build gradient boosting machine learning models in Python by building a model that can predict a frog’s toxicity levels by its luminance.

We’ll start with using pandas to load and clean the data. Then, we’ll visualize it using seaborn and Matplotlib to gain a better understanding of the data and how we can use it to train the model. Next, we’ll train a baseline XGBoost model, perform simple optimizations, and analyze the performance. Afterward, we’ll conclude the project with the final step of saving the model using ONNX.