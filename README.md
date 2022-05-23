# nn-verification

## Setup
Create a virtual environment with Python 2.7

Install dependencies: `pip install pip install -r requirements.txt`

The Lasagne version available on PyPi is out of date. Install it separately with
`pip install --upgrade https://github.com/Lasagne/Lasagne/archive/5d3c63cb315c50b1cbd27a6bc8664b406f34dd99.zip`

If you get an error like `ImportError: No module named TL4HDR.data.preProcess`, try setting the `PYTHONPATH` environment
variable to the empty string. On Linux, `export PYTHONPATH=` has resolved this issue.

## Getting Started

The model folder contains the files for deep neural network and deep transfer learning implementation.

We run the "PanGyn-DFI-5-MC-equal.py", "PanGyn-DFI-5-MC-inequal.py", "PanGyn-DFI-5-noMC-equal.py", "PanGyn-DFI-5-noMC-inequal.py" files within the simulation folder to generate our data for the independent learning scheme.

This data was plotted as box-and-whisker plots in R using the "BoxPlots.R" script and compared against the box plots from the Nature paper to verify our results. 

We convert this data from .xlsx format into .nnet file format using the "writeNNet.py" file under the "utils" foldr in the NNet-master repo.

We are currently running these .nnet files through Marabou.
