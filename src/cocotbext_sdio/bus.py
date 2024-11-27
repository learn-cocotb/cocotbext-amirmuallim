"""Bus."""

import cocotb
from cocotb_bus.bus import Bus as BusBaseClass


class SDIOBus:
    """Bus class for SDIO."""

    def __init__(
        self,
        dut: cocotb.SigHandle,
        prefix: str = "",
        suffix: str = "",
        bus_seperator: str = "_",
        clk: str = "clk",
        reset: str = "rst_n",
        active_high_reset: bool = True,
        uppercase: bool = False,
    ):
        """Constructor for?

        Args:
        dut (SimHandle): ...
        prefix (str):...
        """

    def get_bus(self) -> BusBaseClass:
        """Creates and returns the bus object."""
        return BusBaseClass()

    def get_somespecialfunction_bus(self, params: int) -> BusBaseClass:
        """This function handles a special signal naming convention seen in this protocol that is not covered by the default bus structure and creates and returns the bus.

        Args:
            params (int):...
        """
        cocotb.log.info(params)
        return BusBaseClass()
