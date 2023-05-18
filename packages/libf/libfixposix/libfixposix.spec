#
# spec file for package libfixposix
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname libfixposix
%define sover 4
Name:           libfixposix
Version:        0.5.1
Release:        0
Summary:        POSIX syscall wrappers
License:        BSL-1.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/sionescu/libfixposix
Source:         https://github.com/sionescu/libfixposix/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Thin wrapper over POSIX syscalls.

%package -n     %{soname}%{sover}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n %{soname}%{sover}
Thin wrapper over POSIX syscalls.
The purpose of libfixposix is to offer replacements for parts of POSIX
whose behaviour is inconsistent across *NIX flavours.

This package contains the shared library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}

%description    devel
Thin wrapper over POSIX syscalls.

This package contains the pkgconfig, header files and libraries needed to
develop application that use %{name}.

%prep
%setup -q

%build
autoreconf -fiv
%configure

make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%license LICENCE
%doc README.md VERSION
%{_libdir}/libfixposix.so.%{sover}*

%files devel
%{_includedir}/lfp/
%{_includedir}/lfp.h
%{_libdir}/libfixposix.so
%{_libdir}/pkgconfig/libfixposix.pc

%changelog
