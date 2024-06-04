#
# spec file for package compiz
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


%define _rev    198c6cfb64ddfc07eecaf5b1aa183c55
%define sover   0
Name:           compiz
Version:        0.8.18
Release:        0
Summary:        OpenGL window and compositing manager
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            https://gitlab.com/compiz/compiz-core
Source:         https://gitlab.com/compiz/compiz-core/uploads/%{_rev}/%{name}-%{version}.tar.xz
Source1:        opensuse.png
Source2:        sle.png
Source3:        baselibs.conf
# PATCH-FEATURE-OPENSUSE compiz-suse-defaults.patch dimstar@opensuse.org -- Compiz default settings for openSUSE.
Patch0:         %{name}-suse-defaults.patch
# PATCH-FIX-UPSTREAM compiz-java-config-notify.diff dreveman@novell.com -- Java config notify workaround.
Patch1:         %{name}-java-config-notify.diff
# PATCH-FIX-UPSTREAM bsc#474862 dreveman@novell.com -- Allow moving focus to fs window.
Patch2:         bug-474862-allow-moving-focus-to-fs-window.diff
# PATCH-FIX-UPSTREAM compiz-0.8.18-fix-librsvg-2.51.patch -- Fix building against librsvg 2.51+.
Patch3:         %{name}-0.8.18-fix-librsvg-2.51.patch
# PATCH-FIX-UPSTREAM Fix compatibility with libxml 2.12
Patch4:         fix-compatibility-with-libxml-2.12.patch
# PATCH-FIX-UPSTREAM Fixed compilation with gcc-14
Patch5:         fixed-compilation-with-gcc-14.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libxslt-tools
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo) >= 1.0
BuildRequires:  pkgconfig(cairo-xlib-xrender)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libmarco-private)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.14.0
BuildRequires:  pkgconfig(libstartup-notification-1.0) >= 0.7
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender) >= 0.9.3
Requires:       %{name}-branding < 0.9
Requires:       %{name}-decorator < 0.9
Requires:       %{name}-plugins < 0.9
Requires:       lib%{name}config
Requires:       pciutils
Suggests:       compicc < 0.9
Provides:       windowmanager
# KDE is no longer supported in Compiz.
Obsoletes:      %{name}-kde < %{version}
Obsoletes:      %{name}-kde4 < %{version}
ExcludeArch:    s390 s390x

%description
Compiz is an OpenGL compositing manager that uses
GLX_EXT_texture_from_drawable for binding redirected top-level
windows to texture objects. It has a flexible plug-in system and it
is designed to run well on most graphics hardware.

%lang_package

%package gnome
Summary:        OpenGL window and compositing manager configuration utilities
Requires:       %{name} = %{version}
Recommends:     %{name}-plugins-main < 0.9
Suggests:       ccsm < 0.9
Supplements:    (%{name} and gnome-session)
Supplements:    (%{name} and mate-session-manager)
Provides:       %{name}-decorator = 0.8
Provides:       %{name}-mate = %{version}

%description gnome
This package contains GNOME/MATE based configuration utilities for
the Compiz compositing manager.

%package plugins
Summary:        OpenGL window and compositing manager default plugins
Recommends:     %{name} = %{version}
Recommends:     %{name}-plugins-main < 0.9
Suggests:       %{name}-plugins-experimental < 0.9
Suggests:       %{name}-plugins-extra < 0.9

%description plugins
This package contains the default Compiz compositing manager
plugins.

%package devel
Summary:        Development files for Compiz
Requires:       %{name}-plugins = %{version}
Requires:       libjpeg-devel
Requires:       libxslt-tools
Requires:       pkgconfig
Requires:       pkgconfig(cairo) >= 1.0
Requires:       pkgconfig(cairo-xlib-xrender)
Requires:       pkgconfig(fuse)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(gtk+-3.0)
Requires:       pkgconfig(ice)
Requires:       pkgconfig(libpng)
Requires:       pkgconfig(librsvg-2.0)
Requires:       pkgconfig(libstartup-notification-1.0)
Requires:       pkgconfig(libwnck-3.0)
Requires:       pkgconfig(libxml-2.0)
Requires:       pkgconfig(libxslt)
Requires:       pkgconfig(pangocairo)
Requires:       pkgconfig(sm)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xcomposite)
Requires:       pkgconfig(xcursor)
Requires:       pkgconfig(xdamage)
Requires:       pkgconfig(xext)
Requires:       pkgconfig(xfixes)
Requires:       pkgconfig(xinerama)
Requires:       pkgconfig(xrandr)
Requires:       pkgconfig(xrender)
Recommends:     pkgconfig(libmarco-private)

