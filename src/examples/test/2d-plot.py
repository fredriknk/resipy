import sys
sys.path.append("C:/Users/fnk/PycharmProjects/resipy-fnk3/src")
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


    profiles = {0:"PROFILA_1m_20210720.EE",
                1:"PROFILA_5m_20210716",
                2:"PROFILB_5m_20211106(1)",
                3:"PROFILC_1m_20210713.EE",
                4:"PROFILC_5m_20210712",
                5:"PROFILD_1m_del1_20210722.EE",
                6:"PROFILD_1m_del2_20210723.EE",
                7:"PROFILD_5m_20210721.EE",
                8:"PROFILE_1m_del1.EE",
                9:"PROFILE_1m_del2_20211019",
                10:"PROFILE_5m_20211018.EE",
                11:"Profil_F_1m_del1_20211027.EE",
                12:"Profil_F_1m_del2_20211029.EE",
                13:"Profil_F_5m_20211025.EE"}

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

    #
    profile_no = 0
    print(profiles[profile_no])
    fig,ax = plt.subplots()
    ax.set_title(profiles[profile_no])

    k.showResults(index=profile_no,ax=ax, cropMesh=False, color_map='jet', vmin=1.2, vmax=2, cropMaxDepth=False, contour=True,
                   elec_color="k", elec_size=4.)

    profile_no = 1
    print(profiles[profile_no])
    fig, ax = plt.subplots()
    ax.set_title(profiles[profile_no])

    k.showResults(index=profile_no, ax=ax, cropMesh=False, color_map='jet', vmin=1.2, vmax=2, cropMaxDepth=False,
                  contour=True,
                  elec_color="k", elec_size=4.)

    k.saveInvPlots(attr='Conductivity(mS/m)',
                   outputdir="C:\\Users\\fnk\PycharmProjects\\resipy-fnk3\\src\\examples\\test")

    """ Displays a 2d mesh and attribute.

            Parameters
            ----------
            color_map : string, optional
                color map reference 
            color_bar : Boolean, optional 
                `True` to plot colorbar 
            xlim : tuple, optional
                Axis x limits as `(xmin, xmax)`.
            zlim : tuple, optional
                Axis z limits as `(zmin, zmax)`. 
            ax : matplotlib axis handle, optional
                Axis handle if preexisting (error will thrown up if not) figure is to be cast to.
            electrodes : boolean, optional
                Enter true to add electrodes to plot.
            sens : boolean, optional
                Enter true to plot sensitivities. 
            edge_color : string, optional
                Color of the cell edges, set to `None` if you dont want an edge.
            contour : boolean, optional
                If `True`, plot filled with contours instead of the mesh.
            vmin : float, optional
                Minimum limit for the color bar scale.
            vmax : float, optional
                Maximum limit for the color bar scale.
            attr : string, optional
                Which attribute in the mesh to plot, references a dictionary of attributes. attr is passed 
                as the key for this dictionary.
            clabel : string, optional
                Label of the colorbar. Default is the value of `attr` argument.
            hor_cbar : boolean, optional
                'True' to make a horizontal color bar at the bottom of the plot, default
                is vertical color bar to the right of the plot. 
            sensPrc : float, optional
                Normalised (between 0 and 1) sensitivity value threshold. Default
                is None meaning the sensitivity is just overlay. Need `sens=True` 
                to be used.
            maxDepth : float 
                Maximum absolute depth to be shown on the plotted figure. 
            aspect : string, optional
                defines the aspect ratio of the plot.
                'equal' locks the aspect ratio.
                'auto', aspect ratio is define by plotting area.
            darkMode : bool, optional
                If True, electrodes will be plotted in white, else black

            Returns
            -------
            figure : matplotlib figure 
                Figure handle for the plotted mesh object.

            Notes
            -----
            Show a mesh object using matplotlib. The color map variable should be 
            a string refering to the color map you want (default is "jet").
            As we're using the matplotlib package here any color map avialable within 
            matplotlib package can be used to display the mesh here also. See: 
            https://matplotlib.org/2.0.2/examples/color/colormaps_reference.html
            """

