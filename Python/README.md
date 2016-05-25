## Python Code Sample Readme
--Bridget Bertoni 5/20/2016


The four files included in this code sample are designed to calculate a bootstrapped velocity correlation function for a specific simulated stellar dataset and then plot the results.  More detailed information about each file is included in comments at the top of each file.


The code is executed in the bash shell as follows:

bash run_JB_vel_corr_polygon_boot.sh halo_number

where halo_number is the a string which labels the halo data set you want to use to compute the velocity correlation function.


This shell script executes compute_JB_vel_corr_polygon_boot.sh 20 times, each with different inputs.  Running compute_JB_vel_corr_polygon_boot.sh submits a single job to the Stanford computer cluster which runs the code compute_JB_vel_corr_polygon_boot.py.  This python code calculates the velocity correlation function and produces an output text file.


The output data can by plotted using mk_plot.py which is executed in the shell by typing:

python mk_plot.py random 

where random is the random number which was generated when running run_JB_vel_corr_polygon_boot.sh and was using to label the output folder which contains all of the output.  An example of the output from this code is shown in the file JB_mangle_halo02.png.
