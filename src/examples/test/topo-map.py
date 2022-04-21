"""
.. _ref_topo_map_example:

Topographic Map
~~~~~~~~~~~~~~~

This is very similar to the :ref:`ref_texture_example` example except it is
focused on plotting aerial imagery from a GeoTIFF on top of some topography
mesh.
"""
# sphinx_gallery_thumbnail_number = 4

import pyvista as pv
from pyvista import examples
from osgeo import gdal
import numpy as np
import gemgis as gg
import rasterio

filename2 = "Maps/clipped raster2.tif"

fn = filename2
mesh = gg.visualization.read_raster(path=fn ,nodata_val=0.,name='Elevation [m]')

dem = rasterio.open(fn)
import matplotlib.pyplot as plt

im = plt.imshow(dem.read(1), cmap='gist_earth', vmin=0, vmax=500)
cbar = plt.colorbar(im)
cbar.set_label('m')
plt.show()

sargs = dict(fmt="%.0f", color='black')

bounds = [6.122e+05,6.140e+05,6.65101e+06,6.6509e+06,0,1.760e+02]
topo = mesh.warp_by_scalar(scalars="Elevation [m]")#, factor=15.0)
topo  = topo.clip('z', invert=False,origin=(0,0,0))
topo = topo.clip_box(bounds)
topo = topo.texture_map_to_plane(use_bounds=True, inplace=True)

map =  "Maps\eksport_4417235_07042022\Eksport-nib.tif"
map = "Maps\eksport_4417238_07042022\Eksport-nib.tif"
src = rasterio.open(map)
array = src.read(1)

texture = pv.numpy_to_texture(array)

p = pv.Plotter()
p.add_mesh(topo, texture=texture)
#p.add_mesh(mesh=topo, cmap='gist_earth', scalar_bar_args=sargs, clim=[0, 500])
p.set_background('white')
p.show_grid(color='black')
p.show(cpos='xy')
