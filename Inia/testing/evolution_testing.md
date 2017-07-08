---------------------------
# r.evolution testing
---------------------------
**environment**
FATRA
location: LakeWheeler
mapset: evol
## set working directory
Working directory changed to:"/home/jajezior/evol_test" 
## set the region
g.region n=219657.343931 s=219320.143864 e=637072.65134968 w=636731.851429 res=0.3
----------------------------
## copy the elevtion raster from PERMANENT
	g.copy raster=2015_06_patch@PERMANENT,hydroDSM_2015_06_20_notrees

## r.evolution with default values 
	r.evolution elevation=hydroDSM_2015_06_20_notrees@evol runs=event mode=simwe_mode rain_intensity=30 rain_duration=40 mannings_value=0.15 start=2015-06-20 00:00:00 rain_interval=2 threads=8 elevation_timeseries=elevation_timeseries

