# This code plots the output velocity correlation function from a single run of
# run_JB_vel_corr_polygon_boot.sh for the Johnston and Bullock halo labelled as "halo02".  It
# creates a plot with 20 subplots, one for each of the separation shells within which the
# velocity correlation function was calculated.
#
# It has one input, which is the random seed label for the bootstrapped halo calculation.  This
# is carried along for labelling purposes so that these 'random' results are easily reproducible.

###############################################################################################

import matplotlib.pyplot as plt
from numpy import array
import sys

rvals = [0.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0,120.0,140.0,160.0,180.0,200.0,
	220.0,240.0,260.0,280.0,300.0]

rand = sys.argv[1]

fig,axs = plt.subplots(4,5)
fig.subplots_adjust(hspace=0.4,wspace=0.4)
axs = axs.ravel()
plt.suptitle("Bullock & Johnston data bootstrap sample"+str(rand)+", footprint,"+
             " |vLOS| < 600 km/s, |b| > 30 deg, random noise in dist and vLOS")
for i in range(len(rvals)-1):
	r = list()
	psi1 = list()
	counter = list()
	infile = open("/home/bridget/BullockJohnston/footprint_mangle/halo02_boot/"+str(rand)+
                      "/JBout8psi1_polygon_"+str(rvals[i])+"_"+str(rvals[i+1])+"_10.0.txt",'r')
	for line in infile.readlines():
		vals = line.split()
		r.append((float(vals[0])+float(vals[1]))/2.0)
		psi1.append(vals[2])
		counter.append(float(vals[3]))

	counter = array(counter)
	counter = max(counter)

	axs[i].plot(r,psi1,'bo',r,psi1,'b-')
	axs[i].set_title(str(rvals[i])+" kpc < distance < "+str(rvals[i+1])+" kpc \n"+ 
				"Nstars = "+"{:.2E}".format(float(counter)),size=10)
	infile.close()	

plt.show()

fig.savefig("JB_mangle_halo02_"+str(rand)+".png")


