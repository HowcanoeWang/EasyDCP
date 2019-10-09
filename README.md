# 3Dphenotyping

An auto python scripts for batch image processing, and common phenotype traits extraction from 3D point clouds.

## Installation

unzip all files to the `plugins` folder in Agisoft installation paths, e.g. `C:\Program Files\Agisoft\Metashape Pro\plugins\3Dphenotyping`

Right click the `install_packages.bat`，and edit the start paths to your Agisoft path:

`D:\Your_path_to\Agisoft\Metashape Pro\python\python.exe" -m pip install -r requirements.txt`

And then run `install_packages.bat` in Administrator permission, the batch file will automatically install all the packages required for this project.

Add Metashape program folder to Windows PATH
See https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/

## Functions

**Agisoft auto control**

* [ ] Auto match key points
* [ ] Auto points cloud generation
* [ ] Auto points cloud output
* [ ] Batch processing

**Phenotype Processing**

* [ ] Decision tree classifier for plant pixel classification
* [ ] Cluster algorithm for individual plant segmentation
* [ ] Plant width, length, and height calculation

## Using Agisoft auto control

open pipeline1.py
-change 'path_folders' to the path containing the folders of images
-change 'blur_threshold' to desired value. Pipeline will disable all images with Agisoft image quality below the blur_threshold.
