#
# spec file for package libtorrent
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define lname	libtorrent32
Name:           libtorrent
Version:        0.16.2
Release:        0
Summary:        A BitTorrent library written in C++
License:        SUSE-GPL-2.0+-with-openssl-exception
Group:          Productivity/Networking/File-Sharing
URL:            https://github.com/rakshasa/libtorrent
Source:         https://github.com/rakshasa/rtorrent/releases/download/v%version/libtorrent-%version.tar.gz
BuildRequires:  automake
%if 0%{?suse_version} && 0%{?suse_version} < 1600
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(libcurl) >= 7.15.4
BuildRequires:  pkgconfig(openssl)

%description
LibTorrent is a BitTorrent library written in C++. It transfers
directly from file pages to the network stack, and achieves 3x higher
seed speeds than the official client on high-bandwidth links.

%package -n %lname
Summary:        A BitTorrent library written in C++
Group:          System/Libraries

%description -n %lname
LibTorrent is a BitTorrent library written in C++. It transfers
directly from file pages to the network stack, and achieves 3x higher
seed speeds than the official client on high-bandwidth links.

%package devel
Summary:        Development files for libtorrent, a C++ BitTorrent library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
LibTorrent is a BitTorrent library written in C++. It transfers
directly from file pages to the network stack, and achieves 3x higher
seed speeds than the official client on high-bandwidth links.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} && 0%{?suse_version} < 1600
export CXX=g++-13
%endif
export CFLAGS="%optflags -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
autoreconf -fiv
%configure --enable-ipv6 --with-posix-fallocate
%make_build

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete

%ldconfig_scriptlets -n %lname

%files -n %lname
%_libdir/libtorrent.so.*

%files devel
%_includedir/torrent/
%_libdir/libtorrent.so
%_libdir/pkgconfig/libtorrent.pc

%changelog
