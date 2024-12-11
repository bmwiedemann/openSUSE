#
# spec file for package compiz-plugins-main
#
# Copyright (c) 2024 SUSE LLC
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


%define _rev    9a0178324a73e286352b00c66f02cc07
Name:           compiz-plugins-main
Version:        0.8.18
Release:        0
Summary:        OpenGL window and compositing manager plugins
License:        GPL-2.0-or-later
URL:            https://gitlab.com/compiz/compiz-plugins-main
Source:         https://gitlab.com/compiz/compiz-plugins-main/uploads/%{_rev}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM compiz-plugins-main-0.8.18-fix-gcc-14.patch jskarvad@redhat.com -- Fix build with GCC-14 (commit 568f653a).
Patch0:         compiz-plugins-main-0.8.18-fix-gcc-14.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libjpeg8-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bcop) >= 0.7.3
BuildRequires:  pkgconfig(cairo) >= 1.0
BuildRequires:  pkgconfig(cairo-xlib-xrender)
BuildRequires:  pkgconfig(compiz) < 0.9
BuildRequires:  pkgconfig(compiz-scale) < 0.9
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(pangocairo)
Requires:       compiz-plugins < 0.9
Conflicts:      compiz-extra < %{version}
ExcludeArch:    s390 s390x

%description
This package contains the non-default Compiz compositing manager
plugins.

%lang_package

%package devel
Summary:        OpenGL window and compositing manager plugins
Requires:       %{name} = %{version}
Requires:       pkgconfig(bcop)
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(cairo-xlib-xrender)
Requires:       pkgconfig(compiz) < 0.9
Requires:       pkgconfig(compiz-scale) < 0.9
Requires:       pkgconfig(gl)
Requires:       pkgconfig(pangocairo)
Provides:       compiz-fusion-plugins-main-devel = %{version}
Obsoletes:      compiz-fusion-plugins-main-devel < %{version}

%description devel
This package contains the non-default Compiz compositing manager
plugins.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/compiz/*
%{_datadir}/compiz/*

%files lang -f %{name}.lang

%files devel
%{_includedir}/compiz/
%{_libdir}/pkgconfig/*.pc

%changelog
