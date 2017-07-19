
## Testing the r.evolution module
for description of the module see the [developer's site](https://github.com/baharmon/landscape_evolution)
the source of the [script](baharmon/landscape_evolution/testing/dynamic_simulations.py) for running the simulations
# Workflow
(to preserve naming consistency and clear database structure on *fatra*)
### copy the generic script
`cp Github/landscape_evolution/Inia/testing/dynamic_simulations_LakeWheeler.py Github/landscape_evolution/Inia/testing/name_of_the _simulation.py`
### modify the script
use the script and modify the parameters according to the simulation

### create a new github directory for storing the results
`mkdir Github/landscape_evolution/Inia/testing/name_of_the_simulation`
### move the modified for that simulation script to thet folder
`mv Github/landscape_evolution/Inia/testing/name_of_the_simulation.py Github/landscape_evolution/Inia/testing/name_of_the_simulation/name_of_the_simulation.py`
### move the rendering results to that folder
`mv LW_landscape_evol/rendering/ Github/landscape_evolution/Inia/testing/name_of_the_simulation`



## using the script  


