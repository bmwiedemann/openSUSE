# vim: set sw=4 ts=4 et nu:
#
# spec file for package openpgm
#
# Copyright (c) 2020 SUSE LLC
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/
%define major       5.2
%define mpkg        5_2
%define soname      0
%define tarball_version 5-2-122
%define libname     libpgm-%{mpkg}-%{soname}
Name:           openpgm
Version:        5.2.122
Release:        0
Summary:        OpenPGM implementation of the Reliable Multicast Protocol
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/steve-o/openpgm
Source:         https://github.com/steve-o/openpgm/archive/release-5-2-122.tar.gz#/openpgm-release-%{tarball_version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM bmwiedemann https://github.com/steve-o/openpgm/pull/48
Patch0:         libpgm-5.2.122-reproducible.patch
# PATCH-FIX-UPSTREAM bluca https://github.com/steve-o/openpgm/pull/58
Patch1:         libpgm-5.2.122-reproducible-architecture.patch
# PATCH-FIX-UPSTREAM bluca https://github.com/steve-o/openpgm/pull/57
Patch2:         libpgm-5.2.122-pkg-config-do-not-add-I-to-non-existing-directory.patch
# upstream pending patch https://github.com/steve-o/openpgm/pull/63
Patch3:         libpgm-5.2.122-configure-rdtsc-checking-chg.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python-devel

%description
OpenPGM is an implementation of the Pragmatic General Multicast (PGM)
specification in RFC 3208. PGM is a reliable and scalable multicast protocol
that enables receivers to detect loss, request retransmission of lost data, or
notify an application of unrecoverable loss.

%package -n %{libname}
Summary:        PGM Reliable Multicast Protocol library
Group:          System/Libraries

%description -n %{libname}
OpenPGM is an implementation of the Pragmatic General Multicast (PGM)
specification in RFC 3208. PGM is a reliable and scalable multicast protocol
that enables receivers to detect loss, request retransmission of lost data, or
notify an application of unrecoverable loss.

%package devel
Summary:        Development files for the OpenPGM Reliable Multicast Protocol library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
OpenPGM is an implementation of the Pragmatic General Multicast (PGM)
specification in RFC 3208. PGM is a reliable and scalable multicast protocol
that enables receivers to detect loss, request retransmission of lost data, or
notify an application of unrecoverable loss.

This subpackage contains the header files for OpenPGM.

%prep
%setup -q -n "%{name}-release-%{tarball_version}/openpgm/pgm"
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export ac_cv_func_ftime=no
mkdir -p m4
autoreconf -fi
%{configure} \
    --disable-static

%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/libpgm.la

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%license COPYING LICENSE
%{_libdir}/libpgm-%{major}.so.%{soname}
%{_libdir}/libpgm-%{major}.so.%{soname}.*

%files devel
%defattr(-,root,root)
%doc mibs/PGM-MIB-petrova-01.txt
%{_includedir}/pgm-%{major}
%{_libdir}/libpgm.so
%{_libdir}/pkgconfig/openpgm-%{major}.pc

%changelog
