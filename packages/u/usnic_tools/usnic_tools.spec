#
# spec file for package usnic_tools
#
# Copyright (c) 2022 SUSE LLC
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


%define special_version %{nil}
Name:           usnic_tools
Version:        1.1.2.1
Release:        0
Summary:        Extract diagnostics and informational meta data out of Cisco usNIC devices
License:        BSD-2-Clause OR GPL-2.0-only
Group:          Productivity/Networking/System
URL:            https://www.cisco.com/
Source0:        https://github.com/cisco/usnic_tools/releases/download/v%{version}/usnic-tools-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  infinipath-psm-devel
BuildRequires:  libfabric-devel
ExclusiveArch:  x86_64

%description
This is a tool for extracting some diagnostics and informational
meta data out of Cisco usNIC devices using the Cisco usNIC extensions
in libfabric.

The usnic_devinfo executable will return information about usNIC
Linux devices.

%prep
%setup -q -n usnic-tools-%{version}

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/usnic_devinfo
%{_mandir}/man1/usnic_devinfo.*

%changelog
