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
#
import numpy
import matplotlib
import matplotlib.pyplot as plot
from matplotlib.ticker import MultipleLocator
#
#######
#
# command line
#
from sys import argv
script,plot_datafile=argv #column 0 is the x values then odd columns contain dose/flux
#
#######
#
# screen resolution
#
import Tkinter
root=Tkinter.Tk()
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
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
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
width_dpi=width/width_in
height_dpi=height/height_in
#
dpi_values=(96,120,144,168,192)
current_dpi=width_dpi
minimum=1000
#
for dval in dpi_values:
  difference=abs(dval-width_dpi)
  if difference<minimum:
    minimum=difference
    current_dpi=dval
#
#######
#
# output to screen
#
print('width: %i px, height: %i px'%(width,height))
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
plot_data=numpy.loadtxt(plot_datafile,dtype=float)
#
#######
#
# graph parameters
#
###
#
# font sizes
#
matplotlib.rcParams.update({'font.size': 48}) #axis numbers
#
title_fontsize=54 #plot title
axis_fontsize=48 #axis labels
annotate_fontsize=48 #annotation
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
title='Dose rate - West plate'
xtitle='Wall thickness [cm]'
ytitle='Dose rate [$\mu$Sv/h]'
#
###
#
# legend
# add linecolorN for each plot_dataN
# add curve_textN for each plot_dataN
#
line_color0='blue' #color
line_color1='orange' #color
line_color2='red' #color
line_color3='green' #color
line_color4='cyan' #color
#
curve_text0='10 wt% $B_4C$'	    #legend text
curve_text1='30 wt% $B_4C$'	    #legend text
curve_text2='50 wt% $B_4C$'	    #legend text
curve_text3='70 wt% $B_4C$'	    #legend text
curve_text4='90 wt% $B_4C$'	    #legend text
#
legend_location='lower left' #location of legend on grid
legend_font=42
#
###
#
# annotate
# position of the annotation dependent on axis domain and range
#
annotate_title='L-3030'
annotate_x=23
annotate_y=2700
#
annotate_title2='Helium-Glass backfill'
annotate_x2=23
annotate_y2=1700
#
annotate_title3='10 wt% $^{10}B$'
annotate_x3=23
annotate_y3=900
#
###
#
# axis domain and range
#
xmin=1
xmax=31
#
ymin=1
ymax=4000
#
###
#
# axis ticks
#
xmajortick=5
ymajortick=5000
#
xminortick=1
yminortick=1000
#
###
#
# grid linewidth
#
major_grid_linewidth=2.5
minor_grid_linewidth=2.1
#
major_grid_tick_length=7
minor_grid_tick_length=5
#
###
#
# curve linewidth
#
curve_linewidth=4.0
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
left_axis.set_yscale('log')
#
###
#
# annotation
# comment out if not needed
#
left_axis.annotate(annotate_title,xy=(annotate_x,annotate_y),xytext=(annotate_x,annotate_y),fontsize=annotate_fontsize)
left_axis.annotate(annotate_title2,xy=(annotate_x2,annotate_y2),xytext=(annotate_x2,annotate_y2),fontsize=annotate_fontsize)
left_axis.annotate(annotate_title3,xy=(annotate_x3,annotate_y3),xytext=(annotate_x3,annotate_y3),fontsize=annotate_fontsize)
#
#######
#
# plot data
#
left_axis.plot(plot_data[:,0],plot_data[:,1],marker='o',color=line_color0,label=curve_text0,linewidth=curve_linewidth,markersize=20)
left_axis.plot(plot_data[:,0],plot_data[:,3],marker='o',color=line_color1,label=curve_text1,linewidth=curve_linewidth,markersize=20)
left_axis.plot(plot_data[:,0],plot_data[:,5],marker='o',color=line_color2,label=curve_text2,linewidth=curve_linewidth,markersize=20)
left_axis.plot(plot_data[:,0],plot_data[:,7],marker='o',color=line_color3,label=curve_text3,linewidth=curve_linewidth,markersize=20)
left_axis.plot(plot_data[:,0],plot_data[:,9],marker='o',color=line_color4,label=curve_text4,linewidth=curve_linewidth,markersize=20)
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
