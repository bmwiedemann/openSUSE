#
# spec file for package libxfce4ui
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


%bcond_with git
%define libname_gtk2 libxfce4ui-1-0
%define libname_gtk3 libxfce4ui-2-0

Name:           libxfce4ui
Version:        4.14.1
Release:        0
Summary:        Widgets Library for the Xfce Desktop Environment
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.xfce.org/
Source0:        https://archive.xfce.org/src/xfce/libxfce4ui/4.14/%{name}-%{version}.tar.bz2
# needed until all applications have been ported to xfce_dialog_show_help() or
# an alternative mechanism
Source1:        xfhelp4.sh
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.12
BuildRequires:  pkgconfig(libxfconf-0) >= 4.12
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif

%description
The libxfce4ui library provides a number of widgets commonly used by Xfce
applications.

%package -n %{libname_gtk2}
Summary:        Widgets Library for the Xfce Desktop Environment
# uses exo-open
License:        GPL-2.0-or-later
Group:          System/Libraries
Requires:       exo-tools
# -branding only contains keyboard shortcuts for some libxfce4ui consumers so
# it is not really a dependency but it must be dragged in at a low level
Recommends:     %{name}-branding = %{version}
Recommends:     %{name}-lang = %{version}
Provides:       libxfce4ui = %{version}
Obsoletes:      libxfce4ui <= 4.8.1

%description -n %{libname_gtk2}
The libxfce4ui library provides a number of widgets commonly used by Xfce
applications. This package provides the GTK 2 variant of libxfce4ui.

%package -n %{libname_gtk3}
Summary:        Widgets Library for the Xfce Desktop Environment
# uses exo-open
License:        GPL-2.0-or-later
Group:          System/Libraries
Requires:       exo-tools
# -branding only contains keyboard shortcuts for some libxfce4ui consumers so
# it is not really a dependency but it must be dragged in at a low level
Recommends:     %{name}-branding = %{version}
Recommends:     %{name}-lang = %{version}

%description -n %{libname_gtk3}
The libxfce4ui library provides a number of widgets commonly used by Xfce
applications. This package provides the GTK 3 variant of libxfce4ui.

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
Requires:       %{libname_gtk2} = %{version}
Requires:       %{libname_gtk3} = %{version}
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
Supplements:    packageand(%{libname_gtk2}:branding-upstream)
Supplements:    packageand(%{libname_gtk3}:branding-upstream)
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
Requires:       %{libname_gtk2} = %{version}
Requires:       %{libname_gtk3} = %{version}
Provides:       %{name}-lang-all = %{version}
Supplements:    packageand(bundle-lang-other:%{libname_gtk2})
Supplements:    packageand(bundle-lang-other:%{libname_gtk3})
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%prep
%autosetup

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode \
    --enable-startup-notification \
    --with-vendor-info=openSUSE \
    --disable-static
%else
%configure \
    --enable-startup-notification \
    --with-vendor-info=openSUSE \
    --disable-static
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

%post -n %{libname_gtk2} -p /sbin/ldconfig

%postun -n %{libname_gtk2} -p /sbin/ldconfig

%post -n %{libname_gtk3} -p /sbin/ldconfig

%postun -n %{libname_gtk3} -p /sbin/ldconfig

%files -n %{libname_gtk2}
%license COPYING
%doc AUTHORS NEWS README THANKS TODO
%{_libdir}/libxfce4ui-1.so.*
%{_libdir}/libxfce4kbd-private-2.so.*

%files -n %{libname_gtk3}
%license COPYING
%doc AUTHORS NEWS README THANKS TODO
%{_libdir}/libxfce4ui-2.so.*
%{_libdir}/libxfce4kbd-private-3.so.*

%files lang -f %{name}.lang
%files devel
%{_libdir}/libxfce4ui-*.so
%{_libdir}/libxfce4kbd-private-*.so
%{_libdir}/pkgconfig/libxfce4ui-*.pc
%{_libdir}/pkgconfig/libxfce4kbd-private-*.pc
%{_includedir}/xfce4/libxfce4ui-1/
%{_includedir}/xfce4/libxfce4ui-2/
%{_includedir}/xfce4/libxfce4kbd-private-2/
%{_includedir}/xfce4/libxfce4kbd-private-3/

%files tools
%{_bindir}/xfhelp4
%{_bindir}/xfce4-about
%{_datadir}/applications/xfce4-about.desktop
%{_datadir}/icons/hicolor/48x48/apps/xfce4-logo.png

%files doc
%doc %{_datadir}/gtk-doc/html/libxfce4ui/

%files branding-upstream
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml

%changelog
