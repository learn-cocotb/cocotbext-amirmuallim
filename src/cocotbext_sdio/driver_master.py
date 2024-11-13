"""Driver when VIP is bus master."""

import cocotb


class MasterDriver:
    """Protocol driver."""

    def __init__(self):
        """Constructor."""

    def read(self, address: int, length: int = 4) -> bytes:
        """Read from dut."""
        cocotb.log.info(f"Dummy read got {address} {length} returning 4 bytes of 0")
        return int.to_bytes(0, 4, "little")

    def write(self, address: int, data: bytes) -> None:
        """Write to DUT."""
        cocotb.log.info(
            f"Dummy write  got {address} {data} doing nothing.",  # type:ignore[str-bytes-safe]
        )

    def anyothervipcmd(self) -> None:
        """Any other command that is mentioned in VIP document."""
