########################################################################
# @TheDoctorRAB
########################################################################
#
# Multiple bar chart per label
#
# Labels are months so always the same
#
# Bars are money per year
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
script,plot_datafile=argv
#
#######
#
# screen resolution
#
import tkinter
root=tkinter.Tk()
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
matplotlib.rcParams.update({'font.size': 36}) #axis numbers
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
title='Unfiltered sources by keyword -- 'Risk-benefit Logic''
xtitle='Keywords'
ytitle='Number of sources'
#
###
#
# legend
# add linecolorN for each plot_dataN
# add curve_textN for each plot_dataN
# https://matplotlib.org/stable/gallery/color/named_colors.html
#
bar_color0='olive',
bar_color1='red',
bar_color2='blue',
bar_color3='green',
bar_color4='chocolate',
bar_color5='orchid',
bar_color6='darkorange',
bar_color7='black',
bar_color8='teal',
bar_color9='olive'
bar_color10='olive',
bar_color11='red',
bar_color12='blue',
bar_color13='green',
bar_color14='chocolate',
bar_color15='orchid',
bar_color16='darkorange',
bar_color17='black',
#
edge_color='black' #color
#
bar_text0='risk-benefit logic & nuclear fuel cycle'
bar_text1='risk-benefit logic & nuclear waste'
bar_text2='risk-benefit logic & HLW'
bar_text3='risk-benefit logic & SNF'
bar_text4='risk-benefit logic & TRU'
bar_text5='risk-benefit logic & LLW'
bar_text6='risk-benefit logic & critical facilities'
bar_text7='risk-benefit logic & critical infrastructure'
#bar_text8=''
#bar_text9=''
#
legend_location='upper right' #location of legend on grid
legend_font=24
#
###
#
# annotate
# position of the annotation dependent on axis domain and range
#
#annotate_title='Utility set'
#annotate_x=0.71
#annotate_y=0.95
#
#annotate_title2=''
#annotate_x2=
#annotate_y2=
#
#annotate_title3=''
#annotate_x3=
#annotate_y3=
#
###
#
# axis domain and range
#
#xmin=0.01
#xmax=12.99
ymin=0
ymax=1
#
###
#
# axis ticks
#
#xmajortick=1
ymajortick=0.10
#
#xminortick=1
yminortick=0.025
#
###
#
# grid linewidth
#
major_grid_linewidth=3.5
minor_grid_linewidth=3.1
#
major_grid_tick_length=7
minor_grid_tick_length=5
#
###
#
# bar width and position
#
bar_linewidth=4.0
bar_width=0.10
offset=0.00
#
###
#
# bar labels
#
stressors=3
r=numpy.arange(stressors)
global_position=numpy.arange(stressors)
#
# position the bars
#
#global_position=1.0+(r-1.0)*offset
print(global_position)
#
basis = ['NFC','NW','HLW','SNF','TRU','LLW','CF','CI']
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
left_axis.grid(which='major',axis='y',linewidth=major_grid_linewidth)
left_axis.grid(which='minor',axis='y',linewidth=minor_grid_linewidth)
#
left_axis.tick_params(axis='y',which='major',direction='inout',length=major_grid_tick_length)
left_axis.tick_params(axis='y',which='minor',direction='inout',length=minor_grid_tick_length)
#
###
#
# axis domain and range
#
#plot.xlim(xmin,xmax)
left_axis.axis(ymin=ymin,ymax=ymax)
###
#
# axis ticks
#
#left_axis.xaxis.set_major_locator(MultipleLocator(xmajortick))
#left_axis.xaxis.set_minor_locator(MultipleLocator(xminortick))
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
#left_axis.annotate(annotate_title2,xy=(annotate_x2,annotate_y2),xytext=(annotate_x2,annotate_y2),fontsize=annotate_fontsize)
#left_axis.annotate(annotate_title3,xy=(annotate_x3,annotate_y3),xytext=(annotate_x3,annotate_y3),fontsize=annotate_fontsize)
#
#######
#
# plot data
#
plot.bar(global_position[0],plot_data[0],width=bar_width,color=bar_color0,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text0)
plot.bar(global_position[1],plot_data[1],width=bar_width,color=bar_color1,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text1)
plot.bar(global_position[2],plot_data[2],width=bar_width,color=bar_color2,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text2)
left_axis.legend(loc=legend_location,fontsize=legend_font,framealpha=1,shadow=True,ncol=10) #legend needs to be after all the plot data
plot.get_current_fig_manager().resize(width,height)
plot.gcf().set_size_inches((0.01*width),(0.01*height))
plot.xticks(global_position,basis)
plot.xlim(-1,3)
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
plot.tight_layout()
plot.show()
#
########################################################################
#
# EOF
#
########################################################################
