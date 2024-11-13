[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/98GX9mcv)
# Cocotb VIP templates

[![ci](https://github.com/dyumnin-interns/cocotb-vip-templates/workflows/ci/badge.svg)](https://github.com/dyumnin-interns/cocotb-vip-templates/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://dyumnin-interns.github.io/cocotb-vip-templates/)
[![pypi version](https://img.shields.io/pypi/v/cocotb-vip-templates.svg)](https://pypi.org/project/cocotb-vip-templates/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-blue.svg?style=flat)](https://gitpod.io/#https://github.com/dyumnin-interns/cocotb-vip-templates)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#cocotb-vip-templates:gitter.im)

  # cocotbext-sdio

The `cocotbext-sdio` project provides a Verification IP (VIP) for the SDIO protocol using Cocotb.

## Features

- Command transmission
- Data read/write
- CRC checking

## Installation

```bash
pip install cocotbext-sdio
```
## Usage
```python
from cocotbext_sdio import SdioDriver, SdioMonitor

driver = SdioDriver(dut, "", dut.clk)
monitor = SdioMonitor(dut, "", dut.clk)
```
## Example Test
```python
@cocotb.test()
async def test_sdio_command(dut):
    driver = SdioDriver(dut, "", dut.clk)
    await driver.send_command(0x00, 0x00000000)
```
