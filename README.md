# iDEN Channel Calculator

A simple Project 25 iDEN channel information calculator. This script is a rewrite of the [iden_channel_calc](https://github.com/DVMProject/dvmhost/blob/master/iden_channel_calc.py) from [DVMProject/dvmhost](https://github.com/DVMProject/dvmhost).

## Installation

```shell
pip install git+https://github.com/k4yt3x/iden-channel-calculator.git
```

## Usages

Calculate channel information from channel number:

```shell
iden-channel-calculator -b 144000000 -c 100
```

Calculate channel information from TX frequency:

```shell
iden-channel-calculator -b 144000000 -t 145600000
```

View the help message to see how to specify more parameters (e.g., channel spacing):

```shell
iden-channel-calculator -h
```
