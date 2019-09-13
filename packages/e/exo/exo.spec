#
# spec file for package exo
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define libname_gtk2 libexo-1-0
%define libname_gtk3 libexo-2-0
%bcond_with git
Name:           exo
Version:        0.12.8
Release:        0
Summary:        Application Development Library for Xfce
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            https://docs.xfce.org/xfce/exo/starte
Source0:        https://archive.xfce.org/src/xfce/exo/0.12/%{name}-%{version}.tar.bz2
# icons taken from tango-icon-theme 0.8.90
Source1:        %{name}-icons.tar.bz2
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  perl-URI
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.42
BuildRequires:  pkgconfig(glib-2.0) >= 2.42
BuildRequires:  pkgconfig(gthread-2.0) >= 2.42
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libxfce4ui-1) >= 4.12.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.12.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.12.0
# Prevent dependency cycle exo -> libxfce4ui-devel -> libxfce4ui-1-0 -> exo-tools
#!BuildIgnore:  exo-tools

%description
Exo is an extension library to Xfce which is targeted at application
development.

%package tools
Summary:        Tools for exo
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/XFCE
Provides:       exo:%{_bindir}/exo-csource
Provides:       exo:%{_bindir}/exo-desktop-item-edit
Provides:       exo:%{_bindir}/exo-open
Provides:       exo:%{_bindir}/exo-preferred-applications

%description tools
This package provides tools and helpers for exo.

%package data
Summary:        Helpers Data for exo
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/XFCE
Requires:       %{name}-branding = %{version}
Requires:       %{name}-helpers = %{version}

%description data
This package provides the helpers data for exo.

%package helpers
Summary:        Helpers for exo
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/XFCE

%description helpers
This package provides the helper binaries for exo.

%package -n %{libname_gtk2}
Summary:        Application Development Library for Xfce
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name}-branding = %{version}
# >= because of crazy rpmlint stuff
Requires:       %{name}-data >= %{version}
Requires:       perl-URI
Recommends:     %{name}-lang = %{version}
Recommends:     %{name}-tools

%description -n %{libname_gtk2}
Exo is an extension library to Xfce which is targeted at application
development.

%package -n %{libname_gtk3}
Summary:        Application Development Library for Xfce
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name}-branding = %{version}
Requires:       %{name}-data >= %{version}
Requires:       perl-URI
Recommends:     %{name}-lang = %{version}
Recommends:     %{name}-tools

%description -n %{libname_gtk3}
Exo is an extension library to Xfce which is targeted at application
development.

%package devel
Summary:        Development Files for exo
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{libname_gtk2} = %{version}
Requires:       %{libname_gtk3} = %{version}
Requires:       %{name}-tools = %{version}

%description devel
This package contains development files needed for developing applications
based on exo.

%package branding-upstream
Summary:        Upstream Branding of exo
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
Supplements:    packageand(%{libname_gtk2}:branding-upstream)
Supplements:    packageand(%{libname_gtk3}:branding-upstream)
# BRAND: helpers.rc: Controls default applications and MIME handler.
Conflicts:      %{name}-branding
Provides:       %{libname_gtk2}-branding = %{version}
Provides:       exo-branding = %{version}
Obsoletes:      %{libname_gtk2}-branding <= 0.10.6
BuildArch:      noarch

%description branding-upstream
This package provides the upstream look and feel for the exo library.

# this should be replaced by %%lang_package once bnc#513786 is resolved
# additional bug: %%lang_package will always reuire %%name, which is unwanted here
%package lang
Summary:        Languages for package %{name}
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Localization
Requires:       %{libname_gtk2} = %{version}
Requires:       %{libname_gtk3} = %{version}
Supplements:    packageand(bundle-lang-other:%{libname_gtk2})
Supplements:    packageand(bundle-lang-other:%{libname_gtk3})
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%prep
%setup -q -b1
mkdir m4
find . -name '*.pl' -o -name exo-compose-mail| \
    xargs sed -i 's|^#! */usr/bin/env *\perl|#!%{_bindir}/perl|'

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

find %{buildroot} -type f -name "*.la" -delete -print

%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_includedir}

# remove unsupported locales
rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang exo-1 %{?no_lang_C}

%suse_update_desktop_file exo-preferred-applications
%suse_update_desktop_file exo-mail-reader
%suse_update_desktop_file exo-terminal-emulator
%suse_update_desktop_file exo-file-manager
%suse_update_desktop_file exo-web-browser

%post -n %{libname_gtk2} -p /sbin/ldconfig
%postun -n %{libname_gtk2} -p /sbin/ldconfig
%post -n %{libname_gtk3} -p /sbin/ldconfig
%postun -n %{libname_gtk3} -p /sbin/ldconfig

%files tools
%{_bindir}/exo-csource
%{_bindir}/exo-desktop-item-edit
%{_bindir}/exo-open
%{_bindir}/exo-preferred-applications
%{_datadir}/applications/exo-file-manager.desktop
%{_datadir}/applications/exo-mail-reader.desktop
%{_datadir}/applications/exo-preferred-applications.desktop
%{_datadir}/applications/exo-terminal-emulator.desktop
%{_datadir}/applications/exo-web-browser.desktop
%{_mandir}/man1/exo-csource.1*
%{_mandir}/man1/exo-open.1*
%{_datadir}/icons/hicolor/*/*/*

%files data
%dir %{_datadir}/xfce4
%{_datadir}/xfce4/helpers
# frame image directly used by the library
%dir %{_datadir}/pixmaps/exo
%{_datadir}/pixmaps/exo/*

%files helpers
## does not realy belong into -data
%dir %{_libdir}/xfce4
%dir %{_libdir}/xfce4/exo
%dir %{_libdir}/xfce4/exo-2
# helper binaries which can be considered part of the API
%{_libdir}/xfce4/exo-2/*
%{_libdir}/xfce4/exo/exo-compose-mail

%files lang -f exo-1.lang

%files -n %{libname_gtk2}
%doc README NEWS AUTHORS THANKS TODO
%license COPYING COPYING.LIB
%{_libdir}/libexo-1.so.*

%files -n %{libname_gtk3}
%doc README NEWS AUTHORS THANKS TODO
%license COPYING COPYING.LIB
%{_libdir}/libexo-2.so.*

%files devel
%{_includedir}/exo-1
%{_includedir}/exo-2
%{_libdir}/libexo*.so
%{_libdir}/pkgconfig/exo*
%{_datadir}/gtk-doc/html/exo-1/

%files branding-upstream
%dir %{_sysconfdir}/xdg/xfce4
%config %{_sysconfdir}/xdg/xfce4/helpers.rc

%changelog
