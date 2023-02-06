# ludbots
CS 396 Artificial Life

Assignment 5 "The Nped"

OVERVIEW: For this assignment I created a milliped like creature that evolved to walk.
The aspects being evolved are:
- Length of the body
- Number of legs on the left side
- Number of legs on the right side
- The weights of the neurons connecting the sensors to the motors

Eitness function:
The fitness funtion used to evaluate the ability of the bots is the absolute value of the distance from the origin in the y direction.

Evolution Method:
I switched the evolution method away from parallel hill climbing to a more pool based evolution method.
For this I evaluated all parents and then selected the top 4 to reproduce all the children.

40 Parents -> Top 4 selected -> 10 children each -> Evaluate Children -> Replace parents if children do better -> Repeat

Findings:
Some interesting findings were:
- It generally evolved to have the same number of legs on the left and right side
- It sometimes evolved a walking gait you may expect whereas other time it developed a more pronking gait

Sources: https://www.reddit.com/r/ludobots/


