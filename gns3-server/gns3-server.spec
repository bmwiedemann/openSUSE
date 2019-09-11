#
# spec file for package gns3-server
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gns3-server
Version:        2.1.16
Release:        0
Summary:        A graphical network simulator
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            https://gns3.com/
Source0:        https://github.com/GNS3/gns3-server/archive/v%{version}.tar.gz
Source1:        %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM gns3-server-timeout-fix.patch
Patch0:         gns3-server-timeout-fix.patch
# PATCH-FIX-UPSTREAM gns3-server-requirements-fix.patch
Patch1:         gns3-server-requirements-fix.patch
BuildRequires:  busybox
BuildRequires:  python3-devel >= 3.3
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
Requires:       busybox
Requires:       cpulimit
Requires:       docker
Requires:       dynamips >= 0.2.11
Requires:       iouyap
Requires:       python3-Jinja2 >= 2.7.3
Requires:       python3-aiohttp >= 0.21.5
Requires:       python3-aiohttp-cors
Requires:       python3-docker-py >= 1.4.0
Requires:       python3-jsonschema >= 2.4.0
Requires:       python3-prompt_toolkit1
Requires:       python3-psutil >= 3.0.0
Requires:       python3-raven >= 5.2.0
Requires:       python3-typing_extensions
Requires:       python3-zipstream >= 1.1.3
Requires:       qemu
Requires:       ubridge >= 0.9.14
Requires:       vpcs >= 0.5b1
Requires:       wireshark
BuildArch:      noarch
%if 0%{?suse_version}
Recommends:     virtualbox
%endif

%description
The GNS3 server manages emulators such as Dynamips, VirtualBox or Qemu/KVM.
Clients like the GNS3 GUI controls the server using a JSON-RPC API over Websockets.

You will need the new GNS3 GUI (gns3-gui repository) to control the server.

%prep
%setup -q -n gns3-server-%{version}
%patch0 -p1
%patch1 -p1
find . -type f -name "*.py" -exec sed -i 's/^#!\/usr\/bin\/env python3/#!\/usr\/bin\/python3/' {} +
find . -type f -name "*.py" -exec sed -i 's/^#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' {} +

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}
rm -rf %{buildroot}/%{python3_sitelib}/gns3server/symbols/.gitkeep
find %{buildroot}/%{python3_sitelib}/gns3server -type f -name "*.py" -exec grep -Hl python3 {} + | xargs chmod +x
find %{buildroot}/%{python3_sitelib}/gns3server -name "*.svg" -exec chmod -x {} +

rm -rf %{buildroot}/%{python3_sitelib}/tests
rm -rf %{buildroot}/%{python3_sitelib}/gns3server/compute/docker/resources/bin/busybox
ln -sf %{_bindir}/busybox %{buildroot}/%{python3_sitelib}/gns3server/compute/docker/resources/bin/busybox

%files
%defattr(-, root, root, 0755)
%license LICENSE
%doc AUTHORS README.rst
%{_bindir}/gns3server
%{_bindir}/gns3vmnet
%{_bindir}/gns3loopback
%{python3_sitelib}/gns3server
%{python3_sitelib}/gns3_server-%{version}-py%{py3_ver}.egg-info

%changelog
