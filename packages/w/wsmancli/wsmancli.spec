#
# spec file for package wsmancli
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


Name:           wsmancli
BuildRequires:  gcc-c++
BuildRequires:  libwsman-devel >= 2.5.1
BuildRequires:  libwsman_clientpp-devel >= 2.5.1
BuildRequires:  pkgconfig
%if 0%{?suse_version} > 1010
BuildRequires:  libcurl-devel
%else
# SLE 10
BuildRequires:  curl-devel
%endif
Version:        2.8.0
Release:        0
URL:            http://www.openwsman.org/
Summary:        Command line client utilities for WS-Management
License:        BSD-3-Clause
Group:          System/Management
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides 'wsman', a CLI utility for resource management
over the WS-Management protocol.

Also included is 'wseventmgr', a CLI utility for event management over
the WS-Management protocol.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%configure --disable-more-warnings
make %{?jobs:-j%jobs}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/wsman
%{_bindir}/wseventmgr
%{_mandir}/man1/wsman*
%{_mandir}/man1/wseventmgr*

%changelog
