#
# spec file for package iperf
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


%define soname  0
Name:           iperf
Version:        3.12
Release:        0
Summary:        A tool to measure network performance
License:        BSD-3-Clause
Group:          Productivity/Networking/Diagnostic
URL:            https://software.es.net/iperf/
Source:         https://downloads.es.net/pub/iperf/iperf-%{version}.tar.gz
Source1:        https://downloads.es.net/pub/iperf/iperf-%{version}.tar.gz.sha256
Requires:       lib%{name}%{soname} = %{version}-%{release}
%if %{?sles_version} && %{?sles_version} <= 11
BuildRequires:  libuuid-devel
%else
BuildRequires:  pkgconfig(uuid)
%endif

%description
Iperf is a tool for active measurements of the maximum achievable bandwidth
on IP networks. It supports tuning of various parameters related to timing,
protocols, and buffers. For each test it reports the bandwidth, loss, and
other parameters.

This version, sometimes referred to as iperf3, is a redesign of an original
version developed at NLANR/DAST. iperf3 is a new implementation from scratch,
with the goal of a smaller, simpler code base, and a library version of the
functionality that can be used in other programs. iperf3 also a number of
features found in other tools such as nuttcp and netperf, but were missing
from the original iperf. These include, for example, a zero-copy mode and
optional JSON output.

Note that iperf3 is NOT backwards compatible with the original iperf.

%package -n lib%{name}%{soname}
Summary:        A library to measure network performance
Group:          Development/Libraries/C and C++

%description -n lib%{name}%{soname}
lib%{name} gives you access to all the functionality of the iperf3
network testing tool.
You can build it directly into your own program, instead of having
to run it as a shell command.

%package devel
Summary:        A tool to measure network performance
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{soname} = %{version}
%if %{?sles_version} && %{?sles_version} <= 11
Requires:       libuuid-devel
%else
Requires:       pkgconfig(uuid)
%endif

%description devel
Iperf is a tool for active measurements of the maximum achievable bandwidth
on IP networks. It supports tuning of various parameters related to timing,
protocols, and buffers. For each test it reports the bandwidth, loss, and
other parameters.

This package contains development files.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install

# cleanup empty libtool .la file
rm %{buildroot}%{_libdir}/lib%{name}.la

%post -n lib%{name}%{soname} -p /sbin/ldconfig
%postun -n lib%{name}%{soname} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md RELNOTES.md
%{_bindir}/%{name}3
%{_mandir}/man1/%{name}3.1%{?ext_man}

%files -n lib%{name}%{soname}
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%license LICENSE
%{_includedir}/%{name}_api.h
%{_libdir}/lib%{name}.so
%{_mandir}/man3/lib%{name}.3%{?ext_man}

%changelog
