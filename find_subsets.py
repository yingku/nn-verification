import math

from typing import Iterable

from MarabouRepo.maraboupy import Marabou, MarabouNetworkNNet
import itertools


def find_subsets_just_over_half(layer, net):
    # type: (int, MarabouNetworkNNet) -> Iterable[int]
    layer_size = len(net.weights[layer])
    just_over_half = (layer_size + 1) // 2
    print "layer size: " + str(layer_size)
    print "number of subsets: " + str(math.factorial(layer_size) / (math.factorial(just_over_half) * math.factorial(layer_size - just_over_half)))
    return itertools.combinations(range(layer_size), just_over_half)


if __name__ == "__main__":
    net1 = Marabou.read_nnet("TL4HDR/Result/ccsa_transfer_0.model")
    subsets = list(find_subsets_just_over_half(0, net1))
    print subsets
