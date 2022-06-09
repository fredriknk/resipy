import sys
sys.path.append("C:/Users/fnk/PycharmProjects/resipy_fnk/src")
from resipy import Project
import pyvista as pv
import time


if __name__ == '__main__':

    timings = {}
    t0 = time.time()
    k = Project(typ='R2')

    k.createPseudo3DSurvey(r'C:/Users/fnk/PycharmProjects/resipy_fnk/src/examples/test/data',
                           lineSpacing=20, ftype="ResInv")

    k.importPseudo3DElec(r'C:/Users/fnk/PycharmProjects/Resipy_interpolate/topofiles/electrodes3d.csv')

    k.createMultiMesh(typ='trian', show_output=False, dump=None, runParallel=True)
    k.showPseudo3DMesh(cropMesh=True)
    k.param['b_wgt'] = 0.05
    k.invertPseudo3D(runParallel=True)

    k.showResults(index=-1, cropMesh=False, color_map='jet', vmin=0.8, vmax=4,cropMaxDepth=False,clipContour=False)
    timings['Pseudo 3D'] = time.time() - t0
    k.saveProject(r'/home/fredrikfnk/PycharmProjects/resipy/src/examples/test/JN_Pseudo3D_Willington.resipy')