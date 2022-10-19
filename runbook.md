# Runbook (Internal)

## pyATS Components

## Install

```
pip3 install "pyats[full]"

pyats version check --outdated

pyats version update
```

## CLI vs Python

* `pyats --help`
* show basic connection



## Demos

* First show the repo.
* Show the different ways to install
* Show the tesbed

### Parse /w Rich
Highlight key points to script:
* Multi-processing
* Genie Parse
* Dq
* Rich tables

## Diff via the Diff+Shell
* `./examples/003_genie_diff_pre_1.sh`
* Change interface on spine1
```
conf t
int Eth1/1
  shut
  end
copy run start
```
* `./examples/005_genie_diff_compare_3.sh`
