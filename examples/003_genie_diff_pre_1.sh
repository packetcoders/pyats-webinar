#!/usr/bin/bash

# Note: run from the root of the repo.

# Exporting the environment variables from the .env file.
export $(cat .env)

# Setting the path to the examples folder.
PYATS_EXAMPLE_PATH=examples/

# Running an `ospf`, `routing` and `interface` learn on the `spine1-nxos`, `spine2-nxos`, `leaf1-ios`, and `leaf2-ios`
# devices.
pyats learn ospf routing interface \
      --devices spine1-nxos spine2-nxos leaf1-ios leaf2-ios \
      --testbed-file testbed.yml \
      --output $PYATS_EXAMPLE_PATH/output/diff/pre