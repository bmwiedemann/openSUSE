#
# spec file for package matio
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


%define libname lib%{name}
%define major   13
Name:           matio
Version:        1.5.28
Release:        0
Summary:        Library for reading and writing MATLAB MAT files
License:        BSD-2-Clause
URL:            https://sourceforge.net/projects/matio/
Source0:        https://downloads.sourceforge.net/matio/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib) >= 1.2.3

%description
matio is an open-source library for reading and writing MATLAB MAT files.
This library is designed for use by programs/libraries that do not have
access or do not want to rely on MATLAB's shared library.

%package     -n %{libname}%{major}
Summary:        Library for reading and writing MATLAB MAT files
# Avoid unresolvable errors from multiple providers
Requires:       libhdf5

%description -n %{libname}%{major}
matio is an open-source library for reading and writing MATLAB MAT files.
This library is designed for use by programs/libraries that do not have
access or do not want to rely on MATLAB's shared library.

%package     -n %{libname}-devel
Summary:        Development files for %{name}
Requires:       %{libname}%{major} = %{version}
Requires:       hdf5-devel
Requires:       pkgconfig
BuildRequires:  pkgconfig(zlib) >= 1.2.3

%description -n %{libname}-devel
matio is an open-source library for reading and writing MATLAB MAT files.
This library is designed for use by programs/libraries that do not have
access or do not want to rely on MATLAB's shared library.

%package        tools
Summary:        Command line tools for %{name}
Requires:       %{libname}%{major} = %{version}
# Avoid unresolvable errors from multiple providers
Requires:       libhdf5

%description    tools
matio is an open-source library for reading and writing MATLAB MAT files.
This library is designed for use by programs/libraries that do not have
access or do not want to rely on MATLAB's shared library.

%prep
%setup -q

%build
%configure \
  --enable-shared \
  --disable-static \
  --enable-mat73=yes \
  --enable-extended-sparse=yes
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%check
export LD_LIBRARY_PATH=%{_buildroot}/%{libdir}
%make_build check

%ldconfig_scriptlets -n %{libname}%{major}

%files -n %{libname}%{major}
%license COPYING
%doc NEWS README
%{_libdir}/libmatio.so.%{major}*

%files tools
%{_bindir}/matdump

%files -n %{libname}-devel
%{_includedir}/matio.h
%{_includedir}/matio_pubconf.h
%{_libdir}/libmatio.so
%{_libdir}/pkgconfig/matio.pc
%{_mandir}/man3/Mat_*.3.*

%changelog
