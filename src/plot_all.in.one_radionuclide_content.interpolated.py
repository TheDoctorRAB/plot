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
title='Uranium mass as a function of thorium content at critical'
xtitle='time [d]'
ytitle='${242}^Pu$ mass [g]'
#
###
#
# legend
# add linecolorN for each plot_dataN
# add curve_textN for each plot_dataN 
#
line_color0='black' #color
line_color1='red' #color
line_color2='blue' #color
line_color3='green' #color
line_color4='magenta' #color
line_color5='cyan' #color
line_color6='orange' #color
line_color7='black' #color
line_color8='red' #color
line_color9='blue' #color
line_color10='green' #color
line_color11='magenta' #color
line_color12='cyan' #color
line_color13='orange' #color
line_color14='black' #color
line_color15='red' #color
line_color16='blue' #color
line_color17='green' #color
line_color18='magenta' #color
line_color19='cyan' #color
#
curve_text0='$0.00\ Th\ :\ 0.95\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text1='$0.05\ Th\ :\ 0.90\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text2='$0.10\ Th\ :\ 0.85\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text3='$0.15\ Th\ :\ 0.80\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text4='$0.20\ Th\ :\ 0.75\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text5='$0.25\ Th\ :\ 0.70\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text6='$0.30\ Th\ :\ 0.65\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text7='$0.35\ Th\ :\ 0.60\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text8='$0.40\ Th\ :\ 0.55\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text9='$0.45\ Th\ :\ 0.50\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text10='$0.50\ Th\ :\ 0.45\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text11='$0.55\ Th\ :\ 0.40\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text12='$0.60\ Th\ :\ 0.35\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text13='$0.65\ Th\ :\ 0.30\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text14='$0.70\ Th\ :\ 0.25\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text15='$0.75\ Th\ :\ 0.20\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text16='$0.80\ Th\ :\ 0.15\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text17='$0.85\ Th\ :\ 0.10\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text18='$0.90\ Th\ :\ 0.05\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
curve_text19='$0.95\ Th\ :\ 0.00\ ^{238}U\ :\ 0.05\ ^{235}U$' #legend text
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
ymax=1500
#
###
#
# axis ticks
#
xmajortick=0.05
ymajortick=500
#
xminortick=0.01
yminortick=100
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
