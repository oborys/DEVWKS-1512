## Module 4: Jinja2 for better Ansible, NetBox etc.

NetBox is an open source web application designed to help manage and document computer networks. Initially conceived by the network engineering team at DigitalOcean, NetBox was developed specifically to address the needs of network and infrastructure engineers. It encompasses the following aspects of network management:

- IP address management (IPAM) - IP networks and addresses, VRFs, and VLANs
- Equipment racks - Organized by group and site
- Devices - Types of devices and where they are installed
- Connections - Network, console, and power connections among devices
- Virtualization - Virtual machines and clusters
- Data circuits - Long-haul communications circuits and providers
- Secrets - Encrypted storage of sensitive credentials

```
interfaces {
{% for item in vars_from_netbox_api %}
    {{ item.interface }} {
        unit 0 {
            family inet {
                address {{ item.address }};
            }
        }
    }
{% endfor %}
}
protocols {
    lldp {
{% for item in vars_from_netbox_api %}
        interface "{{ item.interface }}";
{% endfor %}
    }
}

```

```
configure terminal
{% for item in ip_interfaces %}
  interface {{ item.interface }}
    description {{ item.description }}
    ipv4 address {{ item.ip }}{{ item.cidr }}
{% if feed.mbps != "" %}
    service-policy input {{ item.mbps }}Mb
    service-policy output {{ item.mbps }}Mb
{% endif %}
    no shutdown
    exit
{% endfor %}

```


```
#!/bin/bash

export http_proxy={{ http_proxy }}
export https_proxy={{ https_proxy }}
{% if no_proxy is defined -%}
export no_proxy={{ no_proxy | join(',')}}
{%- endif %}

```
## [Return to the Table of Contents](README.md)
