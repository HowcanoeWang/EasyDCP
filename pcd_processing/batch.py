from phenotyping import *

cla = Classifier(path_list=['F:/ply/training_data/fore.png',
                            'F:/ply/training_data/back.png'],
                 kind_list=[0, -1], core='dtc')

# batch processing
plot_set = ['F:/ply/S01.ply', 'F:/ply/S02.ply', 'F:/ply/S03.ply', 'F:/ply/S04.ply', 'F:/ply/S05.ply', 'F:/ply/S06 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S07 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S08 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S09 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S10 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S11 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S12 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S13 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S14 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S15 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S16 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S17 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S18 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S19 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S20 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S21 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S22 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S23 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S24 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S25 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S26 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S27 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S28 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S29 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S30 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S31 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S32 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S33 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S34 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S35 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply', 'F:/ply/S36 - 00000 - ALLSTEPS-v27-med - MetashapeDenseCloud.ply']
# empty list for batch processing
result_container = []

for plot in plot_set:
    # show_steps=True to display output among calculation to check correct or not
    plot_class = Plot(plot, cla, show_steps=False)
    # if need to save points among calculation for checking or other software
    plot_class.write_ply()
    result_container.append(plot_class.traits)

plot_all = pd.concat(result_container, axis=0).reset_index()
plot_all.to_csv('F:/ply/out/plot_alloutputs-batch2.csv', index=False)