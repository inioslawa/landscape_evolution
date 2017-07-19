
## Testing the r.evolution module
* for description of the module see the [developer's site](https://github.com/baharmon/landscape_evolution)
* the source of the [script](baharmon/landscape_evolution/testing/dynamic_simulations.py) for running the simulations
# Workflow
(to preserve naming consistency and clear database structure on *fatra*)

### Local

#### create a new folder for that simulation
```
cd /media/jajezior/540ECB340ECB0E44/Github/landscape_evolution/Inia/testing
mkdir name_of_the_simulation
```

#### copy the generic script to the newly created folder
`cp dynamic_simulations_LakeWheeler.py name_of_the_simulation/name_of_the_simulation.py`

#### push the changes
```
cd /media/jajezior/540ECB340ECB0E44/Github/landscape_evolution
git pull
git add --all
git commit -am 'new simulation'
git push
```
### Githhub 
#### modify the script
use the script and modify the parameters according to the simulation

 https://github.com/inioslawa/landscape_evolution/Inia/testing/ 
 name_of_the_simulation/name_of_the_simulation.py

### Run the simulation
`ssh jajezior@fatra.cnr.ncsu.edu -X`
#### pull the results from the Github
```
cd Github/landscape_evolution/
git pull
```
#### Launch grass
`grass-trunk`
* location: LW_landscape_evol
* mapset: PERMANENT

#### load the script from the location
Github/landscape_evolution/Inia/testing/name_of_the_simulation/name_of_the_simulation.py

#### move the rendering results to the results folder
`mv LW_landscape_evol/rendering/ Github/landscape_evolution/Inia/testing/name_of_the_simulation`
#### rename the mapsets created in the location
* location: LW_landscape_evol
* name_of_the_simulation_flux
* name_of_the_simulation_erdep
* name_of_the_simulation_usped
* name_of_the_simulation_rusle

#### push the results
```
cd Github/landscape_evolution/
git pull
git add --all
git commit -am 'adding the simulation results'
git push
```
#### pull the changes into the local computer
(terminal on the local computer)
```
cd /media/jajezior/540ECB340ECB0E44/Github/landscape_evolution
git pull
```



