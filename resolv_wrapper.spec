#
# spec file for package resolv_wrapper
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


############################# NOTE ##################################
#
# This is a special library. You are not able to link this library.
# Do NOT create library package or a devel package!
#
############################# NOTE ##################################

Name:           resolv_wrapper
Version:        1.1.8
Release:        0

Summary:        A wrapper for DNS name resolving or DNS faking
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://cwrap.org/

Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source2:        resolv_wrapper.keyring
Source3:        %{name}-rpmlintrc

BuildRequires:  cmake
BuildRequires:  glibc-devel
BuildRequires:  libcmocka-devel
BuildRequires:  pkg-config
BuildRequires:  socket_wrapper

Requires:       cmake
Requires:       pkg-config

%description
resolv_wrapper makes it possible to contact your own DNS
implmentation in your test environment. It requires socket_wrapper to be able
to contact it. If it does not work on a special platform, the wrapper is able to
fake DNS queries and return valid responses to your application.

This package does not have a devel package, because this project is for
development/testing.

%prep
%autosetup -p1

%build
%cmake \
  -DUNIT_TESTING=ON

make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

%check
%ctest

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libresolv_wrapper.so*
%dir %{_libdir}/cmake/resolv_wrapper
%{_libdir}/cmake/resolv_wrapper/resolv_wrapper-config-version.cmake
%{_libdir}/cmake/resolv_wrapper/resolv_wrapper-config.cmake
%{_libdir}/pkgconfig/resolv_wrapper.pc
%{_mandir}/man1/resolv_wrapper.1*

%changelog
