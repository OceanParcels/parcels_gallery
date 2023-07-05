# parcels_gallery
The Gallery repository of Parcels, including scripts and example renderings to visualise Lagrangian ocean flow.

## To see the published plot gallery website, see: [https://oceanparcels.org/#gallery](https://oceanparcels.org/#gallery)

## How to add a picture to the Gallery

 - clone the repo : git clone https://github.com/OceanParcels/parcels_gallery.git
 - git branch <my_plot>
 - git checkout <my_plot>
 - cp yourplot.png images/
 - cp yourplot.ipynb scripts_ipynb/
 (- cp yourplot.py scripts_py/)
 - git add *
 - git commit -m "<your_short_plot_name> plot for the gallery"
 - git push origin <my_plot>
 - go to https://github.com/OceanParcels/parcels_gallery and click on pull request to add your pull request (appears at top of page)
 - wait for your request to be merged

## 
To have the table in the jupyter-notebook template showing the version of the python packages: <br>
conda install -c conda-forge version_information

# Binder address

https://mybinder.org/v2/gh/OceanParcels/parcels_gallery/HEAD

(https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/OceanParcels/parcels_gallery/HEAD)
