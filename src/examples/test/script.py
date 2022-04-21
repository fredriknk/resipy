import sys
sys.path.append("C:/Users/fnk/PycharmProjects/resipy_fnk/src")
from resipy import Project
import pyvista as pv
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    timings = {}
    t0 = time.time()
    k = Project(typ='R2')
    # k.createPseudo3DSurvey(r'C:/Users/fnk/PycharmProjects/resipy_fnk/src/examples/test/data',
    #                        lineSpacing=20, ftype="ResInv")
    # k.importPseudo3DElec(r'C:/Users/fnk/PycharmProjects/Resipy_interpolate/topofiles/electrodes3d.csv')
    # k.createMultiMesh(typ='trian', show_output=False, dump=None, runParallel=True)

    # k.param['b_wgt'] = 0.05
    # k.invertPseudo3D(runParallel=True)
    #
    # timings['Pseudo 3D'] = time.time() - t0
    # k.saveProject(r'C:/Users/fnk/PycharmProjects/resipy_fnk/src/examples/test/JN_Pseudo3D_Willington.resipy')

    # k.loadProject(r'C:/Users/fnk/PycharmProjects/resipy_fnk/src/examples/test/JN_Pseudo3D_Willington.resipy')
    k.loadProject("C:/Users/fnk/Downloads/malin_psuedo3d (1).resipy")
    # k.showPseudo3DMesh(cropMesh=True)

    import pyvista as pv
    from pyvista import examples
    from osgeo import gdal
    import numpy as np
    import gemgis as gg
    import rasterio

    filename2 = "Maps/clipped raster2.tif"

    fn = filename2
    mesh = gg.visualization.read_raster(path=fn, nodata_val=0., name='Elevation [m]')

    dem = rasterio.open(fn)
    import matplotlib.pyplot as plt

    im = plt.imshow(dem.read(1), cmap='gist_earth', vmin=0, vmax=500)
    cbar = plt.colorbar(im)
    cbar.set_label('m')
    plt.show()

    sargs = dict(fmt="%.0f", color='black')

    bounds = [6.122e+05, 6.140e+05, 6.65101e+06, 6.6509e+06, 0, 1.760e+02]
    topo = mesh.warp_by_scalar(scalars="Elevation [m]")  # , factor=15.0)
    topo = topo.clip('z', invert=False, origin=(0, 0, 0))
    topo = topo.clip_box(bounds)
    topo = topo.texture_map_to_plane(use_bounds=True, inplace=True)
    topo = topo.translate([0, 0, -40])

    # map = "Maps\eksport_4417235_07042022\Eksport-nib.tif"
    map = "Maps\eksport_4417238_07042022\Eksport-nib.tif"
    src = rasterio.open(map)
    array = src.read(1)

    texture = pv.numpy_to_texture(array)
    # topo.translate([0,0,-40])
    ax = pv.Plotter()
    ax.add_mesh(topo, texture=texture)
    # p.add_mesh(mesh=topo, cmap='gist_earth', scalar_bar_args=sargs, clim=[0, 500])
    ax.set_background('white')
    ax.show_grid(color='black')
    # p.show(cpos='xy')

    k.showResults(index=-1, ax=ax, cropMesh=False, color_map='jet', vmin=0.8, vmax=4, cropMaxDepth=False, contour=True,
                  use_pyvista=True, elec_color="k", elec_size=4., pvshow=True)
