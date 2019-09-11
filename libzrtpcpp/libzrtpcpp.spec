#
# spec file for package libzrtpcpp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libzrtpcpp
%define lname	libzrtpcpp4
Version:        4.6.6
Release:        0
Summary:        A ccrtp extension for ZRTP support
License:        GPL-3.0+
Group:          Development/Libraries/C and C++
Url:            http://www.gnutelephony.org/index.php/GNU_ZRTP

#Git-Clone:	git://github.com/wernerd/ZRTPCPP
#Git-Web:	https://github.com/wernerd/ZRTPCPP
Source:         https://github.com/wernerd/ZRTPCPP/archive/V%version.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 4.7
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libccrtp) >= 2
BuildRequires:  pkgconfig(libcrypto) < 1.1
BuildRequires:  pkgconfig(sqlite3) >= 3.7
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%setup -qn ZRTPCPP-%version
chmod a-x INSTALL

%build
mkdir build
pushd build/

# libzrtpcpp changed its API (apparently - can't tell whether aes_init
# was meant to be exported or not), but failed to bump the SO version.
# So now, add explicit symbol versions to ensure programs with wrong
# ABI combinations are caught.
echo "V_%version { global: *; };" >version.map
cmake -DCMAKE_INSTALL_PREFIX="%_prefix" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_LD_FLAGS:STRING="-Wl,--version-script=$PWD/version.map" \
	-DCRYPTO_STANDALONE:BOOL=false \
%if "%_lib" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	..
make %{?_smp_mflags} VERBOSE=1
popd

%install
pushd build/
%make_install
popd

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS COPYING README.md
%_libdir/libzrtpcpp.so.4*

%files devel
%defattr(-,root,root)
%_libdir/libzrtpcpp.so
%_libdir/pkgconfig/libzrtpcpp.pc
%_includedir/libzrtpcpp/

%changelog
