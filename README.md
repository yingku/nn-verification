# nn-verification

# Getting Started

The model folder contains the files for deep neural network and deep transfer learning implementation.

We run the "PanGyn-DFI-5-MC-equal.py", "PanGyn-DFI-5-MC-inequal.py", "PanGyn-DFI-5-noMC-equal.py", "PanGyn-DFI-5-noMC-inequal.py" files within the simulation folder to generate our data for the independent learning scheme.

This data was plotted as box-and-whisker plots in R using the "BoxPlots.R" script and compared against the box plots from the Nature paper to verify our results. 

We convert this data from .xlsx format into .nnet file format using the "writeNNet.py" file under the "utils" foldr in the NNet-master repo.

We are currently running these .nnet files through Marabou.
