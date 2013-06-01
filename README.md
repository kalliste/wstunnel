wstunnel
========

A WebSocket tunneling software written in python on top of tornado http://www.tornadoweb.org/ web framework for asynchronous I/O.


Quick start
===========

The standalone way
------------------

`wstunneld.py` is the script to start both sides of the tunnel

    $ ./wstunnel.py --help
    usage: wstunneld.py [-h] [-c CONF_FILE]

    WebSocket tunnel endpoint

    optional arguments:
      -h, --help            show this help message and exit
      -c CONF_FILE, --config CONF_FILE
                            path to a configuration file


The configuration file is in YAML syntax. The following is an example of telnet mapping

Tunnel Client side

```yaml
endpoint: client
ws_url: ws://localhost:9000/

proxies:
    /telnet:
      port: 50023
      filters: []
```

Tunnel Server side

```yaml
endpoint: server
listen: 9000
ssl: no
ssl_options:
  certfile: null
  keyfile: null

proxies:
  /telnet:
    address: 192.168.1.2:23
    filters: [wstunnel.filters.DumpFilter]
```

As a warm up you can edit the provided `conf/client.yml` and `conf/server.yml` and run each side separately

    $ ./wstunneld.py -c conf/client.yml

    $ ./wstunneld.py -c conf/server.yml


The API way
-----------

You can use the tunneling endpoints in your code. Check the test suite for examples.

    $ python setup.py install

By default, a `DumpFilter` class is provided to hex dump all network traffic.
I'm planning to extend the plugin feature so this will change very soon.

The developer way
-------------------

If you want to help me and contribute, start by cloning the repo

    $ git clone https://github.com/ffalcinelli/wstunnel wstunnel

Create a `virtualenv`, it's a recommended practice, and install the dependecies using `pip`

    $ pip install -r requirements.txt

Happy hacking :-)

TODOs
=====

1. "Daemonize" the standalone way. A Windows Service would be nice for the Microsoft's platform.
2. Create 2 different executables for client and server tunnels (maybe `wstuncltd` and `wstunsrvd`?). Explicit is better than implicit.
3. Enhance the `filter` support with custom configuration from yaml files.

License
=======

LGPLv3

Copyright (c) 2013 Fabio Falcinelli <fabio.falcinelli@gmail.com>

> This program is free software: you can redistribute it and/or modify
> it under the terms of the GNU Lesser General Public License as published by
> the Free Software Foundation, either version 3 of the License, or
> (at your option) any later version.
>
> This program is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
> GNU Lesser General Public License for more details.
>
> You should have received a copy of the GNU Lesser General Public License
> along with this program.  If not, see <http://www.gnu.org/licenses/>.


This file was modified by PyCharm 2.7.2 for binding GitHub repository