%description devel
Compiz is an OpenGL compositing manager that uses
GLX_EXT_texture_from_drawable for binding redirected top-level
windows to texture objects. It has a flexible plug-in system and it
is designed to run well on most graphics hardware.

%package branding-openSUSE
Summary:        OpenGL window and compositing manager
Requires:       %{name} = %{version}
Requires(pre):  /bin/ln
Requires(pre):  /bin/rm
Supplements:    (%{name} and branding-openSUSE)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}

%description branding-openSUSE
Compiz is an OpenGL compositing manager that uses
GLX_EXT_texture_from_drawable for binding redirected top-level
windows to texture objects. It has a flexible plug-in system and it
is designed to run well on most graphics hardware.

%package branding-SLED
Summary:        OpenGL window and compositing manager
Requires:       %{name} = %{version}
Requires(pre):  /bin/ln
Requires(pre):  /bin/rm
Supplements:    (%{name} and branding-SLED)
Conflicts:      %{name}-branding
# compiz-branding-SLE was last used in openSUSE Leap 42.1
Provides:       %{name}-branding-SLE = %{version}
Obsoletes:      %{name}-branding-SLE < %{version}
Provides:       %{name}-branding = %{version}

%description branding-SLED
Compiz is an OpenGL compositing manager that uses
GLX_EXT_texture_from_drawable for binding redirected top-level
windows to texture objects. It has a flexible plug-in system and it
is designed to run well on most graphics hardware.

%package branding-upstream
Summary:        OpenGL window and compositing manager
Requires:       %{name} = %{version}
Requires(pre):  /bin/ln
Requires(pre):  /bin/rm
Supplements:    (%{name} and branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}

%description branding-upstream
Compiz is an OpenGL compositing manager that uses
GLX_EXT_texture_from_drawable for binding redirected top-level
windows to texture objects. It has a flexible plug-in system and it
is designed to run well on most graphics hardware.

%package -n libdecoration%{sover}
Summary:        Compiz window decoration library

%description -n libdecoration%{sover}
The window decoration library is responsible for drawing the
window borders and title bar of windows managed by Compiz. It is
used by window decorators like gtk-window-decorator.

%prep
%autosetup -p1

cp -a %{SOURCE1} opensuse.png
cp -a %{SOURCE2} sle.png

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-static \
  --enable-marco   \
  --with-gtk=3.0   \
  --with-default-plugins=core,ccp,decoration,dbus,commands,ezoom,fade,minimize,mousepoll,move,place,png,regex,resize,session,snap,switcher,vpswitch,wall,workarounds,matecompat
%make_build

%install
%make_install

install -Dpm 0644 opensuse.png %{buildroot}%{_datadir}/%{name}/opensuse.png
install -Dpm 0644 sle.png %{buildroot}%{_datadir}/%{name}/sle.png

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post branding-openSUSE
ln -sf opensuse.png %{_datadir}/%{name}/cube-image.png

%postun branding-openSUSE
if [ -f %{_datadir}/%{name}/cube-image.png ]; then
    rm -f %{_datadir}/%{name}/cube-image.png || :
fi

%post branding-SLED
ln -sf sle.png %{_datadir}/%{name}/cube-image.png

%postun branding-SLED
if [ -f %{_datadir}/%{name}/cube-image.png ]; then
    rm -f %{_datadir}/%{name}/cube-image.png || :
fi

%post branding-upstream
ln -sf freedesktop.png %{_datadir}/%{name}/cube-image.png

%postun branding-upstream
if [ -f %{_datadir}/%{name}/cube-image.png ]; then
    rm -f %{_datadir}/%{name}/cube-image.png || :
fi

%post -n libdecoration%{sover} -p /sbin/ldconfig

%postun -n libdecoration%{sover} -p /sbin/ldconfig

