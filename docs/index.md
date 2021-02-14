---
layout: default
title:  Home
---

### Inspiration
This project was inspired by the Japanese anime, Naruto. What we're trying to achieve in our project is to recreate some of the hand gestures performed in Naruto, therefore turning our agent into a powerful Naruto character.

![Naruto](assets/naruto.png)

### Overview

We want to use some of the popular hand signs (see below) and be able to translate them into attacks in minecraft and even summon animals in Minecraft
![Hand Gestures](assets/hand-signs.jpg)

The Wizard will take in live camera input, utilize deep learning to classify that input as one of the 12 different Naruto hand signs, and instruct the agent to execute a corresponding action. Our final goal for this project is to build a model that can accurately classify not only static gestures, but continuous hand movements as well.
{% include images.html img1="assets/hand_capture.png" img2="assets/hand-recognition.png" img3="assets/minecraft-action.png" description1="1. Hand capture through webcam" description2="2. Hand recognition by our model" description3="3. Action performed in Minecraft"%}
