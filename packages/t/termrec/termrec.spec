# vim: set sw=4 ts=4 et nu:
#
# spec file for package termrec
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


%define soname  1
Name:           termrec
Version:        0.19
Release:        0
Summary:        Records Videos of Terminal Output
License:        LGPL-2.0-or-later
Group:          Productivity/Text/Utilities
URL:            http://angband.pl/termrec.html
Source:         https://github.com/kilobyte/termrec/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libbz2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
Requires:       libtty%{soname} = %{version}-%{release}

%description
Termrec is a program for recording "videos" of terminal output.

Utilities provided are
- termplay the player.
- termrec the console recorder. Allows you to capture the output
of a console program.
- proxyrec a telnet proxy. Will capture the session to a file.
- termtime takes one of more ttyrecs. Measures their lengths.
Prints that.
- termcat copies a ttyrec, possibly converting it to a different
format and/or combining several ttyrecs together.

%package -n libtty%{soname}
Summary:        Library for Terminal Handling
Group:          System/Libraries

%description -n libtty%{soname}
This contain the library for handling terminals for termrec

%package -n libtty-devel
Summary:        Library for Terminal Handling
Group:          Development/Libraries/C and C++
Requires:       libtty%{soname} = %{version}-%{release}

%description -n libtty-devel
This contain the developpment library for handling terminals
of termrec.

%prep
%setup -q

%build
%if 0%{?suse_version} >= 1210
autoreconf -fiv
%endif

%configure

make VERBOSE=1 %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.a" -delete -print

%post   -n libtty%{soname} -p /sbin/ldconfig
%postun -n libtty%{soname} -p /sbin/ldconfig

%files
%license COPYING.LIB
%doc BUGS ChangeLog README
%{_bindir}/termcat
%{_bindir}/termplay
%{_bindir}/termrec
%{_bindir}/termtime
%{_mandir}/man1/termcat.1%{?ext_man}
%{_mandir}/man1/termplay.1%{?ext_man}
%{_mandir}/man1/termrec.1%{?ext_man}
%{_mandir}/man1/termtime.1%{?ext_man}

%files -n libtty-devel
%{_includedir}/ttyrec.h
%{_includedir}/tty.h
%{_libdir}/libtty.so
%{_mandir}/man3/*.3%{?ext_man}

%files -n libtty%{soname}
%{_libdir}/libtty.so.%{soname}
%{_libdir}/libtty.so.%{soname}.*

%changelog
