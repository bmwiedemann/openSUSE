# vim: set sw=4 ts=4 et nu:
#
# spec file for package userspace-rcu
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define soname  8
Name:           userspace-rcu
Version:        0.14.0
Release:        0
Summary:        Userspace Read-Copy-Update Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND GPL-3.0-or-later
Group:          System/Libraries
URL:            https://liburcu.org/
Source0:        https://lttng.org/files/urcu/userspace-rcu-%{version}.tar.bz2
Source1:        https://lttng.org/files/urcu/userspace-rcu-%{version}.tar.bz2.asc
Source2:        userspace-rcu.keyring
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  pkgconfig

%description
liburcu is a LGPLv2.1 userspace RCU (read-copy-update) library. This data
synchronization library provides read-side access which scales linearly with
the number of cores. It does so by allowing multiples copies of a given data
structure to live at the same time, and by monitoring the data structure
accesses to detect grace periods after which memory reclamation is possible.

%package -n liburcu%{soname}
Summary:        Userspace Read-Copy-Update Library
Group:          System/Libraries

%description -n liburcu%{soname}
liburcu is a LGPLv2.1 userspace RCU (read-copy-update) library. This data
synchronization library provides read-side access which scales linearly with
the number of cores. It does so by allowing multiples copies of a given data
structure to live at the same time, and by monitoring the data structure
accesses to detect grace periods after which memory reclamation is possible.

Accesses to detect grace periods after which memory reclamation is possible.

%package -n liburcu-devel
Summary:        Userspace Read-Copy-Update Library
Group:          Development/Libraries/C and C++
Requires:       liburcu%{soname} = %{version}

%description -n liburcu-devel
liburcu is a LGPLv2.1 userspace RCU (read-copy-update) library. This data
synchronization library provides read-side access which scales linearly with
the number of cores. It does so by allowing multiples copies of a given data
structure to live at the same time, and by monitoring the data structure
accesses to detect grace periods after which memory reclamation is possible.

%prep
%setup -q

%build
%configure --disable-silent-rules --disable-static
%make_build

%install
%make_install

rm -rf "%{buildroot}%{_datadir}/doc"
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n liburcu%{soname} -p /sbin/ldconfig
%postun -n liburcu%{soname} -p /sbin/ldconfig

%files -n liburcu%{soname}
%license LICENSE
%doc ChangeLog README.md *.txt doc/*.md
%{_libdir}/liburcu.so.%{soname}
%{_libdir}/liburcu.so.%{soname}.*
%{_libdir}/liburcu-bp.so.%{soname}
%{_libdir}/liburcu-bp.so.%{soname}.*
%{_libdir}/liburcu-cds.so.%{soname}
%{_libdir}/liburcu-cds.so.%{soname}.*
%{_libdir}/liburcu-common.so.%{soname}
%{_libdir}/liburcu-common.so.%{soname}.*
%{_libdir}/liburcu-mb.so.%{soname}
%{_libdir}/liburcu-mb.so.%{soname}.*
%{_libdir}/liburcu-memb.so.%{soname}
%{_libdir}/liburcu-memb.so.%{soname}.*
%{_libdir}/liburcu-qsbr.so.%{soname}
%{_libdir}/liburcu-qsbr.so.%{soname}.*
%{_libdir}/liburcu-signal.so.%{soname}
%{_libdir}/liburcu-signal.so.%{soname}.*

%files -n liburcu-devel
%{_includedir}/urcu*.h
%{_includedir}/urcu
%{_libdir}/liburcu.so
%{_libdir}/liburcu-bp.so
%{_libdir}/liburcu-cds.so
%{_libdir}/liburcu-common.so
%{_libdir}/liburcu-mb.so
%{_libdir}/liburcu-memb.so
%{_libdir}/liburcu-qsbr.so
%{_libdir}/liburcu-signal.so
%{_libdir}/pkgconfig/liburcu.pc
%{_libdir}/pkgconfig/liburcu-bp.pc
%{_libdir}/pkgconfig/liburcu-cds.pc
%{_libdir}/pkgconfig/liburcu-mb.pc
%{_libdir}/pkgconfig/liburcu-memb.pc
%{_libdir}/pkgconfig/liburcu-qsbr.pc
%{_libdir}/pkgconfig/liburcu-signal.pc

%changelog
