#!/usr/bin/env python

from dotenv import load_dotenv
from genie import testbed
from genie.utils import Dq
from pyats.datastructures.logic import And
from rich.console import Console
from rich.table import Table

# Load .env into environment variables
load_dotenv()

# Load the testbed
testbed = testbed.load("testbed.yml")

# Select the device we want to test
devices = testbed.find_devices(os=And("(nxos)"))

# Connecting to the devices in the testbed.
testbed.connect(*devices)

# Parsing the output of the command "show interface" on the devices in the devices variable.
output = testbed.parse("show interface", devices=devices)

# Using the Dq library to filter the output to only show interfaces with out_discards.
output = Dq(output).contains("out_discard").reconstruct()

# Creating a table object with the title "Interface Errors".
table = Table(title="Interface Errors")

# Creating the table headers.
table.add_column("Device", justify="left", style="cyan", no_wrap=True)
table.add_column("Interface", style="magenta")
table.add_column("OutDiscards", justify="left", style="red")

# Iterating over the output dictionary and adding the data to the table.
for device, interfaces in output.items():
    for interface, counters in interfaces.items():
        table.add_row(device, interface, str(counters["counters"]["out_discard"]))

# Creating a console object.
console = Console()

# Printing the table object.
console.print(table)
