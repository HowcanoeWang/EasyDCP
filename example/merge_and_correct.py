import __init__
import easydcp as dcp
#import open3d as o3d

plant_merge_list = ['S04/class[0]-plant2.ply', 'S04/class[0]-plant3.ply']
pcd_list = []
for ply_path in plant_merge_list:
    pcd = dcp.read_ply(ply_path)
    pcd_list.append(pcd)
m_pcd = dcp.merge_pcd(pcd_list)

#o3d.visualization.draw_geometries([m_pcd])

cla = dcp.Classifier(path_list=['training_data/fore_rm_y.png',
                            'training_data/back.png'],
                 kind_list=[0, -1], core='dtc')

plot1 = dcp.Plot('S04.ply', cla, show_steps=True)

plant_m = dcp.Plant(plot1, m_pcd, 0, 0)

out_dict = {'x(m)': [], 'y(m)': [],
            'width(m)': [], 'length(m)': [], 'hover_area(m2)': [],
            'height(m)': [], 'convex_volume(m3)': [], 'voxel_volume(m3)': []}
out_dict['x(m)']=plant_m.center[0]
out_dict['y(m)']=plant_m.center[1]
out_dict['width(m)']=plant_m.width
out_dict['length(m)']=plant_m.length
out_dict['hover_area(m2)']=plant_m.hull_area
out_dict['height(m)']=plant_m.height
out_dict['convex_volume(m3)']=plant_m.volume_hull_ground
out_dict['voxel_volume(m3)']=plant_m.volumn_voxel

print(out_dict)