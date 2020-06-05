# ansible-role-openvpn-exporter

[![Build Status](https://travis-ci.org/patrickjahns/ansible-role-openvpn-exporter.svg?branch=master)](https://travis-ci.org/patrickjahns/ansible-role-openvpn-exporter)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-patrickjahns.openvpn_exporter-blue.svg)](https://galaxy.ansible.com/patrickjahns/openvpn_exporter/)
[![GitHub tag](https://img.shields.io/github/tag/patrickjahns/ansible-role-openvpn-exporter.svg)](https://github.com/patrickjahns/ansible-role-openvpn-exporter/tags)

## Description

Deploy [openvpn_exporter](//github.com/patrickjahns/openvpn_exporter) using ansible.
For recent changes, please check the [CHANGELOG](/CHANGELOG.md) or have a look at [github releases](https://github.com/patrickjahns/ansible-role-openvpn_exporter/releases)


## Requirements

- Ansible >= 2.7 

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name                                      | Default Value    | Description                                                             |
| ----------------------------------------- | ---------------- | ------------------------------------------------------------------------|
| `openvpn_exporter_version`                | 1.1.1            | The version of the [openvpn_eporter](https://github.com/patrickjahns/openvpn_exporter/releases) to install |
| `openvpn_exporter_system_user`            | openvpn_exporter | User that openvpn_exporter will run as |
| `openvpn_exporter_system_group`           | openvpn_exporter | Groups the openvpn_exporter user belongs to |
| `openvpn_exporter_user_additional_groups` | ""               | Additional groups the openvpn_exporter user should belong to (i.e. openvpn) |
| `openvpn_exporter_install_dir`            | /opt/openvpn_exporter | Directory in wich openvpn_exporter will be installed |
| `openvpn_exporter_config_web_address`     | ""               | [see openvpn_exporter](https://github.com/patrickjahns/openvpn_exporter#usage) |
| `openvpn_exporter_config_web_path`        | ""               | [see openvpn_exporter](https://github.com/patrickjahns/openvpn_exporter#usage) |
| `openvpn_exporter_config_web_root`        | ""               | [see openvpn_exporter](https://github.com/patrickjahns/openvpn_exporter#usage) |
| `openvpn_exporter_disable_client_metrics` | False            | [see openvpn_exporter](https://github.com/patrickjahns/openvpn_exporter#usage) |
| `openvpn_exporter_config_enable_golang_metrics` | False      | [see openvpn_exporter](https://github.com/patrickjahns/openvpn_exporter#usage) |
| `openvpn_exporter_config_log_level`       | "info"           | [see openvpn_exporter](https://github.com/patrickjahns/openvpn_exporter#usage) |
| `openvpn_exporter_config_status_files`    | []               | Path(s) to the status files - [see openvpn_exporter](https://github.com/patrickjahns/openvpn_exporter#usage) |

## Example Playbook

```yaml
---
- hosts: all
  roles:
    - role: patrickjahns.openvpn_exporter
      vars:
        openvpn_exporter_config_status_files:
          - /etc/openvpn/server1.status
          - servername:/etc/openvpn/server2.status
```

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v3.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system.
We are using tox to simplify process of testing on multiple ansible versions. To install tox execute:
```sh
pip3 install tox
```
To run tests on all ansible versions (WARNING: this can take some time)
```sh
tox
```
To run a custom molecule command on custom environment with only default test scenario:
```sh
tox -e ansible29 -- molecule test -s default
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

If you would like to run tests on remote docker host just specify `DOCKER_HOST` variable before running tox tests.

## CI

### Travis
Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix which will take more time than local testing, so please be patient.

### Github Actions
Additionally to TravisCI some github actions are run to perform static code analysis

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.

## Maintainers and Contributors

- [Patrick Jahns](https://github.com/patrickjahns)
