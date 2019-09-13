#
# spec file for package opencsg
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           opencsg
Version:        1.4.2
Release:        0
Summary:        Constructive Solid Geometry rendering library
License:        SUSE-GPL-2.0-with-linking-exception
Group:          Development/Libraries/C and C++
Url:            http://www.opencsg.org/
Source:         http://www.opencsg.org/OpenCSG-%{version}.tar.gz
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
%if 0%{?fedora_version} || 0%{?suse_version} >= 1310
BuildRequires:  libXmu-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_prefix}
mv include %{buildroot}%{_includedir}
mv lib %{buildroot}%{_libdir}

%post -n libopencsg1 -p /sbin/ldconfig

%postun -n libopencsg1 -p /sbin/ldconfig

%files -n libopencsg1
%defattr(-,root,root)
%doc changelog.txt license.txt doc/*
%{_libdir}/libopencsg.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libopencsg.so

%changelog
