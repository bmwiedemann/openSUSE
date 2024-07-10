#
# spec file for package libzrtpcpp
#
# Copyright (c) 2020 SUSE LLC
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


Name:           libzrtpcpp
%define lname	libzrtpcpp4
Version:        4.7.0
Release:        0
Summary:        A ccrtp extension for ZRTP support
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.gnutelephony.org/index.php/GNU_ZRTP

#Git-Clone:	git://github.com/wernerd/ZRTPCPP
#Git-Web:	https://github.com/wernerd/ZRTPCPP
Source:         https://github.com/wernerd/ZRTPCPP/archive/%version.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 4.7
BuildRequires:  libopenssl-1_0_0-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libccrtp) >= 2
BuildRequires:  pkgconfig(sqlite3) >= 3.7

%description
A library that adds RFC6189-compliant ZRTP support to the GNU ccRTP
stack and serves as library for other RTP stacks such as PJSIP and
GStreamer. ZRTP was developed to allow ad-hoc key negotiation to
setup Secure RTP (SRTP) sessions.

%package -n %lname
Summary:        A ccrtp extension for ZRTP support
Group:          System/Libraries

%description -n %lname
A library that adds RFC6189-compliant ZRTP support to the GNU ccRTP
stack and serves as library for other RTP stacks such as PJSIP and
GStreamer. ZRTP was developed to allow ad-hoc key negotiation to
setup Secure RTP (SRTP) sessions.

%package devel
Summary:        Headers and link library for libzrtpcpp
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       ccrtp-devel >= 2.0.0

%description devel
This package provides the header files for building applications that
use libzrtpcpp.

%prep
%autosetup -p1 -n ZRTPCPP-%version
chmod a-x INSTALL

%build
# libzrtpcpp changed its API (apparently - can't tell whether aes_init
# was meant to be exported or not), but failed to bump the SO version.
# So now, add explicit symbol versions to ensure programs with wrong
# ABI combinations are caught.
echo "V_%version { global: *; };" >version.map
%cmake -DCMAKE_INSTALL_PREFIX="%_prefix" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_LD_FLAGS:STRING="-Wl,--version-script=$PWD/version.map" \
	-DCRYPTO_STANDALONE:BOOL=false \
%if "%_lib" == "lib64"
	-DLIB_SUFFIX=64 \
%endif

%cmake_build

%install
%cmake_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING
%_libdir/libzrtpcpp.so.4*

%files devel
%doc AUTHORS README.md
%_libdir/libzrtpcpp.so
%_libdir/pkgconfig/libzrtpcpp.pc
%_includedir/libzrtpcpp/

%changelog
