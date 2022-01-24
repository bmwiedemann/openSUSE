#
# spec file for package libsigscan
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


%define lname	libsigscan1
Name:           libsigscan
Version:        20220124
Release:        0
Summary:        Library for binary signature scanning
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libsigscan
Source:         https://github.com/libyal/libsigscan/releases/download/%version/libsigscan-experimental-%version.tar.gz
Source9:        %name.keyring
Patch1:         system-libs.patch
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libuna) >= 20201204
%python_subpackages

%description
libsigscan is a library for binary signature scanning

libsigscan is part of the libyal family of libraries

%package -n %{lname}
Summary:        Library for binary signature scanning
Group:          System/Libraries

%description -n %{lname}
libsigscan is a library for binary signature scanning

%package tools
Summary:        Tools to scan for binary signatures
Group:          Productivity/File utilities
Requires:       %{lname} = %{version}

%description tools
Tools to scan binary files for signatures.

%package devel
Summary:        Development files for libigscan
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libsigscan is a library for binary signature scanning

This subpackage contains libraries and header files for developing
applications that want to make use of libpff.

%prep
%autosetup -p1

%build
autoreconf -fi
# OOT builds are presently broken, so we have to install
# within each python iteration now, not in %%install.
%{python_expand #
%configure --disable-static --enable-wide-character-type --enable-python PYTHON_VERSION="%{$python_bin_suffix}"
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv %_builddir/rt/* %buildroot/
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libsigscan.so.*

%files -n %name-tools
%license COPYING*
%{_bindir}/sigscan
%{_mandir}/man1/sigscan.1%{?ext_man}
%config %{_sysconfdir}/sigscan.conf

%files -n %name-devel
%license COPYING*
%{_includedir}/libsigscan.h
%{_includedir}/libsigscan/
%{_libdir}/libsigscan.so
%{_libdir}/pkgconfig/libsigscan.pc
%{_mandir}/man3/libsigscan.3%{?ext_man}

%files %python_files
%{python_sitearch}/pysigscan.so

%changelog
