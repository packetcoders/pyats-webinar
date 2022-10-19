#!/usr/bin/bash

# Note: run from the root of the repo.

# Exporting the environment variables from the .env file.
export $(cat .env)

# Setting the path to the examples folder.
PYATS_EXAMPLE_PATH=examples/

# Performing a diff between the outputs from the pre and post Genie learns.
# devices.
pyats diff \
    $PYATS_EXAMPLE_PATH/output/diff/pre/ \
    $PYATS_EXAMPLE_PATH/output/diff/post/ \
    --output $PYATS_EXAMPLE_PATH/output/diff/result