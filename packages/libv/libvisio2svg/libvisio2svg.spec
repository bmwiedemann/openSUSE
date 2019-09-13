#
# spec file for package libvisio2svg
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define soversion 0

Name:           libvisio2svg
Version:        0.5.5
Release:        0
License:        GPL-2.0
Summary:        Library to convert Visio Documents and Stencils (VSS and VSD) to SVG
Url:            https://github.com/kakwa/libvisio2svg
Group:          Productivity/Graphics/Convertors
Source0:        https://github.com/kakwa/libvisio2svg/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  freetype2-devel
%if 0%{?suse_version} > 1320
BuildRequires:  gcc-c++
%else
# Leap 42.2+ / SLE12SP2Backports
BuildRequires:  gcc7-c++
#!Buildignore:  libgcc_s1
%endif
BuildRequires:  libemf2svg-devel >= 1.1.0
BuildRequires:  librevenge-devel
BuildRequires:  libvisio-devel
BuildRequires:  libwmf-devel
BuildRequires:  libxml2-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library for conversion of Visio Documents and Stencils (VSS and VSD) to SVG.
It can be used for conversion of standalone EMF files, but
more typically for files embedded in other file formats, e.g.
Visio drawings.

%package -n %{name}%{soversion}
Summary:        Library to convert Visio Documents and Stencils (VSS and VSD) to SVG
Group:          System/Libraries

%description -n %{name}%{soversion}
Library for conversion of Visio Documents and Stencils (VSS and VSD) to SVG.
It can be used for conversion of standalone EMF files, but
more typically for files embedded in other file formats, e.g.
Visio drawings.

%package devel
Summary:        Development Files for applications which will use libvisio2svg
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soversion} = %{version}

%description devel
The %{name}-devel package includes the header files, libraries,
configuration files and development tools necessary for compiling and
linking programs which will convert Visio files to SVG.

%package -n visio2svg-conv
Summary:        VSS/VDS to SVG converter
Group:          Productivity/Graphics/Convertors
Requires:       %{name}%{soversion} >= %{version}

%description -n visio2svg-conv
Tools to convert Visio Documents (VSD) or Stencils (VSS) to SVG.

%prep
%setup -q

%build
test -x "$(type -p gcc-7)" && export CC=gcc-7
test -x "$(type -p g++-7)" && export CXX=g++-7
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
%{_libdir}/libTitleGenerator.*so.*
%{_libdir}/libVisio2Svg.*so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libTitleGenerator.*so
%{_libdir}/libVisio2Svg.*so
%dir %{_includedir}/visio2svg/
%{_includedir}/visio2svg/*.h

%files -n visio2svg-conv
%defattr(-,root,root)
%{_bindir}/vss2svg-conv
%{_bindir}/vsd2svg-conv

%changelog
