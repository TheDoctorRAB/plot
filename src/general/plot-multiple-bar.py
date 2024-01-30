########################################################################
# @TheDoctorRAB
########################################################################
#
# Multiple bar chart per label
#
# Labels are months so always the same
#
# Bars are per year
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
# compute average of data by columns if needed
#
months=12
columns=numpy.shape(plot_data)[1]-1 #columns minus [0] if data label present
#
average=numpy.zeros(shape=(months,1))
#
average=numpy.mean(plot_data,axis=1)
print(average)
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
title='Ending monthly balance'
xtitle='Month'
xtitle=''
ytitle='$'
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
bar_color8='olive' #color
#
edge_color='black' #color
#
bar_text0='2024'                  #legend text
bar_text1='2023'                  #legend text
bar_text2='2022'                  #legend text
bar_text3='2021'                  #legend text
bar_text4='2020'                  #legend text
bar_text5='2019'                  #legend text
bar_text6='2018'                  #legend text
bar_text7='AVG'                   #legend text
bar_text8='2017'                  #legend text
#
bar_width=0.10
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
r=numpy.arange(months)
month_basis = ['J','F','M','A','M','J','J','A','S','O','N','D']
#month = [20*i for i in month_basis]
#xmin=0.01
#xmax=12.99
#
ymin=0
ymax=35000
#
###
#
# axis ticks
#
#xmajortick=1
ymajortick=5000
#
#xminortick=1
yminortick=1000
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
plot.bar(r-4.55*bar_width,plot_data[:,0],bar_width,color=bar_color0,edgecolor=edge_color,label=bar_text0,linewidth=bar_linewidth)
plot.bar(r-3.55*bar_width,plot_data[:,1],bar_width,color=bar_color1,edgecolor=edge_color,label=bar_text1,linewidth=bar_linewidth)
plot.bar(r-2.55*bar_width,plot_data[:,2],bar_width,color=bar_color2,edgecolor=edge_color,label=bar_text2,linewidth=bar_linewidth)
plot.bar(r-1.55*bar_width,plot_data[:,3],bar_width,color=bar_color3,edgecolor=edge_color,label=bar_text3,linewidth=bar_linewidth)
plot.bar(r,average,avg_bar_width,color=bar_color7,edgecolor=edge_color,label=bar_text7,linewidth=bar_linewidth)
#plot.bar(r,plot_data[:,8],avg_bar_width,color=bar_color7,edgecolor=edge_color7,label=bar_text7,linewidth=bar_linewidth)
plot.bar(r+1.55*bar_width,plot_data[:,4],bar_width,color=bar_color4,edgecolor=edge_color,label=bar_text4,linewidth=bar_linewidth)
plot.bar(r+2.55*bar_width,plot_data[:,5],bar_width,color=bar_color5,edgecolor=edge_color,label=bar_text5,linewidth=bar_linewidth)
plot.bar(r+3.55*bar_width,plot_data[:,6],bar_width,color=bar_color6,edgecolor=edge_color,label=bar_text6,linewidth=bar_linewidth)
plot.bar(r+4.55*bar_width,plot_data[:,7],bar_width,color=bar_color8,edgecolor=edge_color,label=bar_text8,linewidth=bar_linewidth)
#plot.bar(plot_data[:,0]-2*bar_width,plot_data[:,1],bar_width,color=bar_color0,edgecolor=edge_color0,label=bar_text0,linewidth=bar_linewidth)
#plot.bar(plot_data[:,0]-1*bar_width,plot_data[:,2],bar_width,color=bar_color1,edgecolor=edge_color1,label=bar_text1,linewidth=bar_linewidth)
#plot.bar(plot_data[:,0]+1*bar_width,plot_data[:,3],bar_width,color=bar_color2,edgecolor=edge_color2,label=bar_text2,linewidth=bar_linewidth)
#plot.bar(plot_data[:,0]+2*bar_width,plot_data[:,4],bar_width,color=bar_color3,edgecolor=edge_color3,label=bar_text3,linewidth=bar_linewidth)
#plot.bar(plot_data[:,0]+3*bar_width,plot_data[:,5],bar_width,color=bar_color4,edgecolor=edge_color4,label=bar_text4,linewidth=bar_linewidth)
#left_axis.plot(plot_data[:,0],plot_data[:,1],color=line_color0,label=curve_text0,linewidth=curve_linewidth,markersize=20)
#left_axis.plot(plot_data[:,2],plot_data[:,0],marker='o',color=line_color1,label=curve_text1,linewidth=curve_linewidth,markersize=20)
#left_axis.plot(plot_data[:,3],plot_data[:,0],marker='o',color=line_color2,label=curve_text2,linewidth=curve_linewidth,markersize=20)
left_axis.legend(loc=legend_location,fontsize=legend_font,framealpha=1,shadow=True,ncol=10) #legend needs to be after all the plot data
plot.get_current_fig_manager().resize(width,height)
plot.gcf().set_size_inches((0.01*width),(0.01*height))
plot.xticks(r+0.125*bar_width,month_basis)
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
