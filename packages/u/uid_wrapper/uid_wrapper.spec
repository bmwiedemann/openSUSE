#
# spec file for package uid_wrapper
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
Name:           uid_wrapper
Version:        1.3.1
Release:        0
Summary:        A wrapper for privilege seperation
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Source2:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source3:        uid_wrapper.keyring
BuildRequires:  cmake
BuildRequires:  libcmocka-devel
BuildRequires:  pkgconf
BuildRequires:  user(nobody)
Recommends:     cmake
Recommends:     pkgconf

%description
Some projects like a file server need privilege separation to be able to switch
to the connnection user and do file operations. uid_wrapper convincingly lies
to the application, letting it believe it is operating as root and even
switching betwen UIDs and GIDs as needed.

To use it, set the following environment variables:

LD_PRELOAD=libuid_wrapper.so
UID_WRAPPER=1

This package does not have a devel package, because this project is for
development/testing.

%prep
%autosetup -p1

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
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libuid_wrapper.so*
%dir %{_libdir}/cmake/uid_wrapper
%{_libdir}/cmake/uid_wrapper/uid_wrapper-config-version.cmake
%{_libdir}/cmake/uid_wrapper/uid_wrapper-config.cmake
%{_libdir}/pkgconfig/uid_wrapper.pc
%{_mandir}/man1/uid_wrapper.1%{?ext_man}

%changelog
