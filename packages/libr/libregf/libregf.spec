#
# spec file for package libregf
#
# Copyright (c) 2021 SUSE LLC
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


%bcond_without python2
%define lname	libregf1
Name:           libregf
Version:        20210504
Release:        0
Summary:        Library to access Windows REGF-type Registry files
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libregf
Source:         %name-%version.tar.xz
Source2:        Windows_NT_Registry_File_REGF_format.pdf
Patch1:         system-libs.patch
%if %{with python2}
BuildRequires:  python-devel
%endif
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
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
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libfwnt) >= 20210421
BuildRequires:  pkgconfig(libfwsi) >= 20210419
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python3)

%description
libregf is a library to access Windows Registry files of the REGF
type (a non-text representation).

%package -n %lname
Summary:        Library to access Windows REGF-type Registry files
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libregf is a library to access Windows Registry files of the REGF
type (a non-text representation).

%package tools
Summary:        Utilities to inspect Windows REGF-type Registry files
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Several tools for inspecting Windows REGF-type Registry files.
Typically used for computer forensics.

%package devel
Summary:        Development files for libregf, a Windows REGF-type Registry file parser
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
libregf is a library to access Windows Registry files of the REGF
type (a non-text representation).

This subpackage contains libraries and header files for developing
applications that want to make use of %{name}.

%package -n python2-%{name}
Summary:        Python2 bindings for libregf, a library to access Windows REGF Registry files
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Obsoletes:      python-%{name} <= 20190303

%description -n python2-%{name}
libregf is a library to access Windows Registry files of the REGF
type (a non-text representation).

This subpackage contains the Python2 bindings for libregf.

%package -n python3-%{name}
Summary:        Python3 bindings for libregf, a library to access Windows REGF Registry files
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python

%description -n python3-%{name}
libregf is a library to access Windows Registry files of the REGF
type (a non-text representation).

This subpackage contains the Python3 bindings for libregf.

%prep
%autosetup -p1
cp "%{SOURCE2}" .

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure \
    --disable-static \
    --enable-wide-character-type \
%if %{with python2}
    --enable-python2 \
%endif
    --enable-python3
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%{_libdir}/libregf.so.*

%files tools
%{_bindir}/regf*
%{_mandir}/man1/regf*.1*

%files devel
%doc Windows_NT_Registry_File*.pdf
%{_includedir}/libregf.h
%{_includedir}/libregf/
%{_libdir}/libregf.so
%{_libdir}/pkgconfig/libregf.pc
%{_mandir}/man3/libregf.3*

%if %{with python2}
%files -n python2-%{name}
%license COPYING*
%{python2_sitearch}/pyregf.so
%endif

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/pyregf.so

%changelog
