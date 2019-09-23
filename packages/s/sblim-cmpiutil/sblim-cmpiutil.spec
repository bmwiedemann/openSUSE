#
# spec file for package sblim-cmpiutil
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           sblim-cmpiutil
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sblim-cmpi-devel
%define tarname sblim-cmpiutil
Url:            http://www.omc-project.org
# Increment the version every time the source code changes.
Version:        1.0.1
Release:        0
Summary:        Utility library for cmpi development
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
PreReq:         coreutils
# This is necessary to build the RPM as a non-root user.
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# "yes" is the default, but we put it here explicitly to avoid someone
# setting it to "no"
Source0:        %{tarname}-%{version}.tar.bz2

%package -n libsblim-cmpiutil1
Summary:        Utility library for cmpi development
Group:          Development/Libraries/C and C++
#for the debug pkg
Provides:       %{name} = %{version}-%{release}

%package devel
Summary:        Utility library for cmpi development
Group:          Development/Libraries/C and C++
Requires:       libsblim-cmpiutil1

%description
A set of utility functions that make cmpi provider development easier

%description -n libsblim-cmpiutil1
A set of utility functions that make cmpi provider development easier

%description devel
A set of utility functions that make cmpi provider development easier

%prep
# Untar the sources.
%setup -n %{tarname}-%{version}

%build
# If the LD_RUN_PATH environment variable is set at link time,
# it's value is embedded in the resulting binary.  At run time,
# The binary will look here first for shared libraries.  This way
# we link against the libraries we want at run-time even if libs
# by the same name are in /usr/lib or some other path in /etc/ld.so.conf
autoreconf --force --install
CFLAGS="$RPM_OPT_FLAGS -fstack-protector" \
CXXFLAGS="$RPM_OPT_FLAGS -fstack-protector" \
%configure --disable-static
%{__make}

%install
# Tell 'make install' to install into the BuildRoot
#make DESTDIR=$RPM_BUILD_ROOT install
%makeinstall
%{__rm} %{buildroot}%{_libdir}/libsblim-cmpiutil.la

%clean
%{__rm} -rf %{buildroot}

%post -n libsblim-cmpiutil1 -p /sbin/ldconfig

%postun -n libsblim-cmpiutil1 -p /sbin/ldconfig

%files -n libsblim-cmpiutil1
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/cmpiutil
%{_includedir}/cmpiutil/*
%{_libdir}/*.so

%changelog
