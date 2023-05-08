# Batch Radar Transform

This notebook allows to transform radar data provided by the **View of Delft** data set from the radar coordinate system to the relative lidar coordinate system.

You will need the **View of Delft** data set including radar pointclouds and their respective calib files for this notebook to work!

This project is largely based on the great work of the scientist at the TU Delft and their SDK for their data set. I just extracted parts of the code relevant for this exact use case. Please check out their SDK available [here](https://github.com/tudelft-iv/view-of-delft-dataset) for more information!

# Usage

1. Install the necessary packages (I use conda for this)
2. Create a `paths.py` file in the `helper` directory, containing a `paths` dictionary. The only path used so far is called `DELFT_DATASET`, which is the path to the root of the dataset (`/absolute/path/to/view_of_delft_PUBLIC`)

The transformed radar data will be placed in the newly created directory `view_of_delft_PUBLIC/radar/training/velodyne_transformed_to_lidar`.

_This was tested with python version 3.11.3._
