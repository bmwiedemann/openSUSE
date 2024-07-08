#
# spec file for package nss_wrapper
#
# Copyright (c) 2024 SUSE LLC
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
Name:           nss_wrapper
Version:        1.1.16
Release:        0
Summary:        A wrapper for the user, group and hosts NSS API
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source2:        https://cryptomilk.org/gpgkey-8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D.gpg#/%{name}.keyring
Source3:        %{name}-rpmlintrc
BuildRequires:  cmake
BuildRequires:  libcmocka-devel
BuildRequires:  netcfg
Recommends:     cmake
Recommends:     pkgconf

%description
There are projects which provide daemons that need to be able to create, modify
and delete Unix users, or just switch user IDs to interact with the system, e.g.
a user space file server. To be able to test that, you need the privilege to
modify the passwd and groups files. With nss_wrapper, it is possible to define
your own passwd and groups files which will be used by software to act correctly
while under test.

If you have a client and server under test, they normally use functions to
resolve network names to addresses (DNS) or vice versa. The nss_wrappers allow
you to create a hosts file to setup name resolution for the addresses you use
with socket_wrapper.

To use it, set the following environment variables:

LD_PRELOAD=libuid_wrapper.so
NSS_WRAPPER_PASSWD=/path/to/passwd
NSS_WRAPPER_GROUP=/path/to/group
NSS_WRAPPER_HOSTS=/path/to/host

This package does not have a devel package, because this project is for
development/testing.

%prep
%autosetup -p1

%build
%cmake \
  -DUNIT_TESTING=ON

%make_build VERBOSE=1

%install
%cmake_install

find %{buildroot}%{_bindir} -name "*.pl" \
    | xargs sed -i '1 s|/usr/bin/env\ perl|/usr/bin/perl|'

%check
%ctest

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_bindir}/nss_wrapper.pl
%{_libdir}/libnss_wrapper.so*
%dir %{_libdir}/cmake/nss_wrapper
%{_libdir}/cmake/nss_wrapper/nss_wrapper-config-version.cmake
%{_libdir}/cmake/nss_wrapper/nss_wrapper-config.cmake
%{_libdir}/pkgconfig/nss_wrapper.pc
%{_mandir}/man1/nss_wrapper.1%{?ext_man}

%changelog
