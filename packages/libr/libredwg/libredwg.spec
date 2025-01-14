#
# spec file for package libredwg
#
# Copyright (c) 2024 SUSE LLC
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


%define lname	libredwg0
Name:           libredwg
Version:        0.13.3
Release:        0
Summary:        A library to handle DWG files
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gnu.org/software/libredwg/
#Git-Clone:	https://github.com/LibreDWG/libredwg/
Source:         https://ftp.gnu.org/pub/gnu/libredwg/%name-%version.tar.xz
Source2:        https://ftp.gnu.org/pub/gnu/libredwg/%name-%version.tar.xz.sig
#Source:         https://github.com/LibreDWG/libredwg/releases/download/%version/libredwg-%version.tar.xz
Source3:        https://savannah.gnu.org/people/viewgpg.php?user_id=101103#/%name.keyring
Source4:        %name-rpmlintrc
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libpcre2-8)

%description
GNU LibreDWG is a C library to handle DWG files. It can replace the
OpenDWG libraries. DWG is the native file format of AutoCAD.

%package tools
Summary:        Command line utilities for handling DWG file
Group:          Productivity/File utilities
%if 0%{?suse_version} < 1599
Requires(post): %install_info_prereq
Requires(preun): %install_info_prereq
%endif
# Both packages ship a %%_bindir/dwg2dxf
Conflicts:      libdxfrw-tools

%description tools
GNU LibreDWG is a C library to handle DWG files. It can replace the
OpenDWG libraries. DWG is the native file format of AutoCAD.

This package contains some command line utilities using this library.

%package devel
Summary:        Development files for libredwg
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
GNU LibreDWG is a C library to handle DWG files. It can replace the
OpenDWG libraries. DWG is the native file format of AutoCAD.

This package contains the files required for development with libredwg.

%package -n %lname
Summary:        A library to handle DWG files
Group:          System/Libraries

%description -n %lname
GNU LibreDWG is a C library to handle DWG files. It can replace the
OpenDWG libraries. DWG is the native file format of AutoCAD.

%prep
%autosetup -p1

%build
# No management of SO version despite ABI breaking changes:
# Force-add some symvers so RPM can produce meaningful deps.
echo 'V_%version { global: *; };' >src/sv.sym
%configure --disable-static --disable-werror
%make_build libredwg_la_LDFLAGS=-Wl,-version-script,sv.sym libredwg_la_LIBADD=-lm

%install
%make_install
b="%buildroot"
find "$b" -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files tools
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/dwg*
%_bindir/dxf*
%_mandir/man?/*.[1-9]*
%_infodir/LibreDWG.info*%{?ext_info}
%_datadir/libredwg/

%files devel
%license COPYING
%_includedir/*.h
%_libdir/libredwg.so
%_libdir/pkgconfig/libredwg.pc

%files -n %lname
%license COPYING
%_libdir/*.so.*

%changelog
