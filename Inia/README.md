
## Testing the r.evolution module
* for description of the module see the [developer's site](https://github.com/baharmon/landscape_evolution)
* the source of the [script](baharmon/landscape_evolution/testing/dynamic_simulations.py) for running the simulations
# Workflow
(to preserve naming consistency and clear database structure on *fatra*)
`ssh jajezior@fatra.cnr.ncsu.edu -X`

#### copy the generic script
`cp Github/landscape_evolution/Inia/testing/dynamic_simulations_LakeWheeler.py Github/landscape_evolution/Inia/testing/name_of_the _simulation.py`
#### modify the script
use the script and modify the parameters according to the simulation

### Run the simulation
`grass-trunk`
* location: LW_landscape_evol
* mapset: PERMANENT

#### create a new github directory for storing the results
`mkdir Github/landscape_evolution/Inia/testing/name_of_the_simulation`
#### move the modified for that simulation script to thet folder
`mv Github/landscape_evolution/Inia/testing/name_of_the_simulation.py Github/landscape_evolution/Inia/testing/name_of_the_simulation/name_of_the_simulation.py`
#### move the rendering results to that folder
`mv LW_landscape_evol/rendering/ Github/landscape_evolution/Inia/testing/name_of_the_simulation`
#### rename the mapsets created in the location
* location: LW_landscape_evol
* name_of_the_simulation_flux
* name_of_the_simulation_erdep
* name_of_the_simulation_usped
* name_of_the_simulation_rusle

#### push the results into the Github
```
cd Github/landscape_evolution/
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



