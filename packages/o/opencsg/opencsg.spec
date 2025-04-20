#
# spec file for package opencsg
#
# Copyright (c) 2025 SUSE LLC
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


Name:           opencsg
Version:        1.8.1
Release:        0
Summary:        Constructive Solid Geometry rendering library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.opencsg.org/
Source:         https://www.opencsg.org/OpenCSG-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libXmu-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtbase-devel
%ifarch %{arm32} %{arm64}
BuildRequires:  pkgconfig(gl)
%endif

%description
OpenCSG is a library that does image-based Constructive Solid
Geometry rendering using OpenGL.

%package -n libopencsg1
Summary:        Constructive Solid Geometry rendering library
Group:          System/Libraries

%description -n libopencsg1
OpenCSG is a library that does image-based Constructive Solid
Geometry rendering using OpenGL. CSG denotes an approach to model 3D
shapes by applying operations such as union, intersection or
subtraction to so-called primtives, the latter of which are solid
(i.e. have a clearly defined interior and exterior).

%package doc
Summary:        Documents package for opencsg
BuildArch:      noarch

%description doc
This package contains the documentation for opencsg.

%package devel
Summary:        Development files for opencsg, a CSG rendering library
Group:          Development/Libraries/C and C++
Requires:       libopencsg1 = %{version}

%description devel
OpenCSG is a library that does image-based Constructive Solid
Geometry rendering using OpenGL.

This subpackage contains libraries and header files for developing
applications that want to make use of opencsg.

%prep
%setup -q -n OpenCSG-%{version}

%build
%cmake -DBUILD_EXAMPLE:BOOL=OFF
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n libopencsg1

%files -n libopencsg1
%license copying.txt doc/license/gpl-3.0.txt doc/license/gpl-2.0.txt
%doc changelog.txt
%{_libdir}/libopencsg.so.1*

%files devel
%{_includedir}/*
%{_libdir}/libopencsg.so

%files doc
%doc doc/*

%changelog
