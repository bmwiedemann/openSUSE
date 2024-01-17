#
# spec file for package libemf2svg
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


%define soversion 1
Name:           libemf2svg
Version:        1.1.0
Release:        0
Summary:        EMF (Enhanced Metafile) to SVG conversion library
License:        GPL-2.0-only
Group:          Productivity/Graphics/Convertors
URL:            https://github.com/kakwa/libemf2svg
Source:         https://github.com/kakwa/libemf2svg/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel

%description
Library for converting Enhanced Metafile (EMF and EMF+) files to the
SVG format. It can be used for conversion of standalone EMF files,
but more typically for files embedded in other file formats, e.g.
Visio drawings.

%package -n %{name}%{soversion}
Summary:        EMF (Enhanced Metafile) to SVG conversion library
Group:          System/Libraries

%description -n %{name}%{soversion}
Library for converting Enhanced Metafile (EMF and EMF+) files to the
SVG format. It can be used for conversion of standalone EMF files,
but more typically for files embedded in other file formats, e.g.
Visio drawings.

%package devel
Summary:        Development files for applications which will use libemf2svg
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soversion} = %{version}

%description devel
The %{name}-devel package includes the header files, libraries,
configuration files and development tools necessary for compiling and
linking programs which will convert EMF files to SVG.

%package -n emf2svg-conv
Summary:        EMF to SVG converter
Group:          Productivity/Graphics/Convertors

%description -n emf2svg-conv
Tool to convert files in EMF format to SVG

%prep
%setup -q

%build
%cmake -DCMAKE_SKIP_RPATH=TRUE
%cmake_build

%install
%cmake_install

%post -n %{name}%{soversion} -p /sbin/ldconfig
%postun -n %{name}%{soversion} -p /sbin/ldconfig

%files -n %{name}%{soversion}
%doc README.md
%license LICENSE
%{_libdir}/libemf2svg*so.*

%files devel
%{_libdir}/libemf2svg*so
%{_includedir}/*.h

%files -n emf2svg-conv
%{_bindir}/emf2svg-conv

%changelog
