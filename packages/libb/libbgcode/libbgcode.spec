#
# spec file for package libbgcode
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define libname libbgcode
# get this from the pyproject.toml and adjust the _service file accordingly
%define libversion 0.2.0
%define soversion 0_2_0
Name:           libbgcode
# Use the set_version source service for adjusting the field below
Version:        0.2.0+git20240829.b5c57c4
Release:        0
Summary:        Prusa Block & Binary G-code reader / writer / converter
License:        AGPL-3.0-only
URL:            https://github.com/prusa3d/libbgcode
Source0:        libbgcode-%{version}.tar.xz
BuildRequires:  boost-devel >= 1.78
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  heatshrink
BuildRequires:  libboost_nowide-devel >= 1.78
BuildRequires:  zlib-devel
BuildRequires:  (cmake(Catch2) >= 2.9 with cmake(Catch2) < 3)
BuildRequires:  cmake(heatshrink)
# See https://github.com/prusa3d/libbgcode/issues/47
ExcludeArch:    s390x %mipseb %sparc ppc64 ppc

%description
A new G-code file format featuring the following improvements over the legacy G-code:
1) Block structure with distinct blocks for metadata vs. G-code
2) Faster navigation
3) Coding & compression for smaller file size
4) Checksum for data validity
5) Extensivity through new (custom) blocks. For example, a file signature block may be welcome by corporate customers.

bgcode is a command line application which allows to convert gcode files from ascii to binary format and viceversa.

%package -n %{libname}_core%{soversion}
Summary:        Prusa Block & Binary G-code reader / writer / converter

%description -n %{libname}_core%{soversion}
A new G-code file format -- Core Library

Contains the basic definitions and functionality which allow to read a G-code file in binary format

%package -n %{libname}_binarize%{soversion}
Summary:        Prusa Block & Binary G-code reader / writer / converter

%description -n %{libname}_binarize%{soversion}
A new G-code file format -- Binarize Library

Contains the definitions and functionality which allow to write a G-code file in binary format

%package -n %{libname}_convert%{soversion}
Summary:        Prusa Block & Binary G-code reader / writer / converter

%description -n %{libname}_convert%{soversion}
A new G-code file format -- Convert Library

Contains the functionality which allow to convert G-code files to/from binary format

%package devel
Summary:        Prusa Block & Binary G-code reader / writer / converter development files
Requires:       %{libname}_binarize%{soversion} = %{version}
Requires:       %{libname}_convert%{soversion} = %{version}
Requires:       %{libname}_core%{soversion} = %{version}
Requires:       %{name} = %{version}

%description devel
Files required to develop applications using %{name}, the
Prusa Block & Binary G-code reader / writer / converter library

%prep
%setup -q -n libbgcode-%{version}

%build
%cmake \
  -DLibBGCode_BUILD_DEPS:BOOL=OFF

%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n %{libname}_core%{soversion}
%ldconfig_scriptlets -n %{libname}_binarize%{soversion}
%ldconfig_scriptlets -n %{libname}_convert%{soversion}

%files
%license LICENSE
%doc README.md
%{_bindir}/bgcode

%files -n %{libname}_core%{soversion}
%license LICENSE
%{_libdir}/%{libname}_core.so.%{libversion}

%files -n %{libname}_binarize%{soversion}
%license LICENSE
%{_libdir}/%{libname}_binarize.so.%{libversion}

%files -n %{libname}_convert%{soversion}
%license LICENSE
%{_libdir}/%{libname}_convert.so.%{libversion}

%files devel
%license LICENSE
%doc README.md
%{_libdir}/%{libname}_core.so
%{_libdir}/%{libname}_binarize.so
%{_libdir}/%{libname}_convert.so
%{_includedir}/LibBGCode
%{_libdir}/cmake/LibBGCode

%changelog
