#
# spec file for package wget2
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


Name:           wget2
Version:        2.0.1
Release:        0
Summary:        A Tool for Mirroring FTP and HTTP Servers
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            https://www.gnu.org/software/wget/
Source:         https://ftp.gnu.org/gnu/wget/%name-%version.tar.gz
Source2:        https://ftp.gnu.org/gnu/wget/%name-%version.tar.gz.sig
Source3:        https://savannah.gnu.org/people/viewgpg.php?user_id=87218#/%name.keyring
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gettext-devel >= 0.18.1
BuildRequires:  libidn2-devel >= 0.14
BuildRequires:  libtool >= 2.2
BuildRequires:  libunistring-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

%description
Wget enables you to retrieve WWW documents or FTP files from a
server. This can be done in script files or via the command line.

In many cases Wget2 downloads much faster than Wget1.x due to HTTP
zlib compression, parallel connections and use of If-Modified-Since
HTTP header. HTTP/2 has been implemented. Wget2 also consumes less
system and user CPU cycles than Wget1.x.

%package -n libwget1
Summary:        A library to download and mirror FTP/HTTP sites
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n libwget1
Wget enables you to retrieve WWW documents or FTP files from a
server. This can be done in script files or via the command line.

libwget which provides an interface to many useful functions used by
Wget2.

%package -n libwget-devel
Summary:        Development files for libwget
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++

%description -n libwget-devel
libwget which provides an interface to many useful functions used by
Wget2.

This subpackage contains the header files for application wanting
to build against libwget.

%prep
%autosetup -p1

%build
#./bootstrap --no-git --gnulib-srcdir="$PWD/gnulib"
%configure --disable-static
%make_build

%check
%make_build check

%install
%make_install
rm -f "%buildroot/%_bindir"/*_noinstall "%buildroot/%_libdir"/*.la
%find_lang %name

%post   -n libwget1 -p /sbin/ldconfig
%postun -n libwget1 -p /sbin/ldconfig

%files -f %name.lang
%_bindir/wget*
%license COPYING

%files -n libwget1
%_libdir/libwget*.so.*
%license COPYING.LESSER

%files -n libwget-devel
%_mandir/man3/*.3*
%_libdir/pkgconfig/*.pc
%_libdir/libwget*.so
%_includedir/wget*

%changelog
