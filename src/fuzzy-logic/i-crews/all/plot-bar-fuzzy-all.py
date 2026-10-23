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
title='Crisp Number All'
xtitle='Stressor'
xtitle=''
ytitle='Crisp number'
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
bar_text0='Environmental & Climate Stress'        #legend text
bar_text1='Water Infrastructure Capacity'           #legend text
bar_text2='Water Supply Constraints'    #legend text
bar_text3='Water Quality Degradation'   #legend text
bar_text4='Agricultural & Industrial Demand'    #legend text
bar_text5='Development Impacts'   #legend text
bar_text6='Energy System Reliability'        #legend text
bar_text7='Environmental & Climate Stress'           #legend text
bar_text8='Energy System Diversity'    #legend text
bar_text9='Energy System Transition'   #legend text
bar_text10='Industrial Pressure'    #legend text
bar_text11='Urbanization'   #legend text
bar_text12='Environmental & Climate Stress'        #legend text
bar_text13='Policy Change & Permitting'           #legend text
bar_text14='Economic Pressures'    #legend text
bar_text15='Energy-Water Infrastructure'   #legend text
bar_text16='Industrial Growth'    #legend text
bar_text17='Residential Growth'   #legend text
#bar_text6=''                  #legend text
#bar_text7=''                   #legend text
#bar_text8=''                  #legend text
#bar_text9=''                  #legend text
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
stressors=18
r=numpy.arange(stressors)
global_position=numpy.arange(stressors)
#
# position the bars
#
#global_position=1.0+(r-1.0)*offset
print(global_position)
#
basis = ['ECS','WIC','WSC','WQD','AID','DI','ESR','ECS','ESD','EST','IP','UB','ECS','PCP','EP','EWI','IG','RG']
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
plot.bar(global_position[3],plot_data[3],width=bar_width,color=bar_color3,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text3)
plot.bar(global_position[4],plot_data[4],width=bar_width,color=bar_color4,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text4)
plot.bar(global_position[5],plot_data[5],width=bar_width,color=bar_color5,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text5)
plot.bar(global_position[6],plot_data[6],width=bar_width,color=bar_color6,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text6)
plot.bar(global_position[7],plot_data[7],width=bar_width,color=bar_color7,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text7)
plot.bar(global_position[8],plot_data[8],width=bar_width,color=bar_color8,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text8)
plot.bar(global_position[9],plot_data[9],width=bar_width,color=bar_color9,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text9)
plot.bar(global_position[10],plot_data[10],width=bar_width,color=bar_color10,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text10)
plot.bar(global_position[11],plot_data[11],width=bar_width,color=bar_color11,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text11)
plot.bar(global_position[12],plot_data[12],width=bar_width,color=bar_color12,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text12)
plot.bar(global_position[13],plot_data[13],width=bar_width,color=bar_color13,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text13)
plot.bar(global_position[14],plot_data[14],width=bar_width,color=bar_color14,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text14)
plot.bar(global_position[15],plot_data[15],width=bar_width,color=bar_color15,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text15)
plot.bar(global_position[16],plot_data[16],width=bar_width,color=bar_color16,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text16)
plot.bar(global_position[17],plot_data[17],width=bar_width,color=bar_color17,edgecolor=edge_color,linewidth=bar_linewidth,label=bar_text17)
left_axis.legend(loc=legend_location,fontsize=legend_font,framealpha=1,shadow=True,ncol=3) #legend needs to be after all the plot data
plot.get_current_fig_manager().resize(width,height)
plot.gcf().set_size_inches((0.01*width),(0.01*height))
plot.xticks(global_position,basis)
#plot.xlim(-1,3)
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
