#
# spec file for package opencsg
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


Name:           opencsg
Version:        1.5.1
Release:        0
Summary:        Constructive Solid Geometry rendering library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.opencsg.org/
Source:         https://www.opencsg.org/OpenCSG-%{version}.tar.gz
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
%if 0%{?fedora_version} || 0%{?suse_version} >= 1310
BuildRequires:  libXmu-devel
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

%package devel
Summary:        Development files for opencsg, a CSG rendering library
Group:          Development/Libraries/C and C++
Requires:       freeglut-devel
Requires:       glew-devel
Requires:       libopencsg1 = %{version}

%description devel
OpenCSG is a library that does image-based Constructive Solid
Geometry rendering using OpenGL.

This subpackage contains libraries and header files for developing
applications that want to make use of opencsg.

%prep
%setup -q -n OpenCSG-%{version}
# use system glew
rm -rf glew

%build
# do not build glew and examples
cd src
# rpath is evil
sed -i 's@-Wl,-rpath,\.\./lib@@' Makefile
%make_build

%install
mkdir -p %{buildroot}%{_prefix}
mv include %{buildroot}%{_includedir}
mv lib %{buildroot}%{_libdir}

%post -n libopencsg1 -p /sbin/ldconfig
%postun -n libopencsg1 -p /sbin/ldconfig

%files -n libopencsg1
%license copying.txt doc/license/gpl-3.0.txt doc/license/gpl-2.0.txt
%doc changelog.txt doc/*
%{_libdir}/libopencsg.so.1*

%files devel
%{_includedir}/*
%{_libdir}/libopencsg.so

%changelog
