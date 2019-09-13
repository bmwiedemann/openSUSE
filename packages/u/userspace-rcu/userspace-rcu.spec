# vim: set sw=4 ts=4 et nu:
#
# spec file for package userspace-rcu
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           userspace-rcu
Version:        0.10.0
Release:        0
%define soname  6
Summary:        Userspace Read-Copy-Update Library
License:        LGPL-2.1+ and MIT and GPL-2.0+ and GPL-3.0+
Group:          System/Libraries
Source0:        http://lttng.org/files/urcu/userspace-rcu-%{version}.tar.bz2
Source1:        http://lttng.org/files/urcu/userspace-rcu-%{version}.tar.bz2.asc
Source2:        userspace-rcu.keyring
Source99:       baselibs.conf
Url:            http://lttng.org/urcu
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libtool
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
autoreconf -fi
%configure --disable-silent-rules --disable-static
%__make %{?_smp_mflags}

%install
%makeinstall

rm -rf "%{buildroot}%{_datadir}/doc"
rm "%buildroot/%_libdir"/*.la

%post   -n liburcu%{soname} -p /sbin/ldconfig
%postun -n liburcu%{soname} -p /sbin/ldconfig

%files -n liburcu%{soname}
%defattr(-,root,root)
%doc ChangeLog LICENSE README.md *.txt doc/*.md
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
%{_libdir}/liburcu-qsbr.so.%{soname}
%{_libdir}/liburcu-qsbr.so.%{soname}.*
%{_libdir}/liburcu-signal.so.%{soname}
%{_libdir}/liburcu-signal.so.%{soname}.*

%files -n liburcu-devel
%defattr(-,root,root)
%{_includedir}/urcu*.h
%{_includedir}/urcu
%{_libdir}/liburcu.so
%{_libdir}/liburcu-bp.so
%{_libdir}/liburcu-cds.so
%{_libdir}/liburcu-common.so
%{_libdir}/liburcu-mb.so
%{_libdir}/liburcu-qsbr.so
%{_libdir}/liburcu-signal.so
%{_libdir}/pkgconfig/liburcu.pc
%{_libdir}/pkgconfig/liburcu-bp.pc
%{_libdir}/pkgconfig/liburcu-cds.pc
%{_libdir}/pkgconfig/liburcu-mb.pc
%{_libdir}/pkgconfig/liburcu-qsbr.pc
%{_libdir}/pkgconfig/liburcu-signal.pc

%changelog
