#
# spec file for package priv_wrapper
#
# Copyright (c) 2022 Andreas Schneider
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


############################# NOTE ##################################
#
# This is a special library. You are not able to link this library.
# Do NOT create library package or a devel package!
#
############################# NOTE ##################################
Name:           priv_wrapper
Version:        1.0.0
Release:        0
Summary:        A library to disable resource limits and other privilege dropping
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Source2:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source3:        priv_wrapper.keyring
BuildRequires:  cmake
BuildRequires:  libcmocka-devel
BuildRequires:  pkgconf
BuildRequires:  user(nobody)
Recommends:     cmake
Recommends:     pkgconf

%description
priv_wrapper aims to help running processes which are dropping privileges or are
restricting resources in test environments.
It can disable chroot, prctl, pledge and setrlmit system calls. A disabled call always
succeeds (i.e. returns 0) and does nothing.
The system call pledge exists only on OpenBSD.

To use it, set the following environment variables:

LD_PRELOAD=libpriv_wrapper.so
PRIV_WRAPPER_CHROOT_DISABLE=1

This package does not have a devel package, because this project is for
development/testing.

%prep
%setup -q

%build
# CMAKE_SKIP_RPATH:BOOL=OFF is need to run the tests!
%cmake \
  -DUNIT_TESTING=ON \
  -DCMAKE_SKIP_RPATH:BOOL=OFF

%make_build

%install
%cmake_install

%check
%ctest

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS README.md CHANGELOG.md
%license LICENSE
%{_libdir}/libpriv_wrapper.so*
%dir %{_libdir}/cmake/priv_wrapper
%{_libdir}/cmake/priv_wrapper/priv_wrapper-config-version.cmake
%{_libdir}/cmake/priv_wrapper/priv_wrapper-config.cmake
%{_libdir}/pkgconfig/priv_wrapper.pc
%{_mandir}/man1/priv_wrapper.1%{?ext_man}

%changelog
