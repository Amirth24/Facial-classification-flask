# Gallery Classifier

## Introduction

Gallery classifier is an application to classify images on one's gallery by recognizing people faces from the images using face embedding.

## What is Face Embedding?

Within the field of computer vision, facial recognition is an area of research and development which deals with giving machines the ability to recognize and verify human faces.  

Face embeddings are 128-d(128-dimensional) vectors pertaining to facial features and are similar to the same person. For example, two face embeddings of my face would be closer to each other in a Euclidean space, compared to a face embedding of your face.

![Illustration for facial recognition](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*yfIa0EcBR01se2vp.png)

By creating face embeddings you are converting a face image into numerical data. That data is then represented as a vector in a latent semantic space. The closer the embeddings are to each other in the latent space, the more likely they are of the same person.

