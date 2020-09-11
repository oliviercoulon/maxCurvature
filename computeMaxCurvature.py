
import sys
import slam.io as sio
import slam.plot as splt
import slam.curvature as scurv
from slam import texture as stex
import numpy as np

def maxAbsCurvature(mesh):
    '''
    function that returns the maximum of the absolute value of the two
    principal curvatures.
    :param mesh: the input surface
    :return: texture
    '''
    PrincipalCurvatures, PrincipalDir1, PrincipalDir2 = scurv.curvatures_and_derivatives(mesh)
    maxCurv = np.max(np.absolute(PrincipalCurvatures), axis=0)
    return maxCurv

def main(arguments):
    if len(arguments)==3:
        meshN = arguments[1]
        texN = arguments[2]

        mesh = sio.load_mesh(meshN)

        maxCurv = maxAbsCurvature(mesh)

        # visb_sc = splt.visbrain_plot(mesh=mesh, tex=maxCurv,
        #                              caption='max absolute curvature',
        #                              cblabel='max absolute curvature')
        # visb_sc.preview()

        sio.write_texture(stex.TextureND(darray=maxCurv), texN)
    else:
        print('Usage:')
        print('python computeMaxCurvature.py mesh curvTex')

if __name__ == "__main__":
     arguments = sys.argv
     main(arguments)
