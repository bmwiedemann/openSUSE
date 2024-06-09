#
# spec file for package clknetsim
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


Name:           clknetsim
Version:        0+git.20240424
Release:        0
Summary:        Clock and Network Simulator
License:        GPL-2.0-only
URL:            https://github.com/mlichvar/clknetsim
Source:         %{name}-%{version}.tar.gz
BuildRequires:  gcc-c++

%description
clknetsim is a tool designed to test programs which synchronize the system
clock, either over network or from a hardware reference clock. It simulates
a system or a number of systems connected to each other in a network and
the tested programs discipline the simulated system clocks. It can be used
to quickly test how well the programs control the system clocks in various
conditions or to test the network protocols.

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC"

%install
install -D -p -m 0755 clknetsim    %{buildroot}%{_bindir}/clknetsim
install -D -p -m 0755 clknetsim.so %{buildroot}%{_libdir}/clknetsim.so

%files
%license COPYING
%doc README
%{_bindir}/clknetsim
%{_libdir}/clknetsim.so

%changelog
