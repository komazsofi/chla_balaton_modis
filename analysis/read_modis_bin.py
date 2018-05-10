'''

'''

import numpy as np
import os

import matplotlib.pyplot as plt

def read_modisbin(working_directory,filename,dimx,dimy):
 modis_cloud_wrashape=np.fromfile(working_directory+filename, dtype=np.float32)
 modis_cloud = modis_cloud_wrashape.reshape(dimx,dimy)
 return modis_cloud

########################################################################################################## 

working_directory='C:/zsofia/Amsterdam/GitHub/komazsofi/chla_balaton_modis/data/'
filename='Cloudmask_1KM_AQUA_xxxxx_20170925_114500.xxxxx_(fltarr_1354x2030).bin'
latitude='Lat_1KM_AQUA_xxxxx_20170925_114500.xxxxx_(fltarr_1354x2030).bin'
longitude='Lon_1KM_AQUA_xxxxx_20170925_114500.xxxxx_(fltarr_1354x2030).bin'

#modis_cloud_wrashape=np.fromfile(working_directory+filename, dtype=np.float32)
#modis_cloud = modis_cloud_wrashape.reshape(2030,1354)

modis_cloud=read_modisbin(working_directory,filename,2030,1354)
modis_lat=read_modisbin(working_directory,latitude,2030,1354)
modis_long=read_modisbin(working_directory,longitude,2030,1354)

#plt.imshow(modis_cloud)
#plt.colorbar()
#plt.show()



