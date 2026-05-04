# Detect a Writer’s Fingerprints Using Machine Learning

## Technologies Used
<p style='font-weight: bold'>
NLTK | NumPy | Python | Pandas | Matplotlib
</p>

## Project Description

In this project, I explore authorship attribution by analyzing the unique traits in an author’s written works. Our dataset comprises a collection of songs from well-known songwriters and includes song titles, lyrics, and author information. I develop a model that will accurately attribute authorship to a given text. Such a model can have applications in various fields, such as plagiarism detection, literary analysis, and authorship attribution.

To get started, I load the dataset and language model that will help us in processing the text. Then, I preprocess the text to minimize noise and extract linguistic features that can help in identifying an author, for example, word length distribution, word frequency, and word co-occurrences. Next, I learn to create a training corpus, and use it to attribute authorship to a text using Burrows's Delta.