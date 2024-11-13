"""Configuration for the VIP.

The VIP will require configuration related to timing parameters, clock generators etc.
Define a config class which allows changing the VIP behavior.
"""


class Config:
    """Fill this."""

    def __init__(self, param_a: int = 1, param_b: int = 2, xyz: bool = True):
        """Describe what the constructor does. describe all the parameters."""
        self.param_a = param_a
        self.param_b = param_b
        self.xyz = xyz

    def set_xyz(self, new_xyz: bool) -> None:
        """Describe what this setter does."""
        self.xyz = new_xyz
