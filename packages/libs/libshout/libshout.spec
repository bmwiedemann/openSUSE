#
# spec file for package libshout
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


Name:           libshout
Version:        2.4.4
Release:        0
Summary:        Library for communcating with Icecast servers
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://icecast.org/
#Git-Clone:     https://gitlab.xiph.org/xiph/icecast-libshout/
Source:         https://downloads.xiph.org/releases/libshout/%name-%version.tar.gz
Source1:        baselibs.conf
BuildRequires:  libtool
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)

%description
libshout is a library for communicating with and sending data to an
Icecast server. It handles the socket connection, the timing of the
data, and prevents bad data from getting to the Icecast server.

%package -n libshout3
Summary:        Library for communicating with Icecast servers
Group:          System/Libraries

%description -n libshout3
libshout is a library for communicating with and sending data to an
Icecast server. It handles the socket connection, the timing of the
data, and prevents bad data from getting to the Icecast server.

%package devel
Summary:        Development files for libshout, an Icecast communication library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libshout3 = %version

%description devel
This package contains the include files needed to develop
applications that want to use libshout.

%prep
%autosetup -p1

%build
autoreconf --force --install
%configure --disable-static
%make_build

%install
%make_install
# remove unneeded files
rm -f "%buildroot/%_libdir"/*.la
rm -rf "%buildroot/%_datadir/doc/%name"
# remove (possibly) unused ckport definitions (use libabigail instead?)
rm -Rf "%buildroot/%_libdir/ckport"

%post   -n libshout3 -p /sbin/ldconfig
%postun -n libshout3 -p /sbin/ldconfig

%files -n libshout3
%_libdir/*.so.3*

%files devel
%doc README doc/*.xml examples/*.c
%license COPYING
%_libdir/*.so
%_includedir/shout
%_datadir/aclocal/*.m4
%_libdir/pkgconfig/*.pc

%changelog
