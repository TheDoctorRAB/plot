########################################################################
# @TheDoctorRAB
########################################################################
#
# Processing census data into histograms
#
# Single bar per label (city for here)
#
# Data files in ../data directory
#
# Label should be in 0 column in plot_datafile and be \t
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
# extract string from plot_datafile in column 0
#
census_raw_data=numpy.loadtxt(plot_datafile,dtype=str,delimiter='\t')
city_total = numpy.shape(census_raw_data)[0] #rows
data_total = numpy.shape(census_raw_data)[1]-2 #columns minus city name [0] and source [1]
#
#######
#
# load array with city names
#
cities=numpy.empty(city_total,dtype='<U15') #loads string data UNN truncates labels by NN
#
for i in range(0,city_total):
    cities[i]=census_raw_data[i,0]
# end i
#
print(cities)
#######
#
# load data array
#
census_data=numpy.zeros(shape=(city_total,data_total))
#
for i in range(0,city_total):
    for j in range(0,data_total):
        census_data[i,j]=float(census_raw_data[i,j+2])
#   end j
# end i
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
xaxis_fontsize=6 #axis labels
yaxis_fontsize=48 #axis labels
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
title='Employment'
xtitle=''
ytitle='Percent employed'
#
###
#
# legend
# add linecolorN for each plot_dataN
# add curve_textN for each plot_dataN
# https://matplotlib.org/stable/gallery/color/named_colors.html
#
bar_color0='red' #color
bar_color1='blue' #color
bar_color2='green' #color
bar_color3='chocolate' #color
bar_color4='orchid' #color
bar_color5='darkorange' #color
bar_color6='teal' #color
bar_color7='black' #color
#
edge_color0='black' #color
edge_color1='black' #color
edge_color2='black' #color
edge_color3='black' #color
edge_color4='black' #color
edge_color5='black' #color
edge_color6='black' #color
edge_color7='black' #color
#
#bar_text0=''                  #legend text
#bar_text1=''                  #legend text
#bar_text2=''                  #legend text
#bar_text3=''                  #legend text
#bar_text4=''                  #legend text
#bar_text5=''                  #legend text
#bar_text6=''                  #legend text
#bar_text7=''                  #legend text
#
bar_width=0.15
avg_bar_width=0.125
legend_location='upper right' #location of legend on grid
legend_font=28
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
#N=12
#r=numpy.arange(N)
#month_basis = ['J','F','M','A','M','J','J','A','S','O','N','D']
#xmin=0.01
#xmax=32.99
#
ymin=0
ymax=100
#
###
#
# axis ticks
#
#xmajortick=1
ymajortick=10
#
#xminortick=1
yminortick=2
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
# bar linewidth
#
bar_linewidth=4.0
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
#left_axis.set_xlabel(xtitle,fontsize=axis_fontsize)
left_axis.set_ylabel(ytitle,fontsize=yaxis_fontsize)
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
#plot.bar(cities,census_data[:,0],bar_width,color=bar_color0,edgecolor=edge_color0,linewidth=bar_linewidth)
#plot.bar(cities,census_data[:,1],bar_width,color=bar_color0,edgecolor=edge_color0,linewidth=bar_linewidth)
plot.bar(cities,census_data[:,1],bar_width,color=bar_color0,edgecolor=edge_color0,linewidth=bar_linewidth)
plot.get_current_fig_manager().resize(width,height)
plot.gcf().set_size_inches(60,40)
#plot.gcf().set_size_inches((0.01*width),(0.01*height))
plot.xticks(rotation=90)
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
