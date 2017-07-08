### Calculate travel time


#### Traveltime based on discharge from r.sim.water
r.slope.aspect elevation=midpines_lidar_DEM_2015@evol_lidar dx=dx dy=d
r.sim.water elevation=midpines_lidar_DEM_2015@evol_lidar dx=dx@evol_lidar dy=dy@evol_lidar depth=depth discharge=discharge

r.info map=discharge@evol_lidar
mean velocity= **2.19 m/s**

downhill segment of the modeling area (from the top down to the road) = **262 m** (straight line)

#### traveltime
distance / mean velocity = **119 s** = **2 min**

