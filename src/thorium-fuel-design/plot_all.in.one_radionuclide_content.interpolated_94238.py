########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.11.March.2015
########################################################################
#
# Plot routine
# All in one file, with no separate control input, lib files
# Plot data is contained in a separate data file, read on command line
# Set up for a secondary y axis if needed
# Plots burnup v burn time.
# Run mcnpx_burn.card.py first.
#
########################################################################
#
#
#
#######
#
# imports
#
# plot
import numpy
import matplotlib
import matplotlib.pyplot as plot
from matplotlib.ticker import MultipleLocator
###
#
# command line
from sys import argv
script,plot_datafile0=argv #add plotdatafileN for each data file to plot
###
#
# screen resolution
import Tkinter
import ctypes
root=Tkinter.Tk()
user32=ctypes.windll.user32
#
########################################################################
#
#
#
#######
#
# screen resolution
#
###
#
# pixels
#
width_px=root.winfo_screenwidth()
height_px=root.winfo_screenheight()
#
###
#
# mm
#
width_mm=root.winfo_screenmmwidth()
height_mm=root.winfo_screenmmheight()
#
###
#
# in
#
width_in=width_mm/25.4 
height_in=height_mm/25.4
#
###
#
# dpi
#
width_dpi=width_px/width_in
height_dpi=height_px/height_in
#
###
#
# get system metrics
#
user32.SetProcessDPIAware()
[width,height]=[user32.GetSystemMetrics(0),user32.GetSystemMetrics(1)]
current_dpi=width*96/width_px
#
###
#
# output to screen
print('width: %i px, height: %i px'%(width_px,height_px))
print('width: %i mm, height: %i mm'%(width_mm,height_mm))
print('width: %0.f in, height: %0.f in'%(width_in,height_in))
print('width: %0.f dpi, height: %0.f dpi'%(width_dpi,height_dpi))
print('size is %0.f %0.f'%(width,height))
print('current DPI is %0.f' % (current_dpi))
#
#######
#
# open the plot data file(s)
# add plot_dataN for each plot_datafileN
#
plot_data0=numpy.loadtxt(plot_datafile0,dtype=float)
#
#######
#
# graph parameters
#
###
#
# font sizes
#
matplotlib.rcParams.update({'font.size': 32}) #axis numbers
#
title_fontsize=48 #plot title
axis_fontsize=36 #axis labels
annotate_fontsize=32 #annotation
#
###
#
# set up for two y axis
#
fig,left_axis=plot.subplots()
# right_axis=left_axis.twinx()
#
###
# 
# plot text
#
title='Plutonium mass as a function of thorium content at critical'
xtitle='time [d]'
ytitle='$^{238}Pu$ mass [g]'
#
###
#
# legend
# add linecolorN for each plot_dataN
# add curve_textN for each plot_dataN 
#
line_color0='black' #color
#
curve_text0='interpolated' #legend text
#
legend_location='upper left' #location of legend on grid
legend_font=28
#
###
#
# annotate
# position of the annotation dependent on axis domain and range
#
annotate_title='' 
annotate_x=0
annotate_y=0
#
###
#
# axis domain and range
#
xmin=0
xmax=0.95 
#
ymin=0 
ymax=225
#
###
#
# axis ticks
#
xmajortick=0.05
ymajortick=50
#
xminortick=0.01
yminortick=10
#
###
#
# grid linewidth
#
major_grid_linewidth=1.5
minor_grid_linewidth=1.1
#
major_grid_tick_length=7
minor_grid_tick_length=5
#
###
#
# curve linewidth
#
curve_linewidth=2.0
#
#######
#
# set plot diagnostics
#
###
#
# titles
#
plot.title(title,fontsize=title_fontsize)
left_axis.set_xlabel(xtitle,fontsize=axis_fontsize)
left_axis.set_ylabel(ytitle,fontsize=axis_fontsize)
# right_axis.set_ylabel()
#
###
#
# grid
#
left_axis.grid(which='major',axis='both',linewidth=major_grid_linewidth)
left_axis.grid(which='minor',axis='both',linewidth=minor_grid_linewidth)
#
left_axis.tick_params(axis='both',which='major',direction='inout',length=major_grid_tick_length)
left_axis.tick_params(axis='both',which='minor',direction='inout',length=minor_grid_tick_length)
#
###
#
# axis domain and range
#
plot.xlim(xmin,xmax)
left_axis.axis(ymin=ymin,ymax=ymax)
###
#
# axis ticks
#
left_axis.xaxis.set_major_locator(MultipleLocator(xmajortick))
left_axis.xaxis.set_minor_locator(MultipleLocator(xminortick))
left_axis.yaxis.set_major_locator(MultipleLocator(ymajortick))
left_axis.yaxis.set_minor_locator(MultipleLocator(yminortick))
#
###
#
# log scale option
# xmin,ymin !=0 for log scale
#
#left_axis.set_xscale('log')
#left_axis.set_yscale('log')
#
###
#
# annotation
# comment out if not needed
#
#left_axis.annotate(annotate_title,xy=(annotate_x,annotate_y),xytext=(annotate_x,annotate_y),fontsize=annotate_fontsize)
#
#######
#
# plot data
#
left_axis.plot(plot_data0[:,0],plot_data0[:,1],color=line_color0,label=curve_text0,linewidth=curve_linewidth)
left_axis.legend(loc=legend_location,fontsize=legend_font) #legend needs to be after all the plot data
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
