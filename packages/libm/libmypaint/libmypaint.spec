#
# spec file for package libmypaint
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define shlib %{name}-1_3-0
%define geglshlib %{name}-gegl0
Name:           libmypaint
Version:        1.3.0
Release:        0
Summary:        A brushstroke creation library
License:        ISC
Group:          Productivity/Graphics/Bitmap Editors
URL:            http://mypaint.org/
Source:         https://github.com/mypaint/libmypaint/releases/download/v%{version}/libmypaint-%{version}.tar.xz
# PATCH-FIX-UPSTREAM libmypaint-bump-gegl-version.patch -- Bump minimum gegl version to new stable branch 0.4.0
Patch0:         libmypaint-bump-gegl-version.patch
# PATCH-FIX-UPSTREAM libmypaint-gegl-0.4.14.patch badshah400@gmail.com -- Fix compilation against gegl=0.4.14
# See https://www.gimpusers.com/forums/gimp-developer/21248-libmypaint-needs-patching-for-recent-gegl
Patch1:         libmypaint-gegl-0.4.14.patch
BuildRequires:  intltool
BuildRequires:  libtool
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
Obsoletes:      mypaint-devel

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
%setup -q
%patch0 -p1
%if 0%{?suse_version} >= 1500
%patch1 -p1
%endif

%build
autoreconf -fiv
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
%{_libdir}/%{name}-1.3.so.*

%files lang -f %{name}.lang

%files devel
%license COPYING
%doc README.md
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/

%files -n %{geglshlib}
%{_libdir}/%{name}-gegl.so.*

%files gegl-devel
%{_libdir}/%{name}-gegl.so
%{_includedir}/%{name}-gegl/

%changelog
