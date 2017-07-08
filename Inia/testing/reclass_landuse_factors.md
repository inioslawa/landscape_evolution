## Create raster maps for spatally variable parameters based on the landuse
parameters needed
* mannings
* runoff
* c_factor (RUSLE)

## Base raster
The landuse has beed digitazed based on the ortophoto (in the full vegatation season) `landuse@PERMANENT` location:`LW_landscape_evol`
## Landuse classification 
The digitized landuse has been grouped into landuse classes [NLCD 92 Land Cover Class Definitions](https://landcover.usgs.gov/classes.php)
```
1 = 71	grass
2 = 31	unpaved road
3 = 52	shrub 
4 thru 14 = 82	cultivated crops
15 = 32	gravel pit
```
## reclass for c_factor 
values for C factor based on B.Harmon (landcover_to_cfactor.txt)
```
31 = 0.8
52 = 0.2
71 = 0.005
82 = 0.5
```
## reclass for Mannings 
values for Mannings values based on B.Harmon (landcover_to_mannings.txt)
[Mannings reference table](http://www.spatialhydrology.net/index.php/JOSH/article/viewFile/84/83)
```
31 = 0.0113
52 = 0.4
71 = 0.368
82 = 0.325
```
values for Mannings values based on the paper [The role of mangroves in attenuating storm surges](https://sofia.usgs.gov/publications/papers/mang_storm_surges/cest.html)
```
31 = 0.090
32 = 0.040
52 = 0.050
71 = 0.034
82 = 0.037
```

[Mannings reference table](https://www.wcc.nrcs.usda.gov/ftpref/wntsc/H&H/HecRAS/NEDC/lectures/docs/Manning%92s%20n-values%20for%20Kansas%20Dam%20Breach%20Analyses%20-%20Adopted%20071216.pdf)
```
31 = 0.025
52 = 0.1
71 = 0.035
82 = 0.030
```


It should be noted that the Manning’s n values assigned to each LULC classification are not physically based (involving direct field measurements because 
Manning’s n is empirical in nature) and thus can be easily misinterpreted

## reclass for runoff 
values for runoff values based on B.Harmon (landcover_to_mannings.txt)
```
31 = 0.6
52 = 0.5
71 = 0.35
82 = 0.4
```
