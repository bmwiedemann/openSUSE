#
# spec file for package liblnk
#
# Copyright (c) 2023 SUSE LLC
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


%define lname	liblnk1
Name:           liblnk
Version:        20221023
Release:        0
Summary:        Library and tools to access the Windows Shortcut File (LNK) format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File Utilities
URL:            https://github.com/libyal/liblnk
Source:         https://github.com/libyal/liblnk/releases/download/%version/liblnk-alpha-%version.tar.gz
Source2:        https://github.com/libyal/liblnk/releases/download/%version/liblnk-alpha-%version.tar.gz.asc
Source3:        %name.keyring
Source8:        Windows_Shortcut_File_LNK_format.pdf
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20220120
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcfile) >= 20220106
BuildRequires:  pkgconfig(libclocale) >= 20220107
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcpath) >= 20220108
BuildRequires:  pkgconfig(libcsplit) >= 20220109
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfdatetime) >= 20220112
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libfole) >= 20220115
BuildRequires:  pkgconfig(libfwps) >= 20220122
BuildRequires:  pkgconfig(libfwsi) >= 20220927
BuildRequires:  pkgconfig(libuna) >= 20220611
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
liblnk is a library and tools to access Windows Shortcut File (LNK) format files.

%package -n %lname
Summary:        Library to access the Windows Shortcut File (LNK) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
liblnk is a library to access Windows Shortcut File (LNK) files.

%package tools
Summary:        Tools to access the Windows Shortcut File (LNK) format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
liblnk is a library to access Windows Shortcut File (LNK) files.

%package devel
Summary:        Development files for liblnk, a library to access Windows Shortcut Links
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
liblnk is a library to access Windows Shortcut File (LNK) files.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%prep
%autosetup -p1
cp %_sourcedir/*.pdf .

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type --enable-python \
	PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep ' '' ''local' config.log && exit 1
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv %_builddir/rt/* %buildroot/
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/liblnk.so.*

%files -n %name-tools
%_bindir/lnk*
%_mandir/man1/lnkinfo.1*

%files -n %name-devel
%doc Windows_Shortcut_File_*.pdf
%_includedir/liblnk.h
%_includedir/liblnk/
%_libdir/liblnk.so
%_libdir/pkgconfig/liblnk.pc
%_mandir/man3/liblnk.3*

%files %python_files
%license COPYING*
%python_sitearch/pylnk.so

%changelog
