########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.24.December.2015
########################################################################
# 
# Prepares a standard xy line plot.
# It is set up for a secondary y axis if needed.
# Data is contained in separare file and read in on command line.
# Just include multiple files for more curves on the plot.
# Graph label information is contained in the input files.
# Obviously, need to know ahead of time which columns in the input file to plot.
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
script,plot_datafile0,plot_datafile1=argv
#
########################################################################
#
#
#
#######
#
# open the plot data file(s)
#
plot_data0=numpy.loadtxt(plot_datafile0,dtype=float)
plot_data1=numpy.loadtxt(plot_datafile1,dtype=float)
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
plot_text=numpy.loadtxt('plot_labels.inp',dtype=str,delimiter='\n')
curve_text=numpy.loadtxt('curve_labels.inp',dtype=str,delimiter='\n')
title=plot_text[0]
xtitle=plot_text[1]
ytitle=plot_text[2]
line_color0=plot_text[3]
line_color1=plot_text[4]
line_color2=plot_text[5]
#line_color3=plot_text[6]
#line_color4=plot_text[7]
#line_color5=plot_text[8]
#line_color6=plot_text[9]
#line_color7=plot_text[10]
#line_color8=plot_text[11]
#line_color9=plot_text[12]
#line_color10=plot_text[13]
#line_color11=plot_text[14]
#line_color12=plot_text[15]
#line_color13=plot_text[16]
#line_color14=plot_text[17]
#line_color15=plot_text[18]
#line_color16=plot_text[19]
#line_color17=plot_text[20]
#line_color18=plot_text[21]
#line_color19=plot_text[22]
#
plot.title(title)
left_axis.set_xlabel(xtitle)
left_axis.set_ylabel(ytitle)
# right_axis.set_ylabel()
#
annotate_text=numpy.loadtxt('annotate.inp',dtype=str,delimiter='\n')
annotate_title=annotate_text[0]
annotate_x=annotate_text[1]
annotate_y=annotate_text[2]
#
#######
#
# axis
#
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
left_axis.plot(plot_data0[:,0],plot_data0[:,1],color=line_color0,label=curve_text[0],linewidth=2.0)
left_axis.plot(plot_data1[:,0],plot_data1[:,1],'rs',color=line_color1,label=curve_text[1],linewidth=2.0)
left_axis.set_xscale('log')
left_axis.set_yscale('log')
left_axis.legend(loc='lower right',fontsize='24')
left_axis.annotate(annotate_title,xy=(annotate_x,annotate_y),xytext=(annotate_x,annotate_y))
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
