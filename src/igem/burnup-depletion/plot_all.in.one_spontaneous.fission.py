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
script,plot_datafile0,plot_datafile1,plot_datafile2=argv #add plotdatafileN for each data file to plot
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
plot_data0=numpy.loadtxt(plot_datafile0,dtype=float)
plot_data1=numpy.loadtxt(plot_datafile1,dtype=float)
plot_data2=numpy.loadtxt(plot_datafile2,dtype=float)
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
annotate_fontsize=30 #annotation
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
title='Spontaneous fission rate per assembly'
xtitle='Time (y)'
ytitle='Spontaneous fission rate (neutrons/s)'
#
###
#
# legend
# add linecolorN for each plot_dataN
# add curve_textN for each plot_dataN
#
line_color0='blue' #color
line_color1='black' #color
line_color2='red' #color
#line_color3='green' #color
#line_color4='cyan' #color
#line_color5='magenta' #color
#line_color6='purple' #color
#line_color7='orange' #color
#line_color8='pink' #color
#
curve_text0='L-3030' #legend text
curve_text1='T-4045' #legend text
curve_text2='H-5060' #legend text
#curve_text3='L-3233' #legend text
#curve_text4='L-3533' #legend text
#curve_text5='L-3535' #legend text
#curve_text6='L-3240' #legend text
#curve_text7='L-3540' #legend text
#curve_text8='L-4040' #legend text
#
legend_location='upper right' #location of legend on grid
legend_font=28
#
###
#
# annotate
# position of the annotation dependent on axis domain and range
#
#annotate_title='Notes'
#annotate_x=0
#annotate_y=0
#
###
#
# axis domain and range
#
xmin=0
xmax=20
#
ymin=5E7
ymax=2E9
#
###
#
# axis ticks
#
xmajortick=5
#ymajortick=0.1
#
xminortick=1
#yminortick=0.01
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
#left_axis.yaxis.set_major_locator(MultipleLocator(ymajortick))
#left_axis.yaxis.set_minor_locator(MultipleLocator(yminortick))
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
#left_axis.annotate(annotate_title,xy=(annotate_x,annotate_y),xytext=(annotate_x,annotate_y),fontsize=annotate_fontsize)
#
#######
#
# plot data
#
left_axis.plot(plot_data0[:,0],plot_data0[:,3],color=line_color0,label=curve_text0,linewidth=curve_linewidth)
left_axis.plot(plot_data1[:,0],plot_data1[:,3],color=line_color1,label=curve_text1,linewidth=curve_linewidth)
left_axis.plot(plot_data2[:,0],plot_data2[:,3],color=line_color2,label=curve_text2,linewidth=curve_linewidth)
#left_axis.plot(plot_data0[:,0],plot_data0[:,4],color=line_color3,label=curve_text3,linewidth=curve_linewidth)
#left_axis.plot(plot_data0[:,0],plot_data0[:,5],color=line_color4,label=curve_text4,linewidth=curve_linewidth)
#left_axis.plot(plot_data0[:,0],plot_data0[:,6],color=line_color5,label=curve_text5,linewidth=curve_linewidth)
#left_axis.plot(plot_data0[:,0],plot_data0[:,7],color=line_color6,label=curve_text6,linewidth=curve_linewidth)
#left_axis.plot(plot_data0[:,0],plot_data0[:,8],color=line_color7,label=curve_text7,linewidth=curve_linewidth)
#left_axis.plot(plot_data0[:,0],plot_data0[:,9],color=line_color8,label=curve_text8,linewidth=curve_linewidth)
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
