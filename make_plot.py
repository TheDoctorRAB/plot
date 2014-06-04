########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.02.June.2014
########################################################################
# This function prepares a standard xy line plot.
# It is set up for a secondary y axis if needed.
# A matrix of 2 columns (x,y) must be passed in.
# The second argument 0 or 1 turns off/on the grid lines.
# The minor gridlines are commented out because they aren't used commonly.
########################################################################
#
########################################################################
# input files
# plot_labels = title,xaxis,yaxis; just input one per line as is
# axis_config.major = xmin,xmax,ymin,ymax; input tabbed (2) per line
# axis_config.minor = tick marks; xmajor,ymajor,xminor,yminor
########################################################################
#
#
#
####### imports
import numpy
import matplotlib.pyplot as plot
from matplotlib.ticker import MultipleLocator
#######
#
#
#
####### make the plot
def makeplot(plotdata,grid_parameter):
###
# set up for two y axis
    fig,left_axis=plot.subplots()
#right_axis=left_axis.twinx()
###
# plot text
    plot_text=numpy.loadtxt('plot_labels.inp',dtype=str,delimiter='\n')
    title=plot_text[0]
    xtitle=plot_text[1]
    ytitle=plot_text[2]
    line_color=plot_text[3]
###
    plot.title(title,fontsize=18)
    left_axis.set_xlabel(xtitle,fontsize=16)
    left_axis.set_ylabel(ytitle,fontsize=16)
#right_axis.set_ylabel()
###
# axis
    axis_config_major=numpy.loadtxt('axis_config.major.inp')
    axis_config_minor=numpy.loadtxt('axis_config.minor.inp')
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
###
    plot.xlim(xmin,xmax)
    left_axis.axis(ymin=ymin,ymax=ymax)
#
    left_axis.xaxis.set_major_locator(MultipleLocator(xmajortick))
    left_axis.xaxis.set_minor_locator(MultipleLocator(xminortick))
    left_axis.yaxis.set_major_locator(MultipleLocator(ymajortick))
    left_axis.yaxis.set_minor_locator(MultipleLocator(yminortick))
#
    left_axis.tick_params(axis='both',which='major',direction='inout',length=7)
###
# grid
    if grid_parameter==1:
        left_axis.grid(which='major',axis='both',linewidth='1.1')
#       left_axis.grid(which='minor',axis='both')
###
# plot
        left_axis.plot(plotdata[:,0],plotdata[:,1],color=line_color)
###
        plot.show()
###
# save
        plot.savefig(title)
#######
#
#
#
########################################################################
#      EOF
########################################################################
