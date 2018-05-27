EmPOWER: Mobile Networks Operating System
=========================================

### What is EmPOWER?
EmPOWER is a new network operating system designed for heterogeneous mobile networks.

### Top-Level Features
* Supports both LTE and WiFi radio access networks
* Northbound abstractions for a global network view, network graph, and
  application intents.
* REST API and native (Python) API for accessing the Northbound abstractions
* Support for Click-based Lightweight Virtual Networks Functions
* Declarative VNF chaning on precise portion of the flowspace
* Flexible southbound interface supporting WiFi APs LTE eNBs

Checkout out our [website](http://empower.create-net.org/) and our [wiki](https://github.com/5g-empower/empower-runtime/wiki)

This repository contains the empower-manager applicattion.

Code is released under the Apache License, Version 2.0.

### Installation

    git clone https://github.com/5g-empower/empower-manager
    cd empower-manager
    python setup.py install

### Usage
List all WTPs currently defined:

    $ empower-manager --no-passwd list-wtps
    00:0D:B9:2F:56:64 last seen 0
    00:0D:B9:2F:56:58 last seen 0
    00:0D:B9:2F:56:5C last seen 0
    00:0D:B9:2F:56:B4 last seen 0

### Options

    -h, --help            show this help message and exit
    -r HOST, --host HOST  REST server address; default='127.0.0.1'
    -p PORT, --port PORT  REST server port; default=8888
    -u USER, --user USER  EmPOWER admin user; default='root'
    -n, --no-passwd       Run without password; default false
    -f PASSWDFILE, --passwd-file PASSWDFILE
                        Password file; default=none
    -t TRANSPORT, --transport TRANSPORT
                        Specify the transport; default='http'
