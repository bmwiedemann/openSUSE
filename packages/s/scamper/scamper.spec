#
# spec file for package scamper
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2016, Martin Hauke <mardnh@gmx.de>
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


Name:           scamper
Version:        20230224
Release:        0
Summary:        Parallel Internet measurement utility
License:        GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://www.caida.org/tools/measurement/scamper/
Source:         https://www.caida.org/tools/measurement/%{name}/code/%{name}-cvs-%{version}.tar.gz
BuildRequires:  libopenssl-devel
BuildRequires:  pkgconfig

%description
Scamper is a program that is able to conduct Internet measurement
tasks to large numbers of IPv4 and IPv6 addresses, in parallel, to
fill a specified packets-per-second rate. Currently, it supports the
well-known ping and traceroute techniques, as well as MDA traceroute,
alias resolution, some parts of tbit, sting, and neighbour discovery.

Scamper can do ICMP-based Path MTU discovery. scamper starts with the
outgoing interface's MTU and discovers the location of Path MTU
bottlenecks. scamper performs a PMTUD search when an ICMP
fragmentation required message is not returned to establish the PMTU
to the next point in the network, followed by a TTL limited search to
infer where the failure appears to occur.

%package -n libscamperfile4
Summary:        File access library for scamper's binary dump format
Group:          System/Libraries
Obsoletes:      libscamperfile1 < %{version}
Obsoletes:      libscamperfile2 < %{version}
Obsoletes:      libscamperfile3 < %{version}

%description -n libscamperfile4
Scamper is a program that is able to conduct Internet measurement
tasks to large numbers of IPv4 and IPv6 addresses, in parallel, to
fill a specified packets-per-second rate. Currently, it supports the
well-known ping and traceroute techniques, as well as MDA traceroute,
alias resolution, some parts of tbit, sting, and neighbour discovery.

This package contains the library that provides access to the binary output
files that scamper can produce in certain modes.

%package -n libscamperfile-devel
Summary:        Development headers for scamper's binary dump file access library
Group:          Development/Libraries/Other
Requires:       libscamperfile4 = %{version}-%{release}

%description -n libscamperfile-devel
Scamper is a program that is able to conduct Internet measurement
tasks to large numbers of IPv4 and IPv6 addresses, in parallel, to
fill a specified packets-per-second rate. Currently, it supports the
well-known ping and traceroute techniques, as well as MDA traceroute,
alias resolution, some parts of tbit, sting, and neighbour discovery.

This package contains development headers and other ancillary files for the
libscamperfile library.

%package -n libscamperctrl1
Summary:        Control library for scamper
Group:          System/Libraries

%description -n libscamperctrl1
Scamper is a program that is able to conduct Internet measurement
tasks to large numbers of IPv4 and IPv6 addresses, in parallel, to
fill a specified packets-per-second rate. Currently, it supports the
well-known ping and traceroute techniques, as well as MDA traceroute,
alias resolution, some parts of tbit, sting, and neighbour discovery.

This package contains thee library that provides functions to interact
with a collection of scamper instances.

%package -n libscamperctrl-devel
Summary:        Development headers for scamper's control library
Group:          Development/Libraries/Other
Requires:       libscamperctrl1 = %{version}-%{release}

%description -n libscamperctrl-devel
Scamper is a program that is able to conduct Internet measurement
tasks to large numbers of IPv4 and IPv6 addresses, in parallel, to
fill a specified packets-per-second rate. Currently, it supports the
well-known ping and traceroute techniques, as well as MDA traceroute,
alias resolution, some parts of tbit, sting, and neighbour discovery.

This package contains development headers and other ancillary files for the
libscamperctrl library.

%prep
%setup -q -n %{name}-cvs-%{version}

%build
%configure --disable-static --without-debugfile
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libscamperfile4 -p /sbin/ldconfig
%post   -n libscamperctrl1 -p /sbin/ldconfig
%postun -n libscamperfile4 -p /sbin/ldconfig
%postun -n libscamperctrl1 -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/sc_*
%{_bindir}/scamper
%{_mandir}/man1/*
%{_mandir}/man5/*

%files -n libscamperfile4
%{_libdir}/libscamperfile.so.*

%files -n libscamperfile-devel
%{_includedir}/scamper_*
%{_libdir}/libscamperfile.so
%{_mandir}/man3/*

%files -n libscamperctrl1
%{_libdir}/libscamperctrl.so.*

%files -n libscamperctrl-devel
%{_includedir}/libscamperctrl.h
%{_libdir}/libscamperctrl.so

%changelog
