#
# spec file for package exo
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


%bcond_with git
Name:           exo
Version:        4.18.0
Release:        0
Summary:        Application Development Library for Xfce
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://docs.xfce.org/xfce/exo/start
Source0:        https://archive.xfce.org/src/xfce/exo/4.18/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.15.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.17.2
# Prevent dependency cycle exo -> libxfce4ui-devel -> libxfce4ui-1-0 -> exo-tools
#!BuildIgnore:  exo-tools

%description
Exo is an extension library to Xfce which is targeted at application
development.

%package tools
Summary:        Tools for exo
Group:          System/GUI/XFCE
Provides:       exo:%{_bindir}/exo-desktop-item-edit
Provides:       exo:%{_bindir}/exo-open
Provides:       exo:%{_bindir}/exo-preferred-applications

%description tools
This package provides tools and helpers for exo.

%package data
Summary:        Helpers Data for exo
Group:          System/GUI/XFCE
Obsoletes:      exo-branding-openSUSE
Obsoletes:      exo-branding-upstream

%description data
This package provides the helpers data for exo.

%package -n libexo-2-0
Summary:        Application Development Library for Xfce
Group:          System/Libraries
Requires:       %{name}-data >= %{version}
Requires:       perl-URI
Recommends:     %{name}-lang = %{version}
Recommends:     %{name}-tools
Obsoletes:      libexo-1-0

%description -n libexo-2-0
Exo is an extension library to Xfce which is targeted at application
development.

%package devel
Summary:        Development Files for exo
Group:          Development/Libraries/C and C++
Requires:       %{name}-tools = %{version}
Requires:       libexo-2-0 = %{version}

%description devel
This package contains development files needed for developing applications
based on exo.

%lang_package -r libexo-2-0

%prep
%autosetup

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
  --enable-maintainer-mode \
  --docdir=%{_datadir}/xfce4/exo-preferred-applications \
  --enable-gtk-doc \
  --disable-static
%else
%configure \
  --docdir=%{_datadir}/xfce4/exo-preferred-applications \
  --enable-gtk-doc \
  --disable-static
%endif
%make_build

%install
%make_install

# currently expected by too many Xfce packages
mkdir -p %{buildroot}%{_libdir}/xfce4
mkdir -p %{buildroot}%{_datadir}/xfce4
mkdir -p %{buildroot}%{_sysconfdir}/xdg/xfce4

find %{buildroot} -type f -name "*.la" -delete -print

%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_includedir}

# remove unsupported locales
rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang exo %{?no_lang_C}

%post -n libexo-2-0 -p /sbin/ldconfig
%postun -n libexo-2-0 -p /sbin/ldconfig

%files tools
%dir %{_libdir}/xfce4
%dir %{_datadir}/xfce4
%dir %{_sysconfdir}/xdg/xfce4
%{_bindir}/exo-desktop-item-edit
%{_bindir}/exo-open
%{_mandir}/man1/exo-open.1*

%files data
# frame image directly used by the library
%dir %{_datadir}/pixmaps/exo
%{_datadir}/pixmaps/exo/*

%files lang -f exo.lang

%files -n libexo-2-0
%doc README.md NEWS AUTHORS THANKS
%license COPYING COPYING.LIB
%{_libdir}/libexo-2.so.*

%files devel
%{_includedir}/exo-2
%{_libdir}/libexo*.so
%{_libdir}/pkgconfig/exo*
%{_datadir}/gtk-doc/html/exo-2/

%changelog

