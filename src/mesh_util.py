import sys
sys.path.append('/home/maiqi/yalong/project/KeyPoint/Code/V2V-PoseNet-pytorch/lib/pyigllib')
import pyigl as igl
from iglhelpers import e2p
from igl_mesh_io import read_mesh_eigen


def read_mesh(filename):
    V, F = read_mesh_eigen(filename)
    return e2p(V), e2p(F)


def read_mesh_vertices(filename):
    V, _ = read_mesh_eigen(filename)
    return e2p(V)
