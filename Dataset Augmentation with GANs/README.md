# Dataset Augmentation with GANs

## Technologies Used
<p style='font-weight: bold'>
GANs | Python | PyTorch | Matplotlib
</p>

## Project Description
Generative Adversarial Networks (GANs) are deep neural networks trained to generate data distributions that are not identifiable as being synthetic. Two neural networks are trained in parallel to accomplish this–the generator and the discriminator. The discriminator's job is to identify a sample as either real or synthetic. The generator's job is to generate samples that fool the discriminator into classifying them as real.

Let's say we wanted to create a classification model on a dataset with a high class imbalance. When we trained the model, we got an excellent accuracy score, but when we made a confusion matrix, we saw that the model only predicted one class. Oversampling and undersampling are two solutions to the class imbalance problem. The former includes the minority class samples multiple times, which gives duplicate samples in the dataset. The latter drops a chunk of the majority class samples, which results in the loss of valuable data samples. To resolve these problems, we can use GANs to generate synthetic data for the minority class. This will ensure that there are no duplicate samples and that the classes are equally represented in the dataset. Any model trained on this data will, therefore, learn to predict both classes.

I create a GAN from scratch for dataset augmentation in this project. I use PyTorch for machine learning and Matplotlib for visualizations. Automatic differentiation will be used to train the deep learning models. The generator will be trained so that its generated distribution closely matches the actual distribution of the data.