#
# spec file for package libvisio2svg
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define soversion 0
Name:           libvisio2svg
Version:        0.5.8
Release:        0
Summary:        Library to convert Visio Documents and Stencils (VSS and VSD) to SVG
License:        GPL-2.0-only
URL:            https://github.com/kakwa/libvisio2svg
Source0:        https://github.com/kakwa/libvisio2svg/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libemf2svg-devel >= 1.1.0
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwmf)
BuildRequires:  pkgconfig(libxml-2.0)

%description
Library for conversion of Visio Documents and Stencils (VSS and VSD) to SVG.
It can be used for conversion of standalone EMF files, but
more typically for files embedded in other file formats, e.g.
Visio drawings.

%package -n %{name}%{soversion}
Summary:        Library to convert Visio Documents and Stencils (VSS and VSD) to SVG

%description -n %{name}%{soversion}
Library for conversion of Visio Documents and Stencils (VSS and VSD) to SVG.
It can be used for conversion of standalone EMF files, but
more typically for files embedded in other file formats, e.g.
Visio drawings.

%package devel
Summary:        Development Files for applications which will use libvisio2svg
Requires:       %{name}%{soversion} = %{version}

%description devel
The %{name}-devel package includes the header files, libraries,
configuration files and development tools necessary for compiling and
linking programs which will convert Visio files to SVG.

%package -n visio2svg-conv
Summary:        VSS/VDS to SVG converter
Requires:       %{name}%{soversion} >= %{version}

%description -n visio2svg-conv
Tools to convert Visio Documents (VSD) or Stencils (VSS) to SVG.

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
%{_libdir}/libTitleGenerator.*so.*
%{_libdir}/libVisio2Svg.*so.*

%files devel
%{_libdir}/libTitleGenerator.*so
%{_libdir}/libVisio2Svg.*so
%dir %{_includedir}/visio2svg/
%{_includedir}/visio2svg/*.h

%files -n visio2svg-conv
%{_bindir}/vss2svg-conv
%{_bindir}/vsd2svg-conv

%changelog
