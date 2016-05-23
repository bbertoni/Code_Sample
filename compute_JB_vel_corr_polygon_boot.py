# This python code calculates a bootstrapped version of the velocity correlation function (psi1)
# defined by eqn. 1a in Gorski et al. (http://adsabs.harvard.edu/full/1989ApJ...344....1G) on one
# of the simulated halos from the 11 Johnston and Bullock simulations (available: 
# http://galaxia.sourceforge.net/ http://user.astro.columbia.edu/~kvj/halos/ ).  

# This code ideally will be run many times ~1000s for each Johnston and Bullock halo simulation
# to generate many bootstrapped halo samples, so that we can get an idea of the scatter in the
# velocity correlation function by calculating averages and standard errors of the bootstrapped
# samples.

# This code works with 5 inputs:
#
# 1. "halo", a string labelling the halo simulation data.  This data is not simply the stellar
# data obtained from the Johnston and Bullock website, but it has already been processed such
# that its footprint matches the BOSS footprint (this was accomplished using the polygon file
# boss_geometry_2014_05_28.ply from https://data.sdss.org/sas/dr12/boss/lss/geometry/ and the
# mangle software from http://space.mit.edu/~molly/mangle/ .)  The processed data also has had
# the latitude cut |b| > 30 deg, and has had random Gaussian line of sight velocity errors (mean
# 0 km/s and sigma = 30 km/s) and 15% random distance errors added.  This file contains 7 columns
# describing the stars in the halo: ra [deg], dec [deg], x position coordinate [kpc] (relative to
# the sun), y position coordinate [kpc] (relative to the sun), z position coordinate [kpc]
# (relative to the sun), distance from the sun [kpc], and the velocity along the line of sight to
# the sun [km/s].
#
# 2. "innerr", a float which picks the innermost distance from the sun.  (Note this code 
# calculates the correlation function within a shell defined by "innerr" and "outerr".)
#
# 3. "outerr", a float which picks the outermost distance from the sun.  (Note this code 
# calculates the correlation function within a shell defined by "innerr" and "outerr".)
#
# 4. "bins", an integer which determines how many 'separation' points are calculated for the 
# velocity correlation function within the shell.
#
# 5. "seed", an integer which will be used to set the seed for a random sampling of points from
# the input data set to generate a bootstrapped sample.

###############################################################################################

from numpy import array,zeros,dot,arange,sqrt,random
import sys

###############################################################################################

# get the inputs
halo = str(sys.argv[1]) # halo simulation label
innerr = float(sys.argv[2]) # in kpc
outerr = float(sys.argv[3]) # in kpc
bins = float(sys.argv[4])
seed = int(sys.argv[5])

###############################################################################################

# import the data
infile = open("/home/bbertoni/BullockJohnston/"+halo+"_boot/"+halo+"_final.dat",'r')

xpos = list()
ypos = list()
zpos = list()
dist = list()
vLOS = list()

for line in infile:
    vals = line.split()
    xpos.append(float(vals[2]))
    ypos.append(float(vals[3]))
    zpos.append(float(vals[4]))
    dist.append(float(vals[5]))
    vLOS.append(float(vals[6]))
infile.close()

xpos = array(xpos)
ypos = array(ypos)
zpos = array(zpos)
dist = array(dist)
vLOS = array(vLOS)

###############################################################################################

# put an additional cut on the data, restricting |vLOS| < 600 km/s, to remove outliers that 
# could make the velocity correlation function are to interpret.
vals = abs(vLOS) < 600

xpos = xpos[vals]
ypos = ypos[vals]
zpos = zpos[vals]
dist = dist[vals]
vLOS = vLOS[vals]

###############################################################################################

# create a position vector from the x, y, and z coordinates.
pos = zeros((len(xpos),3))

for i in range(len(xpos)):
    pos[i,0] = xpos[i]
    pos[i,1] = ypos[i]
    pos[i,2] = zpos[i]

###############################################################################################

# define the velocity correlation function, psi1 

def psi1(r1,r2,dists,pos,vLOSs,innerr,outerr):
""" psi1 calculates not only the velocity correlation function (in bins of width r2-r1), but keeps track of the number of stars included in the calculation ("counter"), as well as the number of pairs of stars ("pairs").  Its inputs include r1 and r2, which specify the binning for the velocity correlation function.  They are smallest and largest separations which are included.  dists is a 1D array of the stellar distances from the sun. pos is a 2D array of the three-dimensional positions of the sun (each element is a position with x, y, and z coordinates). vLOSs is a 1D array of the line of sight velocities of the stars with respect to the sun.  innerr and outerr are the innermost and outermost radii from the sun which define the spherical shell within which the correlation function is calculated. 
"""
    num = 0
    den = 0
    countlist = list()
    size = len(dists)
    pairs = 0
    for i in range(size):
        if (innerr < dists[i] <= outerr): # only consider stars within the specified distance
                                          # shell
            for j in range(i+1,size): # restricts the calculation to pairs
                if (innerr < dists[j] <= outerr): 
                    sep = sqrt((pos[i][0]-pos[j][0])**2. + (pos[i][1]-pos[j][1])**2. 
                                 + (pos[i][2]-pos[j][2])**2.)
                    if r1 < sep <= r2:
                        costh = dot( pos[i], pos[j] ) / (dists[i]*dists[j])
                        num = num + vLOSs[i]*vLOSs[j]*costh
                        den = den + costh**2.
                        countlist.append(i)
                        countlist.append(j)
                        pairs = pairs + 1
                    else:
                        pass
                else:
                    pass
        else:
            pass
        countlist = list(set(countlist)) # there's a lot of overcounting, and these lists become
                                         # large, so take a set occasionally to make them less
                                         # massive.
    counter = len(set(countlist))
    if den == 0: # don't divide by zero!
        return 'NAN', counter, pairs
    else:
        return num / den, counter, pairs

###############################################################################################

# Calculate a bootstrapped sample:
   
random.seed(seed)

boot = random.choice(len(xpos),len(xpos),replace=True) # sample the points with replacement
pos_samp = pos[boot]
dist_samp = dist[boot]
vLOS_samp = vLOS[boot]

###############################################################################################

# Compute the velocity correlation function and output the data to an appropriately labelled 
# file.

# start by defining the separation bins for the correlation function:
# this divides the possible separation values within the specified shell on which the correlation function is calculated (i.e. twice the # distance between innerr and outterr) into "bins" bins.
step = (2*outerr) / bins
rvals = arange(0,2*outerr+step,step) 

psi1out = open("JBout8psi1_polygon_"+str(innerr)+"_"+str(outerr)+"_"+str(bins)+".txt",'w')

for i in range(int(bins)):
    psi1vals, counter, pairs = psi1(rvals[i],rvals[i+1],dist_samp,pos_samp,
                                                   vLOS_samp,innerr,outerr)
    psi1out.write(str(rvals[i])+" "+str(rvals[i+1])+" "+str(psi1vals)+" "+str(counter)+" "+
                     str(pairs)+"\n")
        
psi1out.close()

# This output data can by plotted using mk_plot.py.



