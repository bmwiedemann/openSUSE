#
# spec file for package libemf2svg
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define soversion 1

Name:           libemf2svg
Version:        1.1.0
Release:        0
License:        GPL-2.0
Summary:        EMF (Enhanced Metafile) to SVG conversion library
Url:            https://github.com/kakwa/libemf2svg
Group:          Productivity/Graphics/Convertors
Source:         https://github.com/kakwa/libemf2svg/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  cmake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%post -n %{name}%{soversion} -p /sbin/ldconfig

%postun -n %{name}%{soversion} -p /sbin/ldconfig

%files -n %{name}%{soversion}
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_libdir}/libemf2svg*so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libemf2svg*so
%{_includedir}/*.h

%files -n emf2svg-conv
%defattr(-,root,root)
%{_bindir}/emf2svg-conv

%changelog
