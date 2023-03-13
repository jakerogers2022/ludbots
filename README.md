# ludbots
CS 396 Artificial Life

# Assignment 8 Final Project (Science)
# Hypothesis: The parallel hill climbing (PHC) method is a slower and less effective method of evolution than top k selection (TK) and parallel top k (PTK) selection, with top k selection being the fastest, but parallel top k selection being more effective long term. 

# Experiment
Utilize the three evolution algorithms (parallel hill climber, top k selection, and parallel top k selection) to evolve locomotion for a constant population size of 200, 50 generations, k value of 10, and for 10 trials each and compare which one is most effective at optimizing fitness. For a total of 300,000 simulated creatures.

# Evolution Algorithms
- Parallel hill climbing: This method performs hill climbing with 200 parents in parallel with one another. 
  200 Parents -> 200 Children -> For each child parent pair pick best one as next parent -> Repeat
  
- Top k selection: This method is more of a pool based method where the top performers each have 20 children and everyone competes against everyone
  200 Parents -> Top 10 selected -> 20 children each -> Evaluate Children -> Replace parents if children do better -> Repeat
  
- Parallel Top k selection: This method is similar to top k but is basically performing smaller population size top k with no cross over between sections
  10 Sections of 20 parents -> Top performer in each section selected -> Each section repopulated with children of top performer -> Repeat

# Evolution method
The aspects being evolved are:
- The number of links in the body
- The direction of the joints
- The placement and orientation of the connections
- The placement and number of sensors
- The weighted connections in the brain

The creature is generated using a tree like structure.
![image](https://user-images.githubusercontent.com/71994929/219985253-679fc2ae-9e22-400a-8149-31074bdc24b9.png)

The tree is generated recursively. Given a link it creates a random number of children links from it orthoganal to its surfaces, the lower the depth more likely it is to have children. The children links are connected via a joint with a random axis of rotation. Each link is randomly sized. Before children are added their absolute coordinates are checked to ensure they do not overlap with any existing links. Sensors are also randomly added to some links and their colors are green, non sensor links are blue.

#Example bodies (Link dimensions were set to constant of 1 to better illustrate the structure of the creatures)

![image](https://user-images.githubusercontent.com/71994929/219984596-b5018e4c-8165-41f3-bbaa-cbcd474611e7.png)
![image](https://user-images.githubusercontent.com/71994929/219984674-ba58ce83-8f07-4fed-b704-9db52cab1c14.png)

# Brains
The brains are generated by initializing random weighted connections between sensor containing links and motors in the joints.

# Fitness function
The fitness funtion used to evaluate the ability of the bots is the absolute value of the distance from the origin in the x, y plane.

![image](https://user-images.githubusercontent.com/71994929/221426053-0b7bc239-a616-4cff-a54f-e520d88a7fce.png)

# Results
![image](https://user-images.githubusercontent.com/71994929/224786653-cc20cd06-9d6d-4314-834b-1f61c5b7ee95.png)
![image](https://user-images.githubusercontent.com/71994929/224786709-5b68878f-ca64-44ce-aa13-ba01dc41d4a2.png)
![image](https://user-images.githubusercontent.com/71994929/224786771-8f3b67a7-e6b1-430e-b30d-b40498942e32.png)

# Analysis

# Conclusion

# Run it yourself
- Clone repo
- Install packages
- Run search.py

# Sources: https://www.reddit.com/r/ludobots/


