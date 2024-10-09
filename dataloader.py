
from __future__ import annotations
from parse import parse_xyz
import torch
from torch.utils import data
import os
from constants import ELEMENT_IX

ELEMENT_IX = {
    "H": 1,
    "He": 2,
    "Li": 3,
    "Be": 4,
    "B": 5,
    "C": 6,
    "N": 7,
    "O": 8,
    "F": 9,
    "Ne": 10,
    "Na": 11,
    "Mg": 12,
    "Al": 13,
    "Si": 14,
    "P": 15,
    "S": 16,
    "Cl": 17,
    "Ar": 18,
    "K": 19,
    "Ca": 20
}


class QM9Dataset(data.Dataset):
    """
    For loading batches of data from the QM9 dataset.
    """

    def __init__(
        self: QM9Dataset,
        folder: str,
    ) -> None:

        # Get the paths of all the files in the data folder
        self.paths = []
        for file in os.listdir(folder):
            if file.endswith('xyz'):
                self.paths.append(folder + '/' + file)

    def __getitem__(
        self: QM9Dataset,
        ix: int,
    ) -> tuple[torch.Tensor]:
        """
        Get the data from the .xyz file at index ix.
        """

        # Get the path that this index corresponds to
        path = self.paths[ix]
        # Load the coordinates and elements of the atom
        coordinates, elements, energy, charges = parse_xyz(path)
        # Convert the coordinates to a PyTorch tensor
        coordinates = ...
        # Convert the elements into integers using the ELEMENT_IX
        # dictionary
        elements = ...
        # Convert the elements to a PyTorch tensor
        elements = ...
        # Convert the energy to a PyTorch tensor
        energy = ...
        # Convert the charges to a PyTorch tensor
        charges = ...

        # Convert the coordinates and energies to
        # 32-bit floats
        coordinates = ...
        energy = ...
        charges = ...

        return coordinates, elements, energy, charges

    def __len__(
        self: QM9Dataset,
    ) -> int:
        """
        Return the number of datapoints in the dataset.
        """

        return len(self.paths)
