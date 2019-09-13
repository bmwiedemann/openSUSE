#
# spec file for package plib
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


Name:           plib
Version:        1.8.5+svn.2173
Release:        0
Summary:        A collection of game libraries
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://plib.sourceforge.net/
Source:         %{name}-%{version}.tar.xz
Source99:       %{name}-rpmlintrc
# PATCH-FEATURE-UPSTREAM -- https://sourceforge.net/p/plib/bugs/40/
Patch0:         plib-1.8.5-shared.patch
# PATCH-FIX-UPSTREAM -- https://sourceforge.net/p/plib/bugs/49/
Patch1:         plib-1.8.5-strncat.patch
# PATCH-FIX-UPSTREAM -- https://sourceforge.net/p/plib/bugs/50/
Patch2:         plib-1.8.5-CVE-2011-4620.patch
# PATCH-FIX-UPSTREAM -- https://sourceforge.net/p/plib/bugs/51/
Patch3:         plib-1.8.5-CVE-2012-4552.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(gl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Plib contains a selection of libraries that can be helpful for 3D game
programming.

%package -n libplib0
Summary:        A collection of game libraries
Group:          System/Libraries
Obsoletes:      plib < %{version}-%{release}
Provides:       plib = %{version}-%{release}

%description -n libplib0
Plib contains a selection of libraries that can be helpful for 3D game
programming. It contains the following libraries:
* JS  - A Joystick interface
* PUI - A simple GUI built on top of OpenGL
* SG  - Some Standard Geometry functions
* SL  - A Games-oriented Sound Library
* SSG - A Simple Scene Graph API built on top of OpenGL

%package devel
Summary:        Development files for PLIB, a collection of game libraries
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libplib0 = %{version}
Requires:       pkgconfig(gl)

%description devel
Plib contains a selection of libraries that can be helpful for 3D game
programming. It contains the following libraries:
* JS - A Joystick interface.
* PUI - A simple GUI built on top of OpenGL
* SG - Some Standard Geometry functions
* SL - A Games-oriented Sound Library
* SSG - A Simple Scene Graph API built on top of OpenGL

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3

%build
autoreconf -fiv
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%configure --disable-static
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libplib0 -p /sbin/ldconfig
%postun -n libplib0 -p /sbin/ldconfig

%files -n libplib0
%defattr(-,root,root)
%doc ChangeLog KNOWN_BUGS
%if 0%{?suse_version} > 1320
%license AUTHORS COPYING
%else
%doc AUTHORS COPYING
%endif
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc NOTICE README README.GLUT
%{_includedir}/plib
%{_libdir}/*.so

%changelog
