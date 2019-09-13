#
# spec file for package libusbauth-configparser
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2018 Stefan Koch <stefan.koch10@gmail.com>
# Copyright (c) 2015 SUSE LLC. All Rights Reserved.
# Author: Stefan Koch <skoch@suse.de>
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


Name:           libusbauth-configparser
Version:        1.0.1
Release:        0
Summary:        Library for USB Firewall including flex/bison parser
License:        LGPL-2.1-only
Group:          Development/Languages/C and C++
URL:            https://github.com/kochstefan/usbauth-all/tree/master/libusbauth-configparser
Source:         https://github.com/kochstefan/usbauth-all/archive/v%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libudev-devel

%description
Library to read usbauth config file into data structures

%package -n %{name}1
Summary:        Library for USB Firewall including flex/bison parser
Group:          System/Libraries

%description -n %{name}1
Library to read usbauth config file into data structures

%package devel
Summary:        Development part of library for USB Firewall including flex/bison parser
Group:          Development/Languages/C and C++
Requires:       libusbauth-configparser1 = %{version}

%description devel
Development part of library to read usbauth config file into data structures

%prep
%autosetup -n usbauth-all-%{version} -p1

%build
pushd %{name}/
autoreconf -f -i
%configure
%make_build
popd

%install
pushd %{name}/
%make_install
popd

%files -n %{name}1
%defattr(-,root,root)
%_libdir/lib*.so.1*

%files devel
%defattr(-,root,root)
%license libusbauth-configparser/COPYING
%doc libusbauth-configparser/README
%doc %_mandir/*/*
%_includedir/*
%_libdir/lib*.so
%_libdir/pkgconfig/*

%post -n %{name}1 -p /sbin/ldconfig

%postun -n %{name}1 -p /sbin/ldconfig

%changelog
