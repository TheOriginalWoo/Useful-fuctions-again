<div align="center">

# Useful-Functions

</div>

A set of useful functions

## How to incoperate and set it up for my other projects
This goes over how you can setup this module with my other projects that depend on this one

1. Create a json file names **toolspath.json** in the same directory where the main.py of the other project is at.
2. In it, make a key value pair as follows,
```
"toolspath": <absolute path of tools.py of this project>
``` 


## Current functions

* [map_value](#1-map_value)
* [corrupt_values](#2-corrupt_pattern)
* [decorate_graph](#3-decorate_graph)
  

### 1. map_value

Equalant to Aruduino's map function.
  


### 2. corrupt_pattern

Takes a list of numbers, replaces randomly picked values of that list with random values(corrupt values)
and return the altered list.

#### Parameters
**original_pattern**: the pattern that should be corrupted   
**degree**          : the fraction of values of the list that should be corrupted  
**lower_bound**     : lowest value of a corrupted value could have  
**upper_bound**     : the highest value a corrupted value could have  

**return**: original list with the corrupted values  
  


### 3. decorate_graph

Decorate the given fig and ax to the following aesthetic.

![example_graph](imgs/Spring%20graph.png)

#### Parameters
**x_label** : Label of x axis  
**y_label** : Label of y axis  
**fig** :   Figure of the graph  
**ax** :    Ax object of the graph

**return**: None



