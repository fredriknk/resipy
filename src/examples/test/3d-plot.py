import sys
sys.path.append("C:/Users/erlin/PycharmProjects/resipy-fnk/src")
from resipy import Project
import geopandas as gpd
import numpy as np
import pandas as pd
import pyvista as pv
import time
import matplotlib
matplotlib.use("Qt5Agg")
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
    k.loadProject("data/malin_psuedo3d (1).resipy")
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



    sargs = dict(fmt="%.0f", color='black')

    bounds = [6.122e+05, 6.140e+05, 6.65101e+06, 6.6509e+06, 0, 1.760e+02]
    topo = mesh.warp_by_scalar(scalars="Elevation [m]")#, factor=3.0)
    topo = topo.clip('z', invert=False, origin=(0, 0, 0))
    topo = topo.clip_box(bounds)
    topo = topo.texture_map_to_plane(use_bounds=True)#, inplace=True)
    topo = topo.translate([0, 0, -40])

    # map = "Maps\eksport_4417235_07042022\Eksport-nib.tif"
    # map = "Maps\eksport_4417238_07042022\Eksport-nib.tif"
    map = "Maps/TEST_EXPORT_FLYFOTO_DEPONIGRENSE.tif"
    src = rasterio.open(map)

    array = src.read(1)

    gdf = gpd.read_file("Maps/DEPONIGRENSE_PUNKTER.dxf")
    #
    gdf = gdf.boundary
    # gdf_B.boundary.to_file('deponigrense.shp')
    # gdf = gpd.read_file("Maps/DEPONIGRENSE.gpkg")
    # gdf = gpd.read_file("Maps/Deponigrense.shp")
    #
    # gdf_lineslines = gg.visualization.create_delaunay_mesh_from_gdf(gdf)
    # gdf.plot()
    # plt.show()

    texture = pv.numpy_to_texture(array)

    ax = pv.Plotter()
    ax.add_mesh(topo, texture=texture)
    # ax.add_lines(gdf.geometry.values)
    # ax.add_mesh(gdf.boundary)
    # p.add_mesh(mesh=topo, cmap='gist_earth', scalar_bar_args=sargs, clim=[0, 500])
    ax.set_background('white')
    ax.show_grid(color='black')
    # p.show(cpos='xy')
    # k.showPseudo()
    # k.showInvError(index=0)
    # k.showPseudoInvError(index=0)
    # k.showResults(index=0, edge_color="none", contour=True, sens=True, attr="Resistivity(log10)", vmin=1.2, vmax=2.5, color_map="viridis", sensPrc=0.50, doi=False, doiSens=False)

    k.showResults(index=-1, ax=ax, cropMesh=False, color_map='jet', vmin=1.2, vmax=2, cropMaxDepth=False, contour=True,
                    elec_color="k", elec_size=4., pvshow=True)

