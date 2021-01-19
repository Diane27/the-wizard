---
layout: default
title:  Proposal
---

# {{ page.title }}

## Project Summary:
We will be attempting to navigate through a Minecraft-generated maze in order to find a chicken, which will be randomly placed at an opposite end of the maze. The algorithm will take as input an image of a maze, which it will then replicate in a Minecraft world. It will then place the agent and the chicken (the target), and let the chicken move naturally as per the laws of Minecraft. Our AI will guide the agent through the maze, using both visual and audio cues to influence direction. As our agent moves, it will continuously lose hunger, unless it can find pieces of bread which have been uniformly distributed throughout the maze. Bread, however, only provides minimal satiation. The agent will continue its hunt until it either finds and kills the chicken (win), or dies from hunger (loss). The algorithm will then output a cumulative reward corresponding to the outcome and time taken by the agent.

## AI / ML algorithms:
We anticipate using deep learning to detect paths and mobs (NPC’s) within images, and testing different models from Djikstra’s algorithm to reinforcement learning for navigation through the maze, in which we will be using image recognition to determine what's a chicken and what's not.

## Evaluation plan:
We will be evaluating the model based on the time taken to teach the chicken as we plan to use a scoring method based on time. As time progresses the agent will lose its life due to hunger… unless it finds bread. When it finds bread the agent will eat and a given reward value will be attributed to the total score. Every move is exhausting in minecraft and will cost hunger. When the agent finds the chicken he will end its life and eat the chicken, exiting the maze and rewarding the agent with maximal points. Each action will decrease the overall points obtained, and certain actions will reap rewards as proposed above. 

We will be determining the total efficacy of the model through a series of tests by calculating the time taken and average score of the model over a period of time. This score will essentially measure the agents ability to find bread and chase the chicken throughout the generated mazes. Our standards of solutions would hope to set our model in multiple varieties of mazes in the same size, in an attempt to standardize the results and create consistency within our tests. Furthermore, we hope that this method of scoring will contribute to the learning of the model, which would inherently increase its ability within the world to solve the task at hand. As a sanity case, we should at least verify that the agent improves its cumulative reward as it progresses through multiple attempts. Our moonshot case is that the agent would eventually never fail to find the chicken, regardless of starting agent, chicken, and bread locations.