# Speech Recognition with Whisper

## Technologies Used
<p style='font-weight: bold'>
Python | OpenAI | PyTorch | Hugging Face
</p>

## Project Description
Automatic speech recognition is the task of transcribing speech from audio. Current speech recognition models only perform well on in-distribution data (data similar to that on which the model was trained). OpenAI introduced the Whisper model in September 2022. The model has been trained on 680,000 Hrs of speech and is very robust to out-of-distribution data. The data comprises transcribed speech in English plus 96 other languages. The model has also been trained on the task of translating transcriptions, where the speech is translated from these 96 other languages and transcribed in English.

In this project, we will start by loading the whisper model from Hugging Face Hub. We will compute the word error rate (WER) metric for the default checkpoint, fine-tune it on a small subset of the “Librispeech” dataset, and then compute its WER again on the test set.