# Vision Transformer for Image Classification
In this project, I use transfer learning to fine-tune a Vision Transformer (ViT) model for classifying images from the MNIST dataset in Python using the Transformers library. We’ll use the Matplotlib library to visualize our data and evaluate our model using the scikit-learn library

## Technologies Used
<p style='font-weight: bold'>
Python | Matplotlib | Torchvision | Hugging Face | Scikit-learn
</p>

## Project Description
Vision Transformers have revolutionized image classification by applying transformer architectures originally designed for natural language processing to computer vision tasks. Fine-tuning pretrained ViT models enables high-accuracy digit recognition and other classification tasks with less training data than building models from scratch.

In this project, I build a digit classification system using a pretrained Vision Transformer from Hugging Face and the MNIST dataset. I load and visualize image data using the Datasets library and Matplotlib, perform data preprocessing and data augmentation to improve model generalization, then split the data into train, validation, and test sets. Using the Transformers library, I download a pretrained ViT model, configure it for our classification task, and fine-tune it on digit images with custom training arguments and metrics.

I set up a Trainer object for managing the training loop, evaluate baseline performance before training, and monitor progress through TensorBoard visualization. After training, I assess the fine-tuned model using F1 score metrics from scikit-learn, generate a confusion matrix to analyze classification errors, and implement an inference pipeline for making predictions on new images. By the end, you'll have hands-on experience with Vision Transformer architecture, Hugging Face Transformers, transfer learning, model fine-tuning, and deep learning evaluation applicable to any computer vision or image recognition project.