#
# spec file for package libfwnt
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


%define lname	libfwnt1
Name:           libfwnt
Version:        20220922
Release:        0
Summary:        Library for Windows NT data types
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfwnt
Source:         https://github.com/libyal/libfwnt/releases/download/%version/libfwnt-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libfwnt/releases/download/%version/libfwnt-alpha-%version.tar.gz.asc
Source3:        %name.keyring
Source11:       Locale_identifier_LCID.pdf
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcthreads) >= 20220102
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
Library to provide Windows NT data type support for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package -n %{lname}
Summary:        Library for Windows NT data types
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Library to provide Windows NT data type support for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package devel
Summary:        Development files for libfwnt
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide Windows NT data type support for the libyal family
of libraries. libyal is typically used in digital forensic tools.

This subpackage contains libraries and header files for developing
applications that want to make use of libfwnt.

%prep
%autosetup -p1
cp %_sourcedir/*.pdf .

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
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
%{_libdir}/libfwnt.so.*

%files -n %name-devel
%license COPYING*
%doc Locale_identifier_LCID.pdf
%{_includedir}/libfwnt.h
%{_includedir}/libfwnt/
%{_libdir}/libfwnt.so
%{_libdir}/pkgconfig/libfwnt.pc
%{_mandir}/man3/libfwnt.3*

%files %python_files
%license COPYING*
%{python_sitearch}/pyfwnt.so

%changelog
