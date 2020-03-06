# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _OnPrem


class _Network(_OnPrem):
    _type = "network"
    _icon_dir = "resources/onprem/network"


class Apache(_Network):
    _icon = "apache.png"


class Caddy(_Network):
    _icon = "caddy.png"


class Consul(_Network):
    _icon = "consul.png"


class Envoy(_Network):
    _icon = "envoy.png"


class Etcd(_Network):
    _icon = "etcd.png"


class Haproxy(_Network):
    _icon = "haproxy.png"


class Istio(_Network):
    _icon = "istio.png"


class Kong(_Network):
    _icon = "kong.png"


class Linkerd(_Network):
    _icon = "linkerd.png"


class Nginx(_Network):
    _icon = "nginx.png"


class Tomcat(_Network):
    _icon = "tomcat.png"


class Traefik(_Network):
    _icon = "traefik.png"


class Zookeeper(_Network):
    _icon = "zookeeper.png"


# Aliases

ETCD = Etcd
HAProxy = Haproxy