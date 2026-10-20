#
# spec file for package cdio-utils
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cdioutils 1
Name:           cdio-utils
Version:        2.4.0
Release:        0
Summary:        Utility programs making use of libcdio, a CD-ROM access library
License:        GPL-3.0-or-later
URL:            https://savannah.gnu.org/projects/libcdio
Source0:        https://github.com/libcdio/libcdio/releases/download/%{version}/libcdio-%{version}.tar.bz2
Source4:        baselibs.conf
Patch0:         c99.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(form)
BuildRequires:  pkgconfig(formw)
BuildRequires:  pkgconfig(libcddb) >= 1.0.1
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio++)
BuildRequires:  pkgconfig(libiso9660)
BuildRequires:  pkgconfig(libiso9660++)
BuildRequires:  pkgconfig(libudf)
BuildRequires:  pkgconfig(libvcdinfo) >= 2.0
BuildRequires:  pkgconfig(menu)
BuildRequires:  pkgconfig(menuw)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ncurses++)
BuildRequires:  pkgconfig(ncurses++w)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(panel)
BuildRequires:  pkgconfig(panelw)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(tic)
BuildRequires:  pkgconfig(ticw)
BuildRequires:  pkgconfig(tinfo)
Provides:       libcdio-utils = %{version}
Obsoletes:      libcdio-utils < %{version}

%description
This package contains a number of utility programs that make use of
libcdio.

%prep
%autosetup -p1 -n libcdio-%{version}

%define buildir ${PWD}

%build
export VCDINFO_CFLAGS=-I%{_includedir}/libvcd
export VCDINFO_LIBS="-L%{_libdir} -lvcdinfo -L%{buildir}/lib/iso9660/.libs/ -liso9660 -L%{buildir}/lib/driver/.libs/ -lcdio"

VCDINFO_CFLAGS=-I%{_includedir}/libvcd VCDINFO_LIBS="-L%{_libdir} -lvcdinfo -L%{buildir}/lib/iso9660/.libs -liso9660 \
-L%{buildir}/lib/driver/.libs -lcdio" \
%configure \
	--disable-silent-rules \
	--disable-rpath \
	--disable-static \
	--disable-cxx \
	--enable-vcd-info=yes

VCDINFO_CFLAGS=-I%{_includedir}/libvcd VCDINFO_LIBS="-L%{_libdir} -lvcdinfo \
-L%{buildir}/lib/iso9660/.libs/ -liso9660 -L%{buildir}/lib/driver/.libs/ -lcdio" \
%make_build

%install
%make_install
#empty depdendency libs
rm -rf %{buildroot}%{_libdir} %{buildroot}%{_includedir} %{buildroot}%{_infodir}
%fdupes -s %{buildroot}%{_mandir}

%files -n cdio-utils
%doc AUTHORS THANKS TODO ChangeLog NEWS.md README-libcdio.md README.md
%license COPYING*
%{_bindir}/cd-*
%{_bindir}/cdda-*
%{_bindir}/iso-*
%{_bindir}/mmc-*
%{_mandir}/man?/*%{ext_man}

%changelog
