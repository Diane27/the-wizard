---
layout: default
title:  Status
---

# {{ page.title }}

## Project Summary:
The Wizard attempts to control a Malmo agent through Naruto hand signs. In Naruto, there are several hand signs (tiger, bird, dog, etc.) that correspond to a certain spell. The Wizard will take in live camera input, utilize deep learning to classify that input as one of the 12 different Naruto hand signs, and instruct the agent to execute a corresponding action. Our final goal for this project is to build a model that can accurately classify not only static gestures, but continuous hand movements as well. However, for this first checkpoint, our model is only equipped to classify static images. 

## Approach:
Throughout the development of The Wizard, we wanted to create a functional deep learning model with minimal overhead and the ease of simple design. Our output 

## Evaluation:

## Remaining Goals / Challenges:
With regards to our static image classification model, there are a few basic remaining challenges. Firstly, we did not get to implement all of the Malmo functionality required to truly execute the Naruto spells. By the final project, we hope to control the agent in a way that lives up to the name of our project. We do not anticipate this will be particularly difficult, and will simply require some additional effort on the Malmo side.

Secondly, while our model is highly accurate with normal lighting and a clear background, different lighting conditions and noisier backgrounds give the model some difficulty. There are a couple different ways we can combat this problem, starting with collecting more data. Thus far in this project, we have trained the model using data that we have generated. However, most of this image data was captured around roughly the same time, so there is not much variance in the images. Gathering more data, whether it be through online sources, or by making more ourselves, will help the model make its classifications. Thus far, we have already seen major improvements in accuracy after feeding in more training data. Another way we can solve this problem is by utilizing better image segmentation techniques when isolating the user’s hands from the background. We don’t anticipate this to be very difficult, as opencv offers a variety of functions that can help with this problem. For example, we can attempt to isolate the hands through edge detection in addition to our existing image segmentation techniques.

Our biggest remaining challenge will be to adjust our model to classify continuous motions. This remaining portion of our project presents issues on multiple ends. We will need a new data set consisting of GIF or video-like content in order to train our model. While generating data may take an immense amount of time, it can be accomplished through our collective efforts. 

We will also need a way of parsing this new data format, and will need to modify our classification process in order to fit the new data type. In terms of the magnitude of changes that we must perform, this seems like a problematic task. However, we have some ideas as to how we can attempt to overcome these difficulties. If we treat a video as a series of frames, we can attempt to split up the video into chunks, and sample a frame from each chunk. Then, we can retrain our model to look for different image patterns at different times. Finally, we can use this retrained model to classify each section, and then average across the different assigned labels to classify the entire clip. While this may seem like a somewhat rudimentary approach, it is worth a try as we can use parts of our existing model to do so. However, if this fails, we can look into some of the existing research into this area and try to follow their examples.

## Resources used:
