#
# spec file for package libscca
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


%define lname	libscca1
Name:           libscca
Version:        20210419
Release:        0
Summary:        Library and tools to access the Windows Prefetch File (PF) format
License:        GFDL-1.3-only AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libscca
Source:         %{name}-%{version}.tar.xz
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
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libfwnt) >= 20210421
BuildRequires:  pkgconfig(libuna) >= 20201204
%python_subpackages

%description
Library and tools to access the Windows Prefetch File (PF) format.

Note that this project currently only focuses on the analysis of the format.

%package -n %{lname}
Summary:        Library to access the Windows Prefetch File (PF) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
libscca is a library to access the Windows Prefetch File (PF) format.

Note that this project currently only focuses on the analysis of the format.

%package tools
Summary:        Tools to access the Windows Prefetch File (PF) format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
libscca-tools is a project to access the Windows Prefetch File (PF) format.

Note that this project currently only focuses on the analysis of the format.

%package devel
Summary:        Development files for libscca
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
%{name} is a library to access the Windows Prefetch File (PF) format.

This subpackage contains libraries and header files for developing
applications that want to make use of %{name}.

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
%{_libdir}/libscca.so.*

%files -n %name-tools
%{_bindir}/scca*
%{_mandir}/man1/sccainfo.1%{?ext_man}

%files -n %name-devel
%{_includedir}/libscca.h
%{_includedir}/libscca/
%{_libdir}/libscca.so
%{_libdir}/pkgconfig/libscca.pc
%{_mandir}/man3/libscca.3%{?ext_man}

%files %python_files
%license COPYING*
%python_sitearch/pyscca.so

%changelog
