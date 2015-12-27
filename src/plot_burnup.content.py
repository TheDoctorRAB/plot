########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.27.December.2015
########################################################################
# 
# Prepares a standard xy line plot.
# It is set up for a secondary y axis if needed.
# Data is contained in separare file and read in on command line.
# Just include multiple files for more curves on the plot.
# Graph label information is contained in the input files.
# Obviously, need to know ahead of time which columns in the input file to plot.
# Plots BURN card data from MCNPX.
# Run mcnpx_burn.card first.
#
########################################################################
#
# input files
# plot_labels = title,xaxis,yaxis; just input one per line as is
# curve_lables = legend text
# axis_config.major = xmin,xmax,ymin,ymax; input tabbed (2) per line
# axis_config.minor = tick marks; xmajor,ymajor,xminor,yminor
#
########################################################################
#
#
#
####### 
#
# imports
#
import numpy
import matplotlib
import matplotlib.pyplot as plot
import screen_resolution
from matplotlib.ticker import MultipleLocator
from sys import argv
script,plot_datafile=argv
#
########################################################################
#
#
#
#######
#
# open the plot data file(s)
#
plot_data=numpy.loadtxt(plot_datafile,dtype=float)
#
#######
#
# diagnostics
#
matplotlib.rcParams.update({'font.size': 30}) #set global plot font
width,height,current_dpi=screen_resolution.screen_res()
#
####### 
#
# set up for two y axis
#
fig,left_axis=plot.subplots()
# right_axis=left_axis.twinx()
#
#######
# 
# plot text
#
plot_text=numpy.loadtxt('plot_labels.burnup.content.inp',dtype=str,delimiter='\n')
#curve_text=numpy.loadtxt('curve_labels.burnup.content.inp',dtype=str,delimiter='\n')
title=plot_text[0]
xtitle=plot_text[1]
ytitle=plot_text[2]
line_color=plot_text[3]
#
plot.title(title)
left_axis.set_xlabel(xtitle)
left_axis.set_ylabel(ytitle)
# right_axis.set_ylabel()
#
#######
#
# axis
#
axis_config_major=numpy.loadtxt('axis_config.major.burnup.content.inp')
axis_config_minor=numpy.loadtxt('axis_config.minor.burnup.content.inp')
xmin=axis_config_major[0,0]
xmax=axis_config_major[0,1]
#
ymin=axis_config_major[1,0]
ymax=axis_config_major[1,1]
#
xmajortick=axis_config_minor[0]
ymajortick=axis_config_minor[1]
#
xminortick=axis_config_minor[2]
yminortick=axis_config_minor[3]
#
plot.xlim(xmin,xmax)
left_axis.axis(ymin=ymin,ymax=ymax)
#
left_axis.xaxis.set_major_locator(MultipleLocator(xmajortick))
left_axis.xaxis.set_minor_locator(MultipleLocator(xminortick))
left_axis.yaxis.set_major_locator(MultipleLocator(ymajortick))
left_axis.yaxis.set_minor_locator(MultipleLocator(yminortick))
#
left_axis.tick_params(axis='both',which='major',direction='inout',length=7)
#
#######
#
# grid
#
left_axis.grid(which='major',axis='both',linewidth='1.1')
left_axis.grid(which='minor',axis='both')
#
#######
#
# plot diagnostics
#
left_axis.plot(plot_data[:,0],plot_data[:,1],color=line_color)
#left_axis.legend(loc='lower right',fontsize='16')
plot.get_current_fig_manager().resize(width,height)
plot.gcf().set_size_inches((0.01*width),(0.01*height))
#
#######
#
# save
#
plot.savefig(title,dpi=current_dpi)
#
#######
#
# plot to screen
#
plot.show()
#
########################################################################
#
# EOF
#
########################################################################