#
# spec file for package libgarcon
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


%define libname libgarcon-1-0
Name:           libgarcon
Version:        4.18.0
Release:        0
Summary:        Library Implementing the freedesktop.org Desktop Menu Specification
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://wiki.xfce.org/dev/garcon
Source:         https://archive.xfce.org/src/xfce/garcon/4.18/garcon-%{version}.tar.bz2
# PATCH-FEATURE-OPENSUSE libgarcon-x-suse-unimportant-support.patch gber@opensuse.org -- Hide desktop files marked with X-SuSE-Unimportant
Patch0:         libgarcon-x-suse-unimportant-support.patch
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig(gio-2.0) >= 2.66.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.15.6
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.15.6

%description
Garcon is a library based on GLib and GIO which implements the freedesktop.org
Desktop Menu Specification. It is the sucessor to libxfce4menu and covers
almost every part of the menu specification except for legacy menus and a few
XML attributes. It is capable of loading menus modified with menu editors such
as Alacarte and also supports merging.

%package -n %{libname}
Summary:        Library Implementing the freedesktop.org Desktop Menu Specification
# uses exo-open
Group:          System/Libraries
Requires:       exo-tools
# contains just menu data that needs to be dragged in at a low level
Requires:       %{name}-data

%description -n %{libname}
Garcon is a library based on GLib and GIO which implements the freedesktop.org
Desktop Menu Specification. It is the sucessor to libxfce4menu and covers
almost every part of the menu specification except for legacy menus and a few
XML attributes. It is capable of loading menus modified with menu editors such
as Alacarte and also supports merging.

%package data
Summary:        Data Files for garcon
Group:          System/GUI/XFCE
Requires:       %{name}-branding = %{version}
Recommends:     %{name}-lang = %{version}
BuildArch:      noarch

%description data
This package provides data files for garcon.

%package devel
Summary:        Development Files for garcon
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Recommends:     %{name}-doc = %{version}

%description devel
This package contains the files needed for developing applications based on
garcon.

%package doc
Summary:        Documentation for garcon
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package includes the documentation for garcon.

%package branding-upstream
Summary:        Upstream Branding of garcon
# the menu references xfce4-about.desktop
Group:          System/GUI/XFCE
Requires:       libxfce4ui-tools
Supplements:    packageand(%{name}-data:branding-upstream)
# BRAND: xfce-applications.menu: Provides the Xfce applications menu.
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
BuildArch:      noarch

%description branding-upstream
This package provides the upstream look and feel for garcon.

# this should be replaced by %%lang_package once bnc#513786 is resolved

%package lang
Summary:        Languages for package %{name}
Group:          System/Localization
Requires:       %{name}-data = %{version}
Provides:       %{name}-lang-all = %{version}
Supplements:    packageand(bundle-lang-other:%{name}-data)
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%prep
%setup -q -n garcon-%{version}
%patch0 -p1

%build
%configure \
  --disable-static \
  --enable-gtk-doc
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang garcon %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%{_libdir}/libgarcon-1.so.*
%{_libdir}/libgarcon-gtk3-1.so.*

%files data
%dir %{_datadir}/desktop-directories
%{_datadir}/desktop-directories/*.directory
%{_datadir}/icons/hicolor/*/apps/org.xfce.garcon.*

%files lang -f garcon.lang

%files devel
%{_includedir}/garcon-1/
%{_includedir}/garcon-gtk3-1/
%{_libdir}/pkgconfig/garcon-1.pc
%{_libdir}/pkgconfig/garcon-gtk3-1.pc
%{_libdir}/libgarcon-1.so
%{_libdir}/libgarcon-gtk3-1.so

%files doc
%doc AUTHORS NEWS README.md
%license COPYING
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/garcon/

%files branding-upstream
%dir %{_sysconfdir}/xdg/menus
%config %{_sysconfdir}/xdg/menus/xfce-applications.menu

%changelog
