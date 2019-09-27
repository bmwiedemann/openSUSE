#
# spec file for package asio
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


Name:           asio
Version:        1.12.2
Release:        0
Summary:        A cross-platform C++ library for network and low-level I/O programming
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://asio.sourceforge.net/
Source0:        http://downloads.sourceforge.net/asio/asio-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(openssl)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
Asio is a cross-platform C++ library for network and low-level I/O
programming that provides developers with a consistent asynchronous I/O
model using a modern C++ approach.

%package devel
Summary:        A cross-platform C++ library for network and low-level I/O programming
Group:          Development/Libraries/C and C++
Requires:       boost-devel
Requires:       openssl-devel

%description devel
Asio is a cross-platform C++ library for network and low-level I/O
programming that provides developers with a consistent asynchronous I/O
model using a modern C++ approach.

%prep
%setup -q
# Upstream generate them quite creatively, so refresh
autoreconf -fvi

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files devel
%license COPYING LICENSE_1_0.txt
%doc doc/*
%dir %{_includedir}/asio
%{_includedir}/asio/*
%{_includedir}/asio.hpp

%changelog
