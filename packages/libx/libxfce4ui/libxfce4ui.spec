#
# spec file for package libxfce4ui
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

Name:           libxfce4ui
Version:        4.18.0
Release:        0
Summary:        Widgets Library for the Xfce Desktop Environment
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.xfce.org/
Source0:        https://archive.xfce.org/src/xfce/libxfce4ui/4.18/%{name}-%{version}.tar.bz2
# needed until all applications have been ported to xfce_dialog_show_help() or
# an alternative mechanism
Source1:        xfhelp4.sh
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libgtop-2.0) >= 2.24.0
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.15.6
BuildRequires:  pkgconfig(libxfconf-0) >= 4.14
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(x11)
%if %{with git}
BuildRequires:  gtk-doc
BuildRequires:  xfce4-dev-tools
%endif

%description
The libxfce4ui library provides a number of widgets commonly used by Xfce
applications.

%package -n libxfce4ui-2-0
Summary:        Widgets Library for the Xfce Desktop Environment
# uses exo-open
License:        GPL-2.0-or-later
Group:          System/Libraries
Requires:       exo-tools
# -branding only contains keyboard shortcuts for some libxfce4ui consumers so
# it is not really a dependency but it must be dragged in at a low level
Recommends:     %{name}-branding = %{version}
Recommends:     %{name}-lang = %{version}

%description -n libxfce4ui-2-0
The libxfce4ui library provides a number of widgets commonly used by Xfce
applications. This package provides the GTK 3 variant of libxfce4ui.

%package -n libxfce4kbd-private-3-0
Summary:        XFCE keyboard library for xfwm
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libxfce4kbd-private-3-0
The libxfce4kbd-private library provides helper functions for xfwm4.

%package tools
Summary:        Tools from libxfce4ui
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE

%description tools
This package provides tools from libxfce4ui.

%package devel
Summary:        Development Files for the libxfce4ui Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libxfce4kbd-private-3-0 = %{version}-%{release}
Requires:       libxfce4ui-2-0 = %{version}-%{release}
Recommends:     %{name}-doc = %{version}

%description devel
This package provides development files for developing applications based on
the libxfce4ui library.

%package doc
Summary:        Documentation for the libxfce4ui Library
License:        LGPL-2.1-or-later
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package provides the documentation for the libxfce4ui library.

%package branding-upstream
Summary:        Upstream Branding of libxfce4ui
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
Supplements:    packageand(libxfce4ui-2-0:branding-upstream)
# BRAND: xfce4-keyboard-shortcuts.xml: Controls the global keyboard shortcuts
# BRAND: for the Xfce desktop.
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
BuildArch:      noarch

%description branding-upstream
This package provides the upstream look and feel for libxfce4ui.








# this should be replaced by %%lang_package once bnc#513786 is resolved
%package lang
Summary:        Languages for package %{name}
License:        LGPL-2.1-or-later
Group:          System/Localization
Requires:       libxfce4ui-2-0 = %{version}
Provides:       %{name}-lang-all = %{version}
Supplements:    packageand(bundle-lang-other:libxfce4ui-2-0)
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%package -n typelib-1_0-Libxfce4ui-2_0
Summary:        UI Library for the Xfce Desktop Environment
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       typelib-1_0-libxfce4ui-2_0 = %{version}
Obsoletes:      typelib-1_0-libxfce4ui-2_0 < %{version}

%description -n typelib-1_0-Libxfce4ui-2_0
The libxfce4ui library provides a number of widgets commonly used by Xfce
applications.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode \
    --enable-startup-notification \
    --with-vendor-info=openSUSE \
    --disable-static \
    --enable-vala=yes \
    --enable-gladeui2
%else
%configure \
    --enable-startup-notification \
    --with-vendor-info=openSUSE \
    --disable-static \
    --enable-vala=yes \
    --enable-gladeui2
%endif
%make_build

%install
%make_install

install -D -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/xfhelp4

find %{buildroot} -type f -name "*.la" -delete -print

%suse_update_desktop_file xfce4-about -r X-XFCE X-Xfce-Toplevel

# remove unsupported locales
rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{?no_lang_C}

%fdupes %{buildroot}%{_includedir}

%post   -n libxfce4ui-2-0 -p /sbin/ldconfig
%postun -n libxfce4ui-2-0 -p /sbin/ldconfig
%post   -n libxfce4kbd-private-3-0 -p /sbin/ldconfig
%postun -n libxfce4kbd-private-3-0 -p /sbin/ldconfig

%files -n libxfce4ui-2-0
%license COPYING
%{_libdir}/libxfce4ui-2.so.*

%files -n libxfce4kbd-private-3-0
%{_libdir}/libxfce4kbd-private-3.so.*

%files lang -f %{name}.lang

%files devel
%doc AUTHORS NEWS THANKS TODO
%{_libdir}/libxfce4ui-*.so
%{_libdir}/libxfce4kbd-private-*.so
%{_libdir}/pkgconfig/libxfce4ui-*.pc
%{_libdir}/pkgconfig/libxfce4kbd-private-*.pc
%{_libdir}/glade/*
%{_includedir}/xfce4/libxfce4ui-2/
%{_includedir}/xfce4/libxfce4kbd-private-3/
%{_datadir}/vala/vapi/
%{_datadir}/gir-1.0/Libxfce4ui-2.0.gir
%{_datadir}/glade/*

%files tools
%{_bindir}/xfhelp4
%{_bindir}/xfce4-about
%{_datadir}/applications/xfce4-about.desktop
%{_datadir}/icons/hicolor/*/apps/{org.xfce.about.*,xfce4-logo.*}

%files doc
%doc %{_datadir}/gtk-doc/html/libxfce4ui/

%files branding-upstream
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml

%files -n typelib-1_0-Libxfce4ui-2_0
%{_libdir}/girepository-1.0/Libxfce4ui-2.0.typelib

%changelog
