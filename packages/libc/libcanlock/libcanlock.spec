#
# spec file for package libcanlock
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020-2024, Martin Hauke <mardnh@gmx.de>
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


%global sover   3
%global libname %{name}%{sover}
Name:           libcanlock
Version:        3.3.1
Release:        0
Summary:        Library for creating and verifying Usenet cancel locks
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://micha.freeshell.org/libcanlock/
Source:         https://micha.freeshell.org/libcanlock/src/%{name}-%{version}.tar.bz2
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig

%description
Cancel locks are used by Usenet article posters to authenticate their
authorship of an article. It may then by used by servers to prevent
cancel and supersede abuse. The use of this feature remains the
newsmaster's decision.

This library may be used for both the generation and the verification
of cancel locks.

%package -n %{libname}
Summary:        Library for creating and verifying Usenet cancel locks
Group:          System/Libraries

%description -n %{libname}
libcanlock is a library for creating and verifying RFC 8315 Netnews
Cancel-Locks. This implementation uses the recommended algorithm from
Section 4 with HMAC based on the same hash function as <scheme>.

This subpackage contains shared library part of libcanlock.

%package devel
Summary:        Development files for Usenet cancel lock library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
libcanlock is a library for creating and verifying RFC 8315 Netnews
Cancel-Locks. This implementation uses the recommended algorithm from
Section 4 with HMAC based on the same hash function as <scheme>.

This subpackage contains libraries and header files for developing
applications that want to make use of libcanlock.

%package -n canlock
Summary:        Utilities for creating and verifying Usenet cancel locks
Group:          Productivity/Networking/News/Utilities

%description -n canlock
Cancel locks are used by Usenet article posters to authenticate their
authorship of an article. It may then by used by servers to prevent
cancel and supersede abuse. The use of this feature remains the
newsmaster's decision.

This package contains a simple utility wrapping the canlock library,
which may be used for both the generation and the verification of
cancel locks, along with a message header parser and a header field
parser.

%prep
%setup -q

%build
%configure \
  --enable-pc-files
%make_build

%install
%make_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%check
%make_build test

%files -n %{libname}
%license COPYING
%doc ChangeLog README
%{_libdir}/libcanlock.so.%{sover}*
%{_libdir}/libcanlock-hp.so.%{sover}*

%files devel
%dir %{_includedir}/libcanlock-%{sover}
%{_includedir}/libcanlock-%{sover}/canlock.h
%{_includedir}/libcanlock-3/canlock-hp.h
%{_libdir}/libcanlock.so
%{_libdir}/libcanlock-hp.so
%{_libdir}/pkgconfig/libcanlock-3.pc
%{_libdir}/pkgconfig/libcanlock-hp-3.pc
%exclude %{_libdir}/libcanlock.a
%exclude %{_libdir}/libcanlock.la
%exclude %{_libdir}/libcanlock-hp.a
%exclude %{_libdir}/libcanlock-hp.la
%{_mandir}/man3/cl_clear_secret.3%{?ext_man}
%{_mandir}/man3/cl_get_key.3%{?ext_man}
%{_mandir}/man3/cl_get_lock.3%{?ext_man}
%{_mandir}/man3/cl_split.3%{?ext_man}
%{_mandir}/man3/cl_verify.3%{?ext_man}
%{_mandir}/man3/cl_hp_get_field.3%{?ext_man}
%{_mandir}/man3/cl_hp_parse_field.3%{?ext_man}
%{_mandir}/man3/cl_hp_unfold_field.3%{?ext_man}
%{_mandir}/man3/cl_verify_multi.3%{?ext_man}

%files -n canlock
%{_bindir}/canlock
%{_bindir}/canlock-hfp
%{_bindir}/canlock-mhp
%{_mandir}/man1/canlock.1%{?ext_man}
%{_mandir}/man1/canlock-hfp.1%{?ext_man}
%{_mandir}/man1/canlock-mhp.1%{?ext_man}

%changelog
