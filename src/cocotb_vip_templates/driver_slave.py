"""Driver when VIP is slave."""

import typing

import cocotb


class PrintCallback:
    """Only prints the parameters received."""

    def read(self, address: int, length: int = 4) -> bytes:
        """Read?"""
        cocotb.log.info(
            f"Dummy read callback got {address} {length}returning 4 bytes of 0",
        )
        return int.to_bytes(0, 4, "little")

    def write(self, address: int, data: bytes) -> None:
        """Write?"""
        cocotb.log.info(
            f"Dummy write callback got {address} {data} doing nothing.",  # type:ignore[str-bytes-safe]
        )

    def anyothervipcmd(self) -> None:
        """Any other command that is mentioned in VIP document."""


class SlaveDriver:
    """Fill This."""

    def __init__(self, *, callback: typing.Any = None):
        """Constructor."""
        if callback is None:
            callback = PrintCallback()
