---
layout: default
title:  Proposal
---

# {{ page.title }}

## Project Summary:
We will be attempting to generate voxelized 2d images taken from real life scenarios and translating them into 3-dimensional models to be generated in minsecraft. The algorithm will take utilize the ShapeNet dataset and will use the three dimensional data to create validation, training, and test data for the algorithm. Using PyTorch we will then generate voxelizations of a given 2-dimensional image and compare it to ground truth 3d voxelizations provided in the dataset to see how well the algorithm performs. The algorithm will then optimize its parameters and produce outputs for single images, where Blender, a tool for generating three dimensional images will be used to validate the output of our algorithm.

## AI / ML algorithms:
We anticipate using deep learning to detect shadows and contrast within images, and using PyTorch's CNN (Convolutional Neural Networks) in order to generate these voxelizations of these 2d images. 


## Evaluation plan:
We will be evaluating the model based on the time taken to teach the chicken as we plan to use a scoring method based on time. As time progresses the agent will lose its life due to hunger… unless it finds bread. When it finds bread the agent will eat and a given reward value will be attributed to the total score. Every move is exhausting in minecraft and will cost hunger. When the agent finds the chicken he will end its life and eat the chicken, exiting the maze and rewarding the agent with maximal points. Each action will decrease the overall points obtained, and certain actions will reap rewards as proposed above. 

We will be determining the total efficacy of the model through a series of tests by calculating the pixel difference and pixel density of the model by comparing the original image and the minecraft generated object. This score will essentially measure the algorithms ability generate standard XML in order to determine the shape of our object. Images will be color-graded and certain blocks will be pre-determined to identify certain colors. Our standards of solutions would hope to allow our model to produce acceptable outputs for multiple varieties of cars of various sizes. Furthermore, we hope that this method of scoring will contribute to the learning of the model, which would inherently increase its ability to generate more cars from real life images. As a sanity case, we should at least verify that the agent improves its accuracy as it progresses through multiple attempts. Our moonshot case is that the agent would eventually never fail to find the generate images that are inherently identical in color-grading, pixel-density and pixel difference to the given input.