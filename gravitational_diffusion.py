"""gravitational diffusion"""

# gravitational diffusion coefficient (m^2/s)
grav_diffusion = 0.2 # m^2/s

# assign variables
dxx = 'dxx'
dyy = 'dyy'
grow_dxx = 'grow_dxx'
grow_dyy = 'grow_dyy'
settled_elevation = 'settled_elevation'

# compute second order partial derivatives
gscript.run_command('r.slope.aspect',
    elevation=evolved_elevation,
    dxx=dxx,
    dyy=dyy,
    overwrite=True)

# grow border to fix edge effects of moving window computations
gscript.run_command('r.grow.distance',
    input=dxx,
    value=grow_dxx,
    overwrite=True)
dxx = grow_dxx
gscript.run_command('r.grow.distance',
    input=dyy,
    value=grow_dyy,
    overwrite=True)
dyy = grow_dyy

# compute divergence from the sum of the second order derivatives of elevation
gscript.run_command('r.mapcalc',
    expression="{divergence} = {dxx}+{dyy}}".format(divergence=divergence,
        dxx=dxx,
        dyy=dyy),
    overwrite=True)

# compute settling caused by gravitational diffusion
"""change in elevation (m) = elevation (m) - sediment mass density (kg/m^3) * gravitational diffusion coefficient (m^2/s) * 0.5 * divergence"""
gscript.run_command('r.mapcalc',
    expression="{settled_elevation} = {evolved_elevation}-{density}*{grav_diffusion}*0.5*{divergence}".format(settled_elevation=settled_elevation,
        evolved_elevation=evolved_elevation,
        density=self.density,
        grav_diffusion=grav_diffusion,
        divergence=divergence),
    overwrite=True)

# update elevation
evolved_elevation = settled_elevation
gscript.run_command('r.colors',
            map=evolved_elevation,
            color='elevation')

# remove temporary maps

#dxx,dyy,grow_dxx,grow_dyy,settled_elevation
