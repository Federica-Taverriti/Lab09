from dataclasses import dataclass
from model.aeroporto import Aeroporto


@dataclass
class Rotta:
    aeroportoP: Aeroporto
    aeroportoA: Aeroporto
    peso: int