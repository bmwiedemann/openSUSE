#
# spec file for package libfvde
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


%define lname	libfvde1
Name:           libfvde
Version:        20220915
Release:        0
Summary:        Library to access the File Vault Drive Encryption format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfvde/
Source:         https://github.com/libyal/libfvde/releases/download/%version/libfvde-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfvde/releases/download/%version/libfvde-experimental-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libbfio) >= 20220120
BuildRequires:  pkgconfig(libcaes) >= 20220529
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcfile) >= 20220106
BuildRequires:  pkgconfig(libclocale) >= 20220107
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcpath) >= 20220108
BuildRequires:  pkgconfig(libcsplit) >= 20220109
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfcache) >= 20220110
BuildRequires:  pkgconfig(libfdata) >= 20220111
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libfplist) >= 20220116
BuildRequires:  pkgconfig(libfvalue) >= 20220120
BuildRequires:  pkgconfig(libhmac) >= 20220425
BuildRequires:  pkgconfig(libuna) >= 20220611
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libfvde is a library to access the File Vault Drive Encryption format.

%package -n %{lname}
Summary:        Library to access the File Vault Drive Encryption format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
The libfvde library is a library to access the File Vault Drive Encryption format

%package tools
Summary:        Several tools for reading the File Vault Drive Encryption format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %{lname} = %{version}

%description tools
Several tools for reading the File Vault Drive Encryption format

See libfvde for additional details.

%package devel
Summary:        Header files and libraries for developing applications for libfvde
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Header files and libraries for developing applications for libfvde

See libfvde for additional details.

This package contains libraries and header files for developing
applications that want to make use of libfvde.

%prep
%autosetup -p1

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type --enable-python PYTHON_VERSION="%{$python_bin_suffix}" LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep ' '' ''local' config.log && exit 1
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
%{_libdir}/libfvde.so.*

%files -n %name-tools
%license COPYING*
%{_bindir}/fvde*
%{_mandir}/man1/fvde*.1*

%files -n %name-devel
%license COPYING*
%{_includedir}/libfvde.h
%{_includedir}/libfvde/
%{_libdir}/libfvde.so
%{_libdir}/pkgconfig/libfvde.pc
%{_mandir}/man3/libfvde.3*

%files %python_files
%license COPYING*
%{python_sitearch}/pyfvde.so

%changelog
