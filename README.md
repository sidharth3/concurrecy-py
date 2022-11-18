# concurrency-py
concurrency and multithreading assignment in Python

The program is a simple service to release waypoints one at a time to a robot in a way that allows changes/cancellations. 

For example, the process could be:

* The robot begins with coordinates (2, 1). 
* We submit a trajectory with points ((4, 3), (5, 3)).
* The robot starts to move to (4, 3).
* We submit a trajectory with points ((3, 3), (5, 4)).
* The robot starts to move to (3, 3) instead of (4, 3).
* The robot arrives at (3, 3), and starts to move towards (5, 4).
* The robot receives a trajectory with points ().
* The robot stops.
