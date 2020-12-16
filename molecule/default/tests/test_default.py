import os
import pytest
import yaml
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleDefaults():
    with open("./defaults/main.yml", 'r') as stream:
        return yaml.full_load(stream)


@pytest.mark.parametrize("dir", [
    "/opt/openvpn_exporter"
])
def test_directories(host, dir):
    d = host.file(dir)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/etc/default/openvpn_exporter",
    "/etc/systemd/system/openvpn_exporter.service",
    "/usr/local/bin/openvpn_exporter",
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_user(host):
    assert host.group("openvpn_exporter").exists
    assert host.user("openvpn_exporter").exists


def test_service(host):
    s = host.service("openvpn_exporter")
    assert s.is_running


def test_http_socket(host):
    s = host.socket("tcp://0.0.0.0:9176")
    assert s.is_listening


def test_version(host, AnsibleDefaults):
    version = os.getenv('OPENVPN_EXPORTER',
                        AnsibleDefaults['openvpn_exporter_version'])
    out = host.run("/usr/local/bin/openvpn_exporter --version").stdout
    assert "openvpn_exporter version v" + version in out
