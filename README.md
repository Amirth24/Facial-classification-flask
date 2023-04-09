# Gallery Classifier

## Introduction

Gallery classifier is an application to classify images on one's gallery by recognizing people faces from the images using face embedding.

## What is Face Embedding?

Within the field of computer vision, facial recognition is an area of research and development which deals with giving machines the ability to recognize and verify human faces.  

Face embeddings are 128-d(128-dimensional) vectors pertaining to facial features and are similar to the same person. For example, two face embeddings of my face would be closer to each other in a Euclidean space, compared to a face embedding of your face.

![Illustration for facial Embedding](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmMkIRe4rOGW79F4OH8JkzcrPiqiJQL_s9SYbK8ltx_94ZFR_6dLNdthEeJHBHwjJwFlI&usqp=CAU)

By creating face embeddings you are converting a face image into numerical data. That data is then represented as a vector in a latent semantic space. The closer the embeddings are to each other in the latent space, the more likely they are of the same person.

![Clustering using face embeddings](https://www.google.com/imgres?imgurl=https%3A%2F%2Fmiro.medium.com%2Fv2%2Fresize%3Afit%3A1370%2F0*34kdbSVfOHQNPZuT.png&tbnid=sB_fXZcqZamcwM&vet=10CBYQxiAoB2oXChMIsLicifqc_gIVAAAAAB0AAAAAEAY..i&imgrefurl=https%3A%2F%2Ftechmusings.optisolbusiness.com%2Fface-recognition-with-facenet-b6ba474b5180&docid=VQoKMGilEMwmUM&w=685&h=594&itg=1&q=face%20embedding&client=firefox-b-d&ved=0CBYQxiAoB2oXChMIsLicifqc_gIVAAAAAB0AAAAAEAY)