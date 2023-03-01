import sys
sys.path.append("C:\\Users\\fnk\\PycharmProjects\\resipy_updated\\src")
from resipy import Project
import pyvista as pv
import time

if __name__ == '__main__':

    timings = {}
    t0 = time.time()
    k = Project(typ='R2')

    print("Importing_files")
    k.createPseudo3DSurvey(r'C:\\Users\\fnk\\PycharmProjects\\resipy_updated\\src\\examples\\Tobias\\Data',
                           lineSpacing=20, ftype="ResInv")

    print("Importing 3d file")
    k.importPseudo3DElec(r'C:/Users/fnk/PycharmProjects/resipy_updated/src/examples/Tobias/3d_fil/topo3d_ALL.csv')

    print("Meshing")
    k.createMultiMesh(typ='trian', show_output=False, dump=None, runParallel=True)
    k.showPseudo3DMesh(cropMesh=True)

    k.param['b_wgt'] = 0.05
    k.invertPseudo3D(runParallel=True)
    print("Inverted!")

    k.showResults(index=-1, cropMesh=False, color_map='jet', vmin=0.8, vmax=4,cropMaxDepth=False,clipContour=False)
    timings['Pseudo 3D'] = time.time() - t0
    k.saveProject(r'C:/Users/fnk/PycharmProjects/resipy_updated/src/examples/Tobias/Torvald_datafil.resipy')