# pyATS Webinar

This repo contains code, and examples from the Packet Coders pyATS webinar.
The 2 demos that are included within this repo are:
* **Example 1 - Create an interface error report**.
* **Example 2 - Perform a maintenance diff check**.

The recording of the webinar can be viewed here (TBC).

## Environment Setup

To setup your environment to use the examples within this repo perform the following:


1.  Create a virtual environment
To isolate the installation of your Python dependancies create a virtual environment.
```
python3 -m venv .venv
```

2. Activate virtual environment
Enter your virtual environment
```
source .venv/bin/activiate
```

3. Install dependancies
Install the various Python dependancies via PIP:
```
pip install -r requirements.txt
```

4. Add credentials to .env
Add your device credentials to .env. Like so:
```
cp .env-example .env
vim .env
PYATS_UNAME=### <--- update
PYATS_PWORD=### <--- update
```

**Note:** If you are running these examples against your own network please ensure you update the testbed.yml accordingly.

## Example 1 - Interface Error Report
This example is based upon creating an interface error report for out_discards (via Python) using:
* Genie Parse
* Pcall
* Dq
* Rich

You can run the script like so:
```
$ ./examples/002_genie_parse_w_rich.py
```

## Example 2 - Maintenance Diff Check
This example is based upon diff`ing the network pre and post a network change (via the pyATS CLI) using:
* Genie Learn
* Genie Diff

To run this demo perform the following:
1. Take a snapshot of the network (pre change):
```
$ ./examples/003_genie_diff_pre_1.sh`
```
2. Make the network change(s).
3. Take a snapshot of the network (post change):
```
$ ./examples/004_genie_diff_post_2.sh
```
4. Perform a diff between the pre and post change snapshots.
```
$ ./examples/005_genie_diff_compare_3.sh
```

