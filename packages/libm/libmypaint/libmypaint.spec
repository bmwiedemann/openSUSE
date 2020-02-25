#
# spec file for package libmypaint
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


%define shlib %{name}-1_5-1
%define geglshlib %{name}-gegl0
Name:           libmypaint
Version:        1.5.0
Release:        0
Summary:        A brushstroke creation library
License:        ISC
Group:          Productivity/Graphics/Bitmap Editors
URL:            http://mypaint.org/
Source:         https://github.com/mypaint/libmypaint/releases/download/v%{version}/libmypaint-%{version}.tar.xz
# PATCH-FIX-UPSTREAM libmypaint-gegl-pkgconfig.patch badshah400@gmail.com -- In libmypaint-gegl.pc, change Name to libmypaint-gegl to avoid conflict with libmypaint.pc and Requires to depend on the correct version of gegl and on libmypaint - not libmypaint-@LIBMYPAINT_API_PLATFORM_VERSION@
Patch0:         libmypaint-gegl-pkgconfig.patch
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gegl-0.4)
BuildRequires:  pkgconfig(json-c)

%description
libmypaint, a.k.a. "brushlib", is a library for making brushstrokes
which is used by MyPaint and other projects.

%package -n %{shlib}
Summary:        A brushstroke creation library
Group:          System/Libraries
Provides:       libmypaint = %{version}
Recommends:     %{name}-lang = %{version}

%description -n %{shlib}
libmypaint, a.k.a. "brushlib", is a library for making brushstrokes
which is used by MyPaint and other projects including GIMP 2.9+.
This package provides the shared libraries for %{name}.

%package devel
Summary:        Header files for %{name}, a brushstroke creation library
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Provides:       mypaint-devel = %{version}
Obsoletes:      mypaint-devel < %{version}

%description devel
libmypaint, a.k.a. "brushlib", is a library for making brushstrokes
which is used by MyPaint and other projects.
This package provides the header needed for developing
applications using %{name}.

%package gegl-devel
Summary:        Header files for %{name}, a brushstroke creation library
Group:          Development/Libraries/C and C++
Requires:       %{geglshlib} = %{version}
Requires:       %{shlib} = %{version}

%description gegl-devel
libmypaint, a.k.a. "brushlib", is a library for making brushstrokes which
is used by MyPaint and other projects. This package provides the header
files needed for developing applications using the gegl bindings for %{name}.

%package -n %{geglshlib}
Summary:        GEGL bindings for %{name}, a brushstroke creation library
Group:          System/Libraries

%description -n %{geglshlib}
libmypaint, a.k.a. "brushlib", is a library for making brushstrokes which is
used by MyPaint and other projects. This package provides the shared libraries
for %{name}'s GEGL bindings.

%lang_package

%prep
%autosetup -p1

# FIX A SPURIOUS PERM
chmod -x README.md

%build
%configure \
	--enable-gegl \
	%{nil}
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig
%post -n %{geglshlib} -p /sbin/ldconfig
%postun -n %{geglshlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/%{name}-1.5.so.*

%files lang -f %{name}.lang

%files devel
%license COPYING
%doc README.md
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libmypaint.pc
%{_includedir}/%{name}/

%files -n %{geglshlib}
%{_libdir}/%{name}-gegl.so.*

%files gegl-devel
%{_libdir}/%{name}-gegl.so
%{_libdir}/pkgconfig/libmypaint-gegl.pc
%{_includedir}/%{name}-gegl/

%changelog
