#
# spec file for package libGLC
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libGLC
Version:        0.7.2
Release:        0
Summary:        Free OpenGL Character Renderer
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://quesoglc.sf.net/
Source:         http://sourceforge.net/projects/quesoglc/files/%{version}/quesoglc-%{version}.tar.bz2
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         quesoglc-typepun.diff
BuildRequires:  Mesa-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freeglut-devel
BuildRequires:  freetype2-devel
BuildRequires:  fribidi-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  libICE-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
QuesoGLC is a free (as in free speech) implementation of the OpenGL
Character Renderer (GLC). QuesoGLC is based on the FreeType library,
provides Unicode support and is designed to be easily ported to any
platform that supports both FreeType and the OpenGL API.

%package -n libGLC0
Summary:        Free OpenGL Character Renderer
Group:          System/Libraries

%description -n libGLC0
QuesoGLC is a free (as in free speech) implementation of the OpenGL
Character Renderer (GLC). QuesoGLC is based on the FreeType library,
provides Unicode support and is designed to be easily ported to any
platform that supports both FreeType and the OpenGL API.

%package devel
Summary:        QuesoGLC Development Files
Group:          Development/Libraries/C and C++
Requires:       Mesa-devel
Requires:       fontconfig-devel
Requires:       freetype2-devel
Requires:       libGLC0 = %{version}
Requires:       libexpat-devel
Requires:       zlib-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications using QuesoGLC.

%prep
%setup -q -n quesoglc-%{version}
%patch1 -p1

%build
%configure \
  --disable-static
make %{?_smp_mflags}

%post -n libGLC0 -p /sbin/ldconfig

%postun -n libGLC0 -p /sbin/ldconfig

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%check
make check

%files -n libGLC0
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README THANKS
%{_libdir}/libGLC.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libGLC.so
%{_libdir}/pkgconfig/quesoglc.pc

%changelog
