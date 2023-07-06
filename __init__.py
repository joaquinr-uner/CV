import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from scipy.spatial import Delaunay

from .dominio import dominio
from .esfera import esfera
from .fig_ejes3d_cv import fig_ejes3d_cv
from .fig_ejes_cv import fig_ejes_cv
from .gradiente import gradiente
from .intervalo import intervalo
from .plot3d_parametric_line_CV import plot3d_parametric_line_CV
from .plot_implicit_3d_cv import plot_implicit_3d_cv
from .punto3d_cv import punto3d_cv
from .punto_cv import punto_cv
from .sup_nivel_cv import sup_nivel_cv
from .tubo_3d import tubo_3d
from .vector3d_cv import vector3d_cv
from .vector_cv import vector_cv
from .surf2stil import tri_write
