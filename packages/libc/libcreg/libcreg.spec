#
# spec file for package libcreg
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


Name:           libcreg
%define lname	libcreg1
Version:        20210625
Release:        0
Summary:        Library to access Windows 9x/Me REGF-type Registry files
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libcreg
Source:         https://github.com/libyal/libcreg/releases/download/%version/libcreg-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libcreg/releases/download/%version/libcreg-experimental-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  %python_module devel
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python3)
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libcreg is a library to access Windows 9x/Me Registry files of the REGF
type (a non-text representation).

%package -n %lname
Summary:        Library to access Windows 9x/Me REGF-type Registry files
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libcreg is a library to access Windows 9x/Me Registry files of the REGF
type (a non-text representation).

%package tools
Summary:        Utilities to inspect Windows 9x/Me REGF-type Registry files
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Several tools for inspecting Windows 9x/Me REGF-type Registry files.
Typically used for computer forensics.

%package devel
Summary:        Development files for libcreg, a Windows 9x/Me REGF-type Registry file parser
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
libcreg is a library to access Windows 9x/Me Registry files of the REGF
type (a non-text representation).

This subpackage contains libraries and header files for developing
applications that want to make use of %{name}.

%prep
%autosetup -p1

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep ' '' ''local' config.log && exit 1
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv %_builddir/rt/* %buildroot/
find %{buildroot} -name '*.la' -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%{_libdir}/libcreg.so.*

%files -n %name-tools
%{_bindir}/creg*
%{_mandir}/man1/creg*.1*

%files -n %name-devel
%{_includedir}/libcreg.h
%{_includedir}/libcreg/
%{_libdir}/libcreg.so
%{_libdir}/pkgconfig/libcreg.pc
%{_mandir}/man3/libcreg.3*

%files %python_files
%license COPYING*
%{python_sitearch}/pycreg.so

%changelog
