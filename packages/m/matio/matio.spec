#
# spec file for package matio
#
# Copyright (c) 2020 SUSE LLC
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


%define libname lib%{name}
%define major   11
Name:           matio
Version:        1.5.18
Release:        0
Summary:        Library for reading and writing MATLAB MAT files
License:        BSD-2-Clause
Group:          Productivity/Scientific/Other
URL:            http://sourceforge.net/projects/matio
Source0:        http://downloads.sourceforge.net/matio/%{name}-%{version}.7z
# We need hdf5 1.10.2 to allow creation of files backwards compatible with hdf5 1.8
BuildRequires:  hdf5-devel >= 1.10.2
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel >= 1.2.3
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires:  p7zip-full
%else
BuildRequires:  p7zip
%endif

%description
matio is an open-source library for reading and writing MATLAB MAT files.
This library is designed for use by programs/libraries that do not have
access or do not want to rely on MATLAB's shared library.

%package     -n %{libname}%{major}
Summary:        Library for reading and writing MATLAB MAT files
# Avoid unresolvable errors from multiple providers
Group:          System/Libraries
Requires:       libhdf5

%description -n %{libname}%{major}
matio is an open-source library for reading and writing MATLAB MAT files.
This library is designed for use by programs/libraries that do not have
access or do not want to rely on MATLAB's shared library.

%package     -n %{libname}-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{major} = %{version}
Requires:       hdf5-devel
Requires:       pkgconfig
Requires:       zlib-devel

%description -n %{libname}-devel
matio is an open-source library for reading and writing MATLAB MAT files.
This library is designed for use by programs/libraries that do not have
access or do not want to rely on MATLAB's shared library.

%package        tools
Summary:        Command line tools for %{name}
Group:          Productivity/Scientific/Other
Requires:       %{libname}%{major} = %{version}
# Avoid unresolvable errors from multiple providers
Requires:       libhdf5

%description    tools
matio is an open-source library for reading and writing MATLAB MAT files.
This library is designed for use by programs/libraries that do not have
access or do not want to rely on MATLAB's shared library.

%prep
%setup -q
chmod +x configure

%build
%configure \
  --enable-shared \
  --disable-static \
  --enable-mat73=yes \
  --enable-extended-sparse=yes

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%check
export LD_LIBRARY_PATH=%{_buildroot}/%{name}*/src/.libs/
make check

%post   -n %{libname}%{major} -p /sbin/ldconfig
%postun -n %{libname}%{major} -p /sbin/ldconfig

%files -n %{libname}%{major}
%defattr(-,root,root)
%license COPYING
%doc NEWS README
%{_libdir}/libmatio.so.%{major}*

%files tools
%defattr(-,root,root)
%{_bindir}/matdump

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/matio.h
%{_includedir}/matio_pubconf.h
%{_libdir}/libmatio.so
%{_libdir}/pkgconfig/matio.pc
%{_mandir}/man3/Mat_*.3.*

%changelog
