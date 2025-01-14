#
# spec file for package gns3-server
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# Filter auto-generated deps from bundled shell script (which depends on busybox only)
%global __requires_exclude_from ^%{python3_sitelib}/gns3server/compute/docker/resources/.*$

%define gns3_user _gns3
%define gns3_group _gns3
%define gns3_home %{_sharedstatedir}/gns3
Name:           gns3-server
Version:        2.2.52
Release:        0
Summary:        A graphical network simulator
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            https://gns3.com/
Source0:        https://github.com/GNS3/gns3-server/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Source2:        %{name}.service
BuildRequires:  busybox
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       busybox
Requires:       cpulimit
Requires:       docker
Requires:       dynamips >= 0.2.11
Requires:       iouyap
Requires:       python3-Jinja2 >= 3.0.1
Requires:       python3-aiofiles >= 0.7
Requires:       python3-aiohttp >= 3.8.3
Requires:       python3-aiohttp_cors >= 0.7.0
Requires:       python3-async_timeout >= 4.0.2
Requires:       python3-distro >= 1.6.0
Requires:       python3-jsonschema >= 3.2.0
Requires:       python3-platformdirs
Requires:       python3-psutil >= 5.8.0
Requires:       python3-py-cpuinfo >= 8.0.0
Requires:       python3-sentry-sdk >= 1.12.1
Requires:       python3-truststore
%if 0%{?python3_version_nodots} < 39
Requires:       python3-importlib-resources >= 1.3
%endif
Requires:       qemu
Requires:       ubridge >= 0.9.14
Requires:       vpcs >= 0.5b1
Requires:       wireshark
BuildArch:      noarch
%if 0%{?suse_version}
Recommends:     virtualbox
%endif
Requires(pre):  shadow
%{?systemd_ordering}
Provides:       group(%gns3_group)
Provides:       user(%gns3_user)

%description
The GNS3 server manages emulators such as Dynamips, VirtualBox or Qemu/KVM.
Clients like the GNS3 GUI controls the server using a JSON-RPC API over Websockets.

You will need the new GNS3 GUI (gns3-gui repository) to control the server.

%prep
%autosetup -p1
find . -type f -name "*.py" -exec sed -i 's/^#!\/usr\/bin\/env python3/#!\/usr\/bin\/python3/' {} +
find . -type f -name "*.py" -exec sed -i 's/^#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' {} +
cp -f %{_bindir}/busybox gns3server/compute/docker/resources/bin/busybox
## Relax requirements
# Leap 15.2
sed -i -r 's/==/>=/g' requirements.txt
sed -i -r 's/distro>=1.7.*/distro>=1.6.0/' requirements.txt
sed -i -r 's/psutil>=5.9.4/psutil>=5.8.0/' requirements.txt
sed -i -r 's/aiofiles>=22.1.0/aiofiles>=0.7/' requirements.txt
sed -i -r 's/Jinja2>=3.1.2/jinja2>=3.0.1/' requirements.txt
sed -i -r 's/jsonschema>=4.17.3/jsonschema>=3.2.0/' requirements.txt
sed -i -r 's/py-cpuinfo>=9.0.0/py-cpuinfo>=8.0.0/' requirements.txt
sed -i -r '/setuptools/d' requirements.txt

%build
%if 0%{?suse_version} >= 1550
%python3_pyproject_wheel
%else
python3 setup.py build
%endif

%install
%if 0%{?suse_version} >= 1550
%python3_pyproject_install
%else
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}
%endif
rm %{buildroot}/%{python3_sitelib}/gns3server/static/.gitkeep
rm %{buildroot}/%{python3_sitelib}/gns3server/symbols/.gitkeep
find %{buildroot}/%{python3_sitelib}/gns3server -type f -name "*.py" -exec grep -Hl python3 {} + | xargs chmod +x
find %{buildroot}/%{python3_sitelib}/gns3server -name "*.svg" -exec chmod -x {} +
rm %{buildroot}/%{python3_sitelib}/gns3server/compute/docker/resources/bin/busybox
install -D -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -d %{buildroot}/%{_sharedstatedir}/gns3
%fdupes %{buildroot}/%{python3_sitelib}

%pre
%service_add_pre %{name}.service
# Create gns3 user/group
getent group %{gns3_group} >/dev/null || groupadd -r %{gns3_group}
getent passwd %{gns3_user} >/dev/null || useradd -r -g %{gns3_group} -d %{gns3_home} -s /sbin/nologin -c "GNS3 service user" %{gns3_user}
exit 0

%post
%service_add_post %{name}.service
# Replace bundled busybox with the system one
cp -f %{_bindir}/busybox %{python3_sitelib}/gns3server/compute/docker/resources/bin/busybox

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/gns3server
%{_bindir}/gns3vmnet
%{_bindir}/gns3loopback
%{_sbindir}/rc%{name}
%{python3_sitelib}/gns3server
%{python3_sitelib}/gns3_server-%{version}*-info
%ghost %{python3_sitelib}/gns3server/compute/docker/resources/bin/busybox
%dir %attr(0750,%{gns3_user},%{gns3_group}) %{_sharedstatedir}/gns3
%{_unitdir}/%{name}.service

%changelog
