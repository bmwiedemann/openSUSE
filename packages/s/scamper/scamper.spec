#
# spec file for package scamper
#
# Copyright (c) 2024 SUSE LLC
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
Version:        20241112
Release:        0
Summary:        Parallel Internet measurement utility
License:        GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://www.caida.org/catalog/software/scamper/
Source:         https://www.caida.org/tools/measurement/%{name}/code/%{name}-cvs-%{version}.tar.gz
BuildRequires:  libopenssl-devel
# for the Python module
BuildRequires:  python3
BuildRequires:  python3-Cython
# for sc_uptime
BuildRequires:  pkgconfig(sqlite3)
# for sc_hoiho
BuildRequires:  pkgconfig(libpcre2-8)
#BuildRequires:  pkgconfig(libpcre)

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

This also contains the Python module.

%package -n libscamperfile9
Summary:        File access library for scamper's binary dump format
Group:          System/Libraries

%description -n libscamperfile9
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
Requires:       libscamperfile9 = %{version}-%{release}

%description -n libscamperfile-devel
Scamper is a program that is able to conduct Internet measurement
tasks to large numbers of IPv4 and IPv6 addresses, in parallel, to
fill a specified packets-per-second rate. Currently, it supports the
well-known ping and traceroute techniques, as well as MDA traceroute,
alias resolution, some parts of tbit, sting, and neighbour discovery.

This package contains development headers and other ancillary files for the
libscamperfile library.

%package -n libscamperctrl2
Summary:        Control library for scamper
Group:          System/Libraries
Obsoletes:      libscamperctl1 < %{version}

%description -n libscamperctrl2
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
Requires:       libscamperctrl2 = %{version}-%{release}

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
export PYTHON=%{_bindir}/python3
# disabled --with-pcre2 build since 20240229 because of build failure. Reported upstream
%configure --disable-static --disable-debug-file --enable-sc_uptime --with-python --enable-tests --enable-scamper-ring
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
pushd tests
make %{?_smp_mflags}
popd

%post   -n libscamperfile9 -p /sbin/ldconfig
%post   -n libscamperctrl2 -p /sbin/ldconfig
%postun -n libscamperfile9 -p /sbin/ldconfig
%postun -n libscamperctrl2 -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/sc_*
%{_bindir}/scamper
%{_mandir}/man1/*
%{_mandir}/man5/*
%{python3_sitelib}/scamper.so

%files -n libscamperfile9
%{_libdir}/libscamperfile.so.*

%files -n libscamperfile-devel
%{_includedir}/scamper_*
%{_libdir}/libscamperfile.so
%{_mandir}/man3/*

%files -n libscamperctrl2
%{_libdir}/libscamperctrl.so.*

%files -n libscamperctrl-devel
%{_includedir}/libscamperctrl.h
%{_libdir}/libscamperctrl.so

%changelog
