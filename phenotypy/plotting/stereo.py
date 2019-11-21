import colorsys
import numpy as np
import open3d as o3d
from copy import copy

def show_pcd(pcd_list, window_name='Open3D', color=None):
    # color =
    #   None:  to display original color
    #   'Rand': to display a rand color
    #   [(0, 0.5, 1), ...]   max 1 for 255 color
    # todo: multi-progress
    if isinstance(color, str):
        show_list = []
        # generate distinguishable random colors
        num = len(pcd_list)
        dist_colors = []
        i = 0
        step = 360.0 / num
        while i < 360:
            h = i
            s = 90 + np.random.rand() * 10
            l = 50 + np.random.rand() * 10
            r, g, b = colorsys.hls_to_rgb(h / 360.0, l / 100.0, s / 100.0)
            dist_colors.append((r, g, b))
            i += step
        # apply colors
        for i, pcd in enumerate(pcd_list):
            pcd_copy = copy(pcd)
            pcd_copy.paint_uniform_color(dist_colors[i])
            show_list.append(pcd_copy)
    elif isinstance(color, list):
        show_list = []
        for i, c_tuple in enumerate(color):
            pcd_copy = copy(pcd_list[i])
            pcd_copy.paint_uniform_color(c_tuple)
            show_list.append(pcd_copy)
    else:  # color is None:
        show_list = pcd_list

    print('[3DPhenotyping][Visualizing] Visualizing, calculation paused')
    o3d.visualization.draw_geometries(show_list, window_name=window_name)