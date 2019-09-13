#
# spec file for package gns3-net-converter
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gns3-net-converter
Summary:        Convert old ini-style GNS3 topologies
License:        GPL-3.0+
Group:          Productivity/Networking/Other
Version:        1.3.0
Release:        0
Url:            https://pypi.python.org/pypi/gns3-net-converter
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  python3-devel >= 3.3
BuildRequires:  python3-setuptools
Provides:       gns3-converter = %{version}
Obsoletes:      gns3-converter < %{version}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GNS3 Converter is designed to convert old ini-style GNS3 topologies (<=0.8.7) to
the newer version v1+ JSON format for use in GNS3 v1+

The converter will convert all IOS, Cloud and VirtualBox devices to the new format.
It will also convert all QEMU based devices (QEMU VM, ASA, PIX, JUNOS & IDS).
VPCS nodes will be converted to cloud devices due to lack of information the 0.8.7 topology files.

For topologies containing snapshots, the snapshots will also be converted to the new format automatically.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}
chmod -x %{buildroot}/%{python3_sitelib}/gns3converter/configspec

%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog README.rst
%{_bindir}/gns3-converter
%{python3_sitelib}/*

%changelog
