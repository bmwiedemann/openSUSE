#
# spec file for package SDL2_Pango
#
# Copyright (c) 2023 SUSE LLC
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


%define sover 4
%define shlib lib%{name}%{sover}
Name:           SDL2_Pango
Version:        2.1.5
Release:        0
Summary:        A library for graphically rendering internationalized and tagged text in SDL2
License:        LGPL-2.1-or-later
URL:            https://github.com/markuskimius/SDL2_Pango
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(pango) >= 1.2.0
BuildRequires:  pkgconfig(sdl2)

%description
SDL2_Pango is a library for graphically rendering internationalized and tagged
text in SDL2 using TrueType fonts. SDL2_Pango is a port of SDL_Pango to SDL2.

%package -n %{shlib}
Summary:        Shared library for SDL2_Pango

%description -n %{shlib}
SDL2_Pango is a library for graphically rendering internationalized and tagged
text in SDL2 using TrueType fonts. SDL2_Pango is a port of SDL_Pango to SDL2.

This package provides the shared library for SDL2_Pango.

%package devel
Summary:        Headers and sources for developing apps with SDL2_Pango
Requires:       %{shlib} = %{version}
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(pango)
Requires:       pkgconfig(sdl2)

%description devel
SDL2_Pango is a library for graphically rendering internationalized and tagged
text in SDL2 using TrueType fonts. SDL2_Pango is a port of SDL_Pango to SDL2.

This package provides the headers and sources for developing applications with
SDL2_Pango.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

rm %{buildroot}%{_libdir}/libSDL2_Pango.a \
   %{buildroot}%{_libdir}/libSDL2_Pango.la

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_includedir}/SDL2_Pango.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/SDL2_Pango.pc

%changelog
