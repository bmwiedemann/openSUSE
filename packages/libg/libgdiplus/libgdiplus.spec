#
# spec file for package libgdiplus
#
# Copyright (c) 2021 SUSE LLC
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


%define soname 0
Name:           libgdiplus
Version:        6.0.5
Release:        0
Summary:        Open Source Implementation of the GDI+ API
License:        (LGPL-2.1-or-later OR MPL-1.1) AND MIT
Group:          Development/Libraries/Mono
URL:            https://github.com/mono/libgdiplus
Source:         http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrender)

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
sed -i 's/-Wall/-Wall %{optflags}/' src/Makefile.am

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/%{name}.la

#%check
#%make_build check

%post -n libgdiplus%{soname} -p /sbin/ldconfig
%postun -n libgdiplus%{soname} -p /sbin/ldconfig

%files -n libgdiplus%{soname}
%{_libdir}/libgdiplus.so.*
%license COPYING
%doc AUTHORS ChangeLog* NEWS README.md

%files devel
%{_libdir}/libgdiplus.so
%{_libdir}/pkgconfig/libgdiplus.pc

%changelog
