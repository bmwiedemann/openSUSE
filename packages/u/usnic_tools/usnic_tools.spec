#
# spec file for package usnic_tools
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define special_version %{nil}

Name:           usnic_tools
Summary:        Extract diagnostics and informational meta data out of Cisco usNIC devices
License:        BSD-2-Clause OR GPL-2.0
Group:          Productivity/Networking/System
Version:        1.1.2.0
Release:        0
Source0:        usnic_tools-%{version}%{special_version}.tar.xz
Url:            http://www.cisco.com
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  infinipath-psm-devel
BuildRequires:  libfabric-devel

%description
This is a tool for extracting some diagnostics and informational
meta data out of Cisco usNIC devices using the Cisco usNIC extensions
in libfabric.

The usnic_devinfo executable will return information about usNIC
Linux devices.

%prep
%setup -q -n usnic_tools-%{version}

%build
./autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-, root, root)
%{_bindir}/usnic_devinfo
%{_mandir}/man1/usnic_devinfo.*
%doc COPYING

%changelog
