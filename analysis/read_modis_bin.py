'''

'''

import numpy as np
import os

import matplotlib.pyplot as plt

def read_modisbin(working_directory,filename,dimx,dimy):
 modis_wrashape=np.fromfile(working_directory+filename, dtype=np.float32)
 modis_single_layer = modis_wrashape.reshape(dimx,dimy)
 return modis_single_layer
 
def read_modis_radiance_bin(working_directory,filename,dimx,dimy,dimbands):
 modis_wrashape=np.fromfile(working_directory+filename, dtype=np.float32)
 modis_radiance = modis_wrashape.reshape(dimx,dimy,dimbands)
 return modis_radiance

########################################################################################################## 

# set filenames

working_directory='C:/zsofia/Amsterdam/GitHub/komazsofi/chla_balaton_modis/data/'

cloud='Cloudmask_1KM_AQUA_xxxxx_20170925_114500.xxxxx_(fltarr_1354x2030).bin'
latitude='Lat_1KM_AQUA_xxxxx_20170925_114500.xxxxx_(fltarr_1354x2030).bin'
longitude='Lon_1KM_AQUA_xxxxx_20170925_114500.xxxxx_(fltarr_1354x2030).bin'

radiance='Radiances_Ch1-19_1KM_AQUA_xxxxx_20170925_114500.xxxxx_(fltarr_1354x2030x19).bin'

# import data

modis_cloud=read_modisbin(working_directory,cloud,2030,1354)
modis_lat=read_modisbin(working_directory,latitude,2030,1354)
modis_long=read_modisbin(working_directory,longitude,2030,1354)

modis_radiance=read_modis_radiance_bin(working_directory,radiance,2030,1354,19)

# export as .asc file

# get the header data
ncols=1354
nrows=2030

xllcorner=np.min(modis_long)
yllcorner=np.min(modis_lat)

cellsize=(np.max(modis_long)-np.min(modis_long))/2030
nodata_value=-9999

np.savetxt(working_directory+'test.out', modis_cloud, delimiter=' ',fmt='%1.0f')




