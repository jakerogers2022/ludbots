# ludbots
CS 396 Artificial Life

# Assignment 8 "Evolved Body and Brain"

# OVERVIEW: For this assignment I created an evolved creature for locomotion.
The aspects being evolved are:
- The number of links in the body
- The direction of the joints
- The placement and orientation of the connections
- The placement and number of sensors
- The weighted connections in the brain

Video result
https://www.youtube.com/watch?v=Y-U4JQICveE


# Fitness function:
The fitness funtion used to evaluate the ability of the bots is the absolute value of the distance from the origin in the x, y plane.

![image](https://user-images.githubusercontent.com/71994929/221426053-0b7bc239-a616-4cff-a54f-e520d88a7fce.png)

# Evolution Method:
I switched the evolution method away from parallel hill climbing to a more pool based evolution method.
For this I evaluated all parents and then selected the top 4 to reproduce all the children.

100 Parents -> Top 4 selected -> 25 children each -> Evaluate Children -> Replace parents if children do better -> Repeat

# Findings:
Some interesting findings were:
- It generally evolved to be smaller robots which made sense since the brains were more likely to be effective with less neurons to train

# Run it yourself
- Clone repo
- Install packages
- Run search.py

# Sources: 
https://www.reddit.com/r/ludobots/
Pybullet