%files
%license COPYING*
%doc NEWS README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-decorator
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%dir %{_libdir}/%{name}/
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/core.xml
%{_datadir}/%{name}/icon.png
%dir %{_datadir}/%{name}/icons/
%dir %{_datadir}/%{name}/icons/hicolor/
%dir %{_datadir}/%{name}/icons/hicolor/*/
%dir %{_datadir}/%{name}/icons/hicolor/*/apps/
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-core.*

%files lang -f %{name}.lang

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libdecoration.so

%files plugins
%dir %{_libdir}/%{name}/
%dir %{_datadir}/%{name}/
%{_libdir}/%{name}/*annotate.*
%{_datadir}/%{name}/*annotate.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-annotate.*
%{_libdir}/%{name}/*blur.*
%{_datadir}/%{name}/*blur.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-blur.*
%{_libdir}/%{name}/*clone.*
%{_datadir}/%{name}/*clone.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-clone.*
%{_libdir}/%{name}/*commands.*
%{_datadir}/%{name}/*commands.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-commands.*
%{_libdir}/%{name}/*cube.*
%{_datadir}/%{name}/*cube.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-cube.*
%{_libdir}/%{name}/*dbus.*
%{_datadir}/%{name}/*dbus.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-dbus.*
%{_libdir}/%{name}/*decoration.*
%{_datadir}/%{name}/*decoration.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-decoration.*
%{_libdir}/%{name}/*fade.*
%{_datadir}/%{name}/*fade.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-fade.*
%{_libdir}/%{name}/*fs.*
%{_datadir}/%{name}/*fs.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-fs.*
%{_libdir}/%{name}/*glib.*
%{_datadir}/%{name}/*glib.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-glib.*
%{_libdir}/%{name}/*ini.*
%{_datadir}/%{name}/*ini.*
%{_libdir}/%{name}/*inotify.*
%{_datadir}/%{name}/*inotify.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-inotify.*
%{_libdir}/%{name}/*matecompat.*
%{_datadir}/%{name}/*matecompat.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-matecompat.*
%{_libdir}/%{name}/*minimize.*
%{_datadir}/%{name}/*minimize.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-minimize.*
%{_libdir}/%{name}/*move.*
%{_datadir}/%{name}/*move.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-move.*
%{_libdir}/%{name}/*obs.*
%{_datadir}/%{name}/*obs.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-obs.*
%{_libdir}/%{name}/*place.*
%{_datadir}/%{name}/*place.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-place.*
%{_libdir}/%{name}/*png.*
%{_datadir}/%{name}/*png.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-png.*
%{_libdir}/%{name}/*regex.*
%{_datadir}/%{name}/*regex.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-regex.*
%{_libdir}/%{name}/*resize.*
%{_datadir}/%{name}/*resize.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-resize.*
%{_libdir}/%{name}/*rotate.*
%{_datadir}/%{name}/*rotate.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-rotate.*
%{_libdir}/%{name}/*scale.*
%{_datadir}/%{name}/*scale.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-scale.*
%{_libdir}/%{name}/*screenshot.*
%{_datadir}/%{name}/*screenshot.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-screenshot.*
%{_libdir}/%{name}/*svg.*
%{_datadir}/%{name}/*svg.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-svg.*
%{_libdir}/%{name}/*switcher.*
%{_datadir}/%{name}/*switcher.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-switcher.*
%{_libdir}/%{name}/*wall.*
%{_datadir}/%{name}/*wall.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-wall.*
%{_libdir}/%{name}/*water.*
%{_datadir}/%{name}/*water.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-water.*
%{_libdir}/%{name}/*wobbly.*
%{_datadir}/%{name}/*wobbly.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-wobbly.*
%{_libdir}/%{name}/*zoom.*
%{_datadir}/%{name}/*zoom.*
%{_datadir}/%{name}/icons/hicolor/*/apps/plugin-zoom.*

%files branding-openSUSE
%{_datadir}/%{name}/opensuse.png

%files branding-SLED
%{_datadir}/%{name}/sle.png

%files branding-upstream
%{_datadir}/%{name}/freedesktop.png

%files gnome
%{_bindir}/gtk-window-decorator
%{_datadir}/glib-2.0/schemas/*gwd.gschema.xml

%files -n libdecoration%{sover}
%{_libdir}/libdecoration.so.%{sover}*

%changelog
