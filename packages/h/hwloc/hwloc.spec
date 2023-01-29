#
# spec file for package hwloc
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

%global lname libhwloc15
Name:           hwloc
Version:        2.9.0
Release:        0
Summary:        Portable Hardware Locality
License:        BSD-3-Clause
Group:          Productivity/Clustering/Computing
URL:            https://www.open-mpi.org/projects/hwloc/
Source0:        https://download.open-mpi.org/release/hwloc/v2.9/hwloc-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libnuma-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(x11)
Requires:       %{lname} = %{version}-%{release}
Requires:       perl-JSON
Requires:       perl-base >= 5.18.2
Requires(post): desktop-file-utils
Requires(postun):desktop-file-utils
%{?systemd_ordering}

%description
The Portable Hardware Locality (hwloc) software package provides
an abstraction (across OS, versions, architectures, ...)
of the hierarchical topology of modern architectures, including
NUMA memory nodes, shared caches, processor sockets, processor cores
and processing units (logical processors or "threads"). It also gathers
various system attributes such as cache and memory information. It primarily
aims at helping applications with gathering information about modern
computing hardware so as to exploit it accordingly and efficiently.

hwloc may display the topology in multiple convenient formats.
It also offers a powerful programming interface (C API) to gather information
about the hardware, bind processes, and much more.

%package devel
Summary:        Headers and shared development libraries for hwloc
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Provides:       libhwloc-devel = %{version}
Obsoletes:      libhwloc-devel < %{version}
Obsoletes:      libhwloc-devel = 0.0.0

%description devel
This package contains the headers and shared object symbolic links
for the hwloc.

%package -n %{lname}
Summary:        Runtime libraries for hwloc
Group:          System/Libraries
Requires:       %{name}-data

%description -n %{lname}
This package contains the run time libraries for hwloc.

%package data
Summary:        Run time data for hwloc
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description data
This package contains the run time data for the hwloc.

%package doc
Summary:        Documentation for hwloc
Group:          Documentation/Other
BuildArch:      noarch

%description doc
This package contains the documentation for hwloc.

%prep
%setup -q

%build
autoreconf -fvi

%configure \
    --disable-silent-rules
%make_build

%install
%make_install
%suse_update_desktop_file -r lstopo System Monitor
# We don't ship .la files.
rm -rf %{buildroot}%{_libdir}/libhwloc.la

# documentation will be handled by % doc macro
rm -rf %{buildroot}%{_datadir}/doc/

# This binary is built only for intel architectures
%ifarch %{ix86} x86_64
install -D -m 644 %{buildroot}%{_datadir}/hwloc/hwloc-dump-hwdata.service %{buildroot}%{_unitdir}/hwloc-dump-hwdata.service
%endif
rm %{buildroot}%{_datadir}/hwloc/hwloc-dump-hwdata.service

%fdupes -s %{buildroot}/%{_mandir}/man1
%fdupes -s %{buildroot}/%{_mandir}/man7

%check
#XXX: this is weird, but make check got broken by removing doxygen-doc/man above
#     the only one fix is to install documentation by hand, or to ignore check error
%make_build check || :

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%ifarch %{ix86} x86_64
%pre
%service_add_pre hwloc-dump-hwdata.service
%endif

%post
%ifarch %{ix86} x86_64
%service_add_post hwloc-dump-hwdata.service
%endif
%desktop_database_post

%ifarch %{ix86} x86_64
%preun
%service_del_preun hwloc-dump-hwdata.service
%endif

%postun
%ifarch %{ix86} x86_64
%service_del_postun hwloc-dump-hwdata.service
%endif

%desktop_database_postun

%files
%license COPYING
%doc NEWS README VERSION
%{_mandir}/man7/hwloc*
%{_mandir}/man1/hwloc*
%{_mandir}/man1/lstopo*
%{_bindir}/hwloc*
%{_bindir}/lstopo*
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/%{name}
%ifarch %{ix86} x86_64
%attr(0755,root,root) %{_sbindir}/hwloc-dump-hwdata
%{_unitdir}/hwloc-dump-hwdata.service
%endif

%files devel
%{_includedir}/hwloc
%{_includedir}/hwloc.h
%{_libdir}/libhwloc.so
%{_libdir}/pkgconfig/hwloc.pc

%files -n %{lname}
%{_libdir}/libhwloc*so.*

%files data
%dir %{_datadir}/hwloc
%dir %{_datadir}/hwloc/hwloc-ps.www
%{_datadir}/hwloc/hwloc.dtd
%{_datadir}/hwloc/hwloc2-diff.dtd
%{_datadir}/hwloc/hwloc2.dtd
%{_datadir}/hwloc/hwloc-valgrind.supp
%{_datadir}/hwloc/hwloc-ps.www/*

%files doc
%doc ./doc/doxygen-doc/html/*
%{_mandir}/man3/*

%changelog
