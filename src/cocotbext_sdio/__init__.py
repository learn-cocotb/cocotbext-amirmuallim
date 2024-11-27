"""Cocotb VIP package for SDIO IP."""

from __future__ import annotations

from cocotbext_sdio.bus import SDIOBus
from cocotbext_sdio.config import Config
from cocotbext_sdio.driver import SDIODriver
from cocotbext_sdio.driver_master import SDIOMasterDriver
from cocotbext_sdio.driver_slave import SDIOSlaveDriver
from cocotbext_sdio.monitor import SDIOMonitor

# from cooctbext_sdio.debug import ... # not understood yet

__all__: list[str] = [
    "SDIOBus",
    "Config",
    "SDIODriver",
    "SDIOMasterDriver",
    "SDIOSlaveDriver",
    "SDIOMonitor",
]
