# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:49:26 2017

@author: Shakur
"""
import geopandas as gpd
fp = "path/to/shapefile"
out = "path/to/shapefile"
def project(fp):
    gdf = gpd.read_file(fp)
    #gdf_crs = gdf.crs()
    if 'geometry' in gdf.columns:
        gdf_proj = gdf.copy()
        gdf_proj = gdf_proj.to_crs(epsg=????) # Provide the epsg number of your projection
         
    gdf_proj.to_file(out)
project(fp)  