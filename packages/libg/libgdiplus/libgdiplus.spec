#
# spec file for package libgdiplus
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


%define soname 0
Name:           libgdiplus
Version:        3.12
Release:        0
Summary:        Open Source Implementation of the GDI+ API
License:        (LGPL-2.1+ or MPL-1.1) and MIT
Group:          Development/Libraries/Mono
Url:            https://github.com/mono/libgdiplus
Source:         http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM libgdiplus0-giflib5.patch https://github.com/mono/libgdiplus/pull/32
Patch:          libgdiplus-giflib5.patch
# PATCH-FIX-UPSTREAM boo#944912
Patch1:		libgdiplus-libjpeg_prefix.patch
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrender)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mono library that provide a GDI+ comptible API on non-Windows
operating systems.

%package -n libgdiplus%{soname}
Summary:        Open Source Implementation of the GDI+ API
Group:          System/Libraries

%description -n libgdiplus%{soname}
Mono library that provide a GDI+ comptible API on non-Windows
operating systems.

%package devel
Summary:        Development files for libgdiplus
Group:          Development/Libraries/C and C++
Requires:       libgdiplus%{soname} = %{version}

%description devel
This library is part of the Mono project. It is required when
using System.Drawing.

%prep
%setup -q
%patch -p1
%patch1 -p1
sed -i 's/-Wall/-Wall %{optflags}/' src/Makefile.am

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm -rf %{buildroot}%{_libdir}/%{name}.{a,la}

%check
make %{?_smp_mflags} check

%post -n libgdiplus%{soname} -p /sbin/ldconfig

%postun -n libgdiplus%{soname} -p /sbin/ldconfig

%files -n libgdiplus%{soname}
%defattr(-,root,root)
%{_libdir}/libgdiplus.so.*
%doc AUTHORS COPYING ChangeLog* NEWS README

%files devel
%defattr(-,root,root)
%{_libdir}/libgdiplus.so
%{_libdir}/pkgconfig/libgdiplus.pc

%changelog
