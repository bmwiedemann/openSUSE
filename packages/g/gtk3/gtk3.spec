#
# spec file
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2010 Dominique Leuenberger, Amsterdam, Netherlands
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%global pname gtk3
%bcond_with    doc
%endif
%if "%{flavor}" == "doc"
%global pname gtk3-doc
%bcond_without doc
%endif
# When updating the binary version, do not forget to also update baselibs.conf
%define         gtk_binary_version 3.0.0
%define _name   gtk
%bcond_without  broadway
%bcond_with     doc
Name:           %{pname}
Version:        3.24.35
Release:        0
Summary:        The GTK+ toolkit library (version 3)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11
URL:            https://www.gtk.org/
Source0:        %{_name}-%{version}.tar.xz
Source1:        README.SUSE
Source2:        settings.ini
Source3:        macros.gtk3
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE gtk3-GTK_PATH64.patch sbrabec@novell.com - 64-bit dual install. Use GTK_PATH64 environment variable instead of GTK_PATH
Patch0:         gtk3-GTK_PATH64.patch
# PATCH-FIX-OPENSUSE gtk3-revert-forced-xftdpi.patch fvogt@opensuse.org -- Revert very controversal commit on GTK3, forcing DPI to 96
Patch1:         gtk3-revert-forced-xftdpi.patch

BuildRequires:  cups-devel >= 1.7
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gettext-tools-mini >= 0.19.7
BuildRequires:  hicolor-icon-theme
# libtool is needed since we are using a git checkout
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(atk) >= 2.15.1
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(cairo) >= 1.14.0
BuildRequires:  pkgconfig(cairo-gobject) >= 1.14.0
# Enable cloudproviders once upstream settles on a location and version
#BuildRequires:  pkgconfig(cloudproviders) >= 0.2.5
BuildRequires:  pkgconfig(colord) >= 0.1.9
BuildRequires:  pkgconfig(epoxy) >= 1.4
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.53.4
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.53.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.57.2
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.39.0
BuildRequires:  pkgconfig(harfbuzz) >= 0.9
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(pango) >= 1.41.0
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(wayland-client) >= 1.14.91
BuildRequires:  pkgconfig(wayland-cursor) >= 1.14.91
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon) >= 0.2.0
BuildRequires:  pkgconfig(xrandr)
# Autotools requires gtk-doc even with --disable-gtk-doc, try again with meson
%if %{with doc} || 1
BuildRequires:  gtk-doc
%endif

%description
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package -n libgtk-3-0
Summary:        The GTK+ toolkit library (version 3)
Group:          System/Libraries
Requires:       %{name}-data >= %{version}
Requires:       %{name}-schema >= %{version}
# Require gdk-pixbuf-loader-rsvg - bsc#1007453. We require adwaita-icon-theme
# so we need something to load the svg icons.
Requires:       gdk-pixbuf-loader-rsvg
# While hicolor is not a Requires strictly speaking, we put it as
# such instead of as a Recommends because many applications just
# assume it's there and we need to have a low-level package to
# bring it in.
Requires:       hicolor-icon-theme
Requires(post): %{name}-tools
# gtk+ can work without branding/translations. Built in defaults will be used then.
Recommends:     %{name}-branding
# it's nice to have input modules for various locales installed by default
Recommends:     %{name}-immodule-amharic = %{version}
Recommends:     %{name}-immodule-inuktitut = %{version}
Recommends:     %{name}-immodule-thai = %{version}
Recommends:     %{name}-immodule-tigrigna = %{version}
Recommends:     %{name}-immodule-vietnamese = %{version}
# Recommend Adwaita Icon Theme: GTK3 references this icon set in the code,
# but some setups might still want to eliminate it (think limited size Live CDs)
Recommends:     adwaita-icon-theme
Recommends:     gvfs
# Provide %%{name} to make the lang and immodules packages installable
Provides:       %{name} = %{version}
# Before 3.0, the package was actually libgtk-3_0-0 and files might
# conflict
Provides:       libgtk-3_0-0 = %{version}
Obsoletes:      libgtk-3_0-0 < %{version}

%description -n libgtk-3-0
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package -n typelib-1_0-Gtk-3_0
Summary:        Introspection bindings for the GTK+ toolkit library (version 3)
Group:          System/Libraries
Requires:       (python3-gobject-Gdk if python3-gobject)
Requires:       (python310-gobject-Gdk if python310-gobject)
Requires:       (python38-gobject-Gdk if python38-gobject)
Requires:       (python39-gobject-Gdk if python39-gobject)

%description -n typelib-1_0-Gtk-3_0
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the GObject Introspection bindings for GTK+.

%package immodule-amharic
Summary:        Amharic input method for the GTK+ toolkit library v3
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools
Requires(postun):%{name}-tools
Provides:       locale(%{name}:am)

%description immodule-amharic
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method for Amharic.

%package immodule-broadway
Summary:        Broadway input method for the GTK+ toolkit library v3
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools
Requires(postun):%{name}-tools

%description immodule-broadway
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method for Broadway.

%package immodule-inuktitut
Summary:        Inuktitut input method for the GTK+ toolkit library v3
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools
Requires(postun):%{name}-tools
Provides:       locale(%{name}:iu)

%description immodule-inuktitut
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method for Inuktitut.

%package immodule-multipress
Summary:        Multipress input method for the GTK+ toolkit library v3
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools
Requires(postun):%{name}-tools

%description immodule-multipress
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method which allows text entry via the
multi-press method, as on a mobile phone.

%package immodule-thai
Summary:        Thai-Lao input method for the GTK+ toolkit library v3
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools
Requires(postun):%{name}-tools
Provides:       locale(%{name}:lo)
Provides:       locale(%{name}:th)

%description immodule-thai
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method for Thai-Lao.

%package immodule-tigrigna
Summary:        Tigrigna input method for the GTK+ toolkit library v3
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools
Requires(postun):%{name}-tools
Provides:       %{name}-immodules-tigrigna = %{version}
Provides:       locale(%{name}:ti)
Obsoletes:      %{name}-immodules-tigrigna < %{version}

%description immodule-tigrigna
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides two input methods for Tigrigna.

%package immodule-vietnamese
Summary:        Vietnamese input method for the GTK+ toolkit library v3
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools
Requires(postun):%{name}-tools
Provides:       locale(%{name}:vi)

%description immodule-vietnamese
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method for Vietnamese.

%package immodule-wayland
Summary:        Wayland input method for the GTK+ toolkit library (version 3)
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools
Requires(postun):%{name}-tools

%description immodule-wayland
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method which allows text entry via
wayland.

%package immodule-xim
Summary:        X input method for the GTK+ toolkit library v3
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools
Requires(postun):%{name}-tools
Provides:       locale(%{name}:ja)
Provides:       locale(%{name}:ko)
Provides:       locale(%{name}:th)
Provides:       locale(%{name}:zh)

%description immodule-xim
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method based on the X Input Method.

%package tools
Summary:        Auxiliary utilities for the GTK+ toolkit library v3
Group:          System/Libraries
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description tools
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package data
Summary:        Data files for the GTK+ toolkit library v3
Group:          System/Libraries
BuildArch:      noarch

%description data
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package schema
Summary:        Config schema for the GTK+ toolkit library v3
Group:          System/Libraries
BuildArch:      noarch

%description schema
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package branding-upstream
Summary:        Upstream theme configuration for the GTK+ toolkit library v3
Group:          System/Libraries
Requires:       libgtk-3-0 = %{version}
Supplements:    (%{name} and branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: Provides /etc/gtk-3.0/settings.ini, to define default theme and icon
#BRAND: theme.
#BRAND: Do not forget to add proper Requires in branding package if changing
#BRAND: those.

%description branding-upstream
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the upstream theme configuration for widgets and
icon themes.

%package devel
Summary:        Development files for the GTK+ toolkit library v3
Group:          Development/Libraries/X11
Requires:       gettext-its-%{name} >= %{version}
Requires:       libgtk-3-0 = %{version}
Requires:       typelib-1_0-Gtk-3_0 = %{version}

%description devel
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package contains the development files for GTK+ 3.x.

%package -n gettext-its-%{name}
Summary:        International Tag Set for GTK+ 3
Group:          Development/Libraries/X11

%description -n gettext-its-%{name}
This package enhances gettext with an International Tag Set for GTK+ 3

%lang_package

%package -n gtk3-devel-doc
Summary:        API documentation for the GTK+ toolkit library v3
Group:          Documentation/HTML

%description -n gtk3-devel-doc
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package contains the API documentation for GTK+ 3.x.

%prep
%setup -q -n %{_name}-%{version}
%if "%{_lib}" == "lib64"
cp -a %{SOURCE1} .
%patch0 -p1
%endif
%patch1 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
        --disable-static \
        %{?with_doc: \
        --enable-gtk-doc} \
        --enable-man \
        --enable-x11-backend \
        --enable-introspection \
        %{?with_broadway: \
        --enable-broadway-backend} \
        --enable-wayland-backend \
        --enable-explicit-deps=yes \
        --enable-colord \
        %{nil}

%if "%{flavor}" == ""
%make_build
%else
%make_build -C gdk
%make_build -C gtk
%make_build -C tests
%make_build -C docs
%endif

%install
%if "%{flavor}" == ""
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Do not install the exampleapp glib schema, as the app itself is noinst
rm %{buildroot}%{_datadir}/glib-2.0/schemas/org.gtk.exampleapp.gschema.xml
%find_lang gtk30
%find_lang gtk30-properties
install -m 644 -D %{SOURCE2} %{buildroot}%{_sysconfdir}/gtk-3.0/settings.ini
touch %{buildroot}%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules.cache
%if "%{_lib}" == "lib64"
  mv %{buildroot}%{_bindir}/gtk-query-immodules-3.0 %{buildroot}%{_bindir}/gtk-query-immodules-3.0-64
  mv %{buildroot}%{_mandir}/man1/gtk-query-immodules-3.0.1 %{buildroot}%{_mandir}/man1/gtk-query-immodules-3.0-64.1
%endif
# create modules directory that should have been created during the build
test ! -d %{buildroot}%{_libdir}/gtk-3.0/modules
mkdir %{buildroot}%{_libdir}/gtk-3.0/modules
# create theming-engines directory that should have been created during the build
test ! -d %{buildroot}%{_libdir}/gtk-3.0/%{gtk_binary_version}/theming-engines
mkdir %{buildroot}%{_libdir}/gtk-3.0/%{gtk_binary_version}/theming-engines
# Alternatives for gtk-update-icon-cache (binary and manpage)
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
mv %{buildroot}%{_bindir}/gtk-update-icon-cache %{buildroot}%{_bindir}/gtk-update-icon-cache-3.0
ln -s -f %{_sysconfdir}/alternatives/gtk-update-icon-cache %{buildroot}%{_bindir}/gtk-update-icon-cache
mv %{buildroot}%{_mandir}/man1/gtk-update-icon-cache.1 %{buildroot}%{_mandir}/man1/gtk-update-icon-cache-3.0.1
ln -s -f %{_sysconfdir}/alternatives/gtk-update-icon-cache.1%{ext_man} %{buildroot}%{_mandir}/man1/gtk-update-icon-cache.1%{ext_man}
# Install rpm macros
mkdir -p %{buildroot}%{_rpmmacrodir}
cp %{SOURCE3} %{buildroot}%{_rpmmacrodir}

%else
%make_install -C docs
rm -Rf %{buildroot}%{_mandir}/man1/
%endif

%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_libdir}

###########################################################################
# Note: when updating scriptlets, don't forget to also update baselibs.conf
###########################################################################

# Convenient %define for the scriplets
%if "%{_lib}" == "lib64"
%define _gtk_query_immodules %{_bindir}/gtk-query-immodules-3.0-64
%else
%define _gtk_query_immodules %{_bindir}/gtk-query-immodules-3.0
%endif
%define _gtk_query_immodules_update_cache %{_gtk_query_immodules} --update-cache

%post -n libgtk-3-0
/sbin/ldconfig
%if 0
# In case libgtk-3-0 gets installed before gtk3-tools, we don't want to fail.
# So we make the call to gtk-query-immodules-3.0 dependent on the existence of
# the binary. This is why we also have a %post for gtk3-tools.
%endif
if test -f %{_gtk_query_immodules}; then
  %{_gtk_query_immodules_update_cache}
fi

%post immodule-amharic
%{_gtk_query_immodules_update_cache}

%post immodule-broadway
%{_gtk_query_immodules_update_cache}

%post immodule-inuktitut
%{_gtk_query_immodules_update_cache}

%post immodule-multipress
%{_gtk_query_immodules_update_cache}

%post immodule-thai
%{_gtk_query_immodules_update_cache}

%post immodule-tigrigna
%{_gtk_query_immodules_update_cache}

%post immodule-vietnamese
%{_gtk_query_immodules_update_cache}

%post immodule-wayland
%{_gtk_query_immodules_update_cache}

%post immodule-xim
%{_gtk_query_immodules_update_cache}

%post tools
%if 0
# If we install gtk3-tools for the first time, then we should run it in case
# libgtk-3-0 was installed first (ie, if
# %{_libdir}/gtk-3.0/%{gtk_binary_version} already exists) which means
# gtk-query-immodules-3.0 couldn't run there.
%endif
if [ $1 = 1 ]; then
  test -d %{_libdir}/gtk-3.0/%{gtk_binary_version} && %{_gtk_query_immodules_update_cache}
fi
%if 0
# If the gtk-update-icon-cache group is in automatic mode, then this will also
# switch all symlinks automatically
%endif
update-alternatives --install %{_bindir}/gtk-update-icon-cache gtk-update-icon-cache %{_bindir}/gtk-update-icon-cache-3.0 3 \
                    --slave %{_mandir}/man1/gtk-update-icon-cache.1.gz gtk-update-icon-cache.1.gz %{_mandir}/man1/gtk-update-icon-cache-3.0.1.gz

%filetriggerin tools -- %{_datadir}/icons
if [ "$(realpath %{_bindir}/gtk-update-icon-cache)" = "%{_bindir}/gtk-update-icon-cache-3.0" ]; then
  for ICON_THEME in $(cut -d / -f 5 | sort -u); do
    if [ -f "%{_datadir}/icons/${ICON_THEME}/index.theme" ]; then
      %{_bindir}/gtk-update-icon-cache --quiet --force "%{_datadir}/icons/${ICON_THEME}"
    fi
  done
fi

%filetriggerpostun tools -- %{_datadir}/icons
if [ "$(realpath %{_bindir}/gtk-update-icon-cache)" = "%{_bindir}/gtk-update-icon-cache-3.0" ]; then
  for ICON_THEME in $(cut -d / -f 5 | sort -u); do
    if [ -f "%{_datadir}/icons/${ICON_THEME}/index.theme" ]; then
      %{_bindir}/gtk-update-icon-cache --quiet --force "%{_datadir}/icons/${ICON_THEME}"
    fi
  done
fi

%if 0
# No need to call gtk-query-immodules-3.0 in postun:
# - if it's an upgrade, it will have been called in post
# - if it's an uninstall, we don't care about this anymore
%endif

%postun -n libgtk-3-0 -p /sbin/ldconfig

%postun immodule-amharic
%{_gtk_query_immodules_update_cache}

%postun immodule-broadway
%{_gtk_query_immodules_update_cache}

%postun immodule-inuktitut
%{_gtk_query_immodules_update_cache}

%postun immodule-multipress
%{_gtk_query_immodules_update_cache}

%postun immodule-thai
%{_gtk_query_immodules_update_cache}

%postun immodule-tigrigna
%{_gtk_query_immodules_update_cache}

%postun immodule-vietnamese
%{_gtk_query_immodules_update_cache}

%postun immodule-wayland
%{_gtk_query_immodules_update_cache}

%postun immodule-xim
%{_gtk_query_immodules_update_cache}

%postun tools
%if 0
# Note: we don't use "$1 -eq 0", to avoid issues if the package gets renamed
%endif
if [ ! -f %{_bindir}/gtk-update-icon-cache-3.0 ]; then
  update-alternatives --remove gtk-update-icon-cache %{_bindir}/gtk-update-icon-cache-3.0
fi

%if "%{flavor}" == ""
%files -n libgtk-3-0
%license COPYING
%if "%{_lib}" == "lib64"
%doc README.SUSE
%endif
%dir %{_sysconfdir}/gtk-3.0
%dir %{_libdir}/gtk-3.0
%dir %{_libdir}/gtk-3.0/%{gtk_binary_version}
%dir %{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-cedilla.so
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-cyrillic-translit.so
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-ipa.so
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-wayland.so
%dir %{_libdir}/gtk-3.0/%{gtk_binary_version}/printbackends/
%{_libdir}/gtk-3.0/%{gtk_binary_version}/printbackends/libprintbackend-cups.so
%{_libdir}/gtk-3.0/%{gtk_binary_version}/printbackends/libprintbackend-file.so
%{_libdir}/gtk-3.0/%{gtk_binary_version}/printbackends/libprintbackend-lpr.so
%dir %{_libdir}/gtk-3.0/%{gtk_binary_version}/theming-engines/
%ghost %{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules.cache
%dir %{_libdir}/gtk-3.0/modules
%{_libdir}/libgailutil-3.so.*
%{_libdir}/libgdk-3.so.*
%{_libdir}/libgtk-3.so.*

%files -n typelib-1_0-Gtk-3_0
%{_libdir}/girepository-1.0/Gdk-3.0.typelib
%{_libdir}/girepository-1.0/GdkX11-3.0.typelib
%{_libdir}/girepository-1.0/Gtk-3.0.typelib

%files immodule-amharic
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-am-et.so

%files immodule-broadway
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-broadway.so

%files immodule-inuktitut
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-inuktitut.so

%files immodule-multipress
%doc modules/input/README.multipress
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-multipress.so
%config %{_sysconfdir}/gtk-3.0/im-multipress.conf

%files immodule-thai
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-thai.so

%files immodule-tigrigna
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-ti-er.so
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-ti-et.so

%files immodule-vietnamese
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-viqr.so

%files immodule-wayland
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-waylandgtk.so

%files immodule-xim
%{_libdir}/gtk-3.0/%{gtk_binary_version}/immodules/im-xim.so

%files tools
%doc AUTHORS README NEWS
%{_bindir}/broadwayd
%{_bindir}/gtk3-icon-browser
%{_bindir}/gtk-builder-tool
%{_bindir}/gtk-encode-symbolic-svg
%{_bindir}/gtk-launch
%{_bindir}/gtk-query-immodules-3.0*
%{_bindir}/gtk-query-settings
%{_bindir}/gtk-update-icon-cache-3.0
%{_bindir}/gtk-update-icon-cache
%ghost %{_sysconfdir}/alternatives/gtk-update-icon-cache
%{_datadir}/applications/gtk3-icon-browser.desktop
%{_mandir}/man1/broadwayd.1%{?ext_man}
%{_mandir}/man1/gtk3-icon-browser.1%{?ext_man}
%{_mandir}/man1/gtk-builder-tool.1%{?ext_man}
%{_mandir}/man1/gtk-encode-symbolic-svg.1%{?ext_man}
%{_mandir}/man1/gtk-launch.1%{?ext_man}
%{_mandir}/man1/gtk-query-immodules-3.0*.1%{?ext_man}
%{_mandir}/man1/gtk-query-settings.1%{?ext_man}
%{_mandir}/man1/gtk-update-icon-cache-3.0.1%{?ext_man}
%{_mandir}/man1/gtk-update-icon-cache.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/gtk-update-icon-cache.1%{?ext_man}

%files schema
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.ColorChooser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.EmojiChooser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.FileChooser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.Debug.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.Demo.gschema.xml

%files data
%{_datadir}/locale/en/
%{_datadir}/themes/Default/
%{_datadir}/themes/Emacs/

%files branding-upstream
%config(noreplace) %{_sysconfdir}/gtk-3.0/settings.ini

%files devel
%{_bindir}/gtk3-demo
%{_bindir}/gtk3-demo-application
%{_bindir}/gtk3-widget-factory
%{_mandir}/man1/gtk3-demo.1%{?ext_man}
%{_mandir}/man1/gtk3-demo-application.1%{?ext_man}
%{_mandir}/man1/gtk3-widget-factory.1%{?ext_man}
%{_datadir}/aclocal/gtk-3.0.m4
%{_datadir}/applications/gtk3-demo.desktop
%{_datadir}/applications/gtk3-widget-factory.desktop
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gtk-3.0
%{_datadir}/gtk-3.0/gtkbuilder.rng
%dir %{_datadir}/gtk-3.0/valgrind
%{_datadir}/gtk-3.0/valgrind/gtk.supp
%{_datadir}/icons/hicolor/*/apps/gtk3-demo.png
%{_datadir}/icons/hicolor/*/apps/gtk3-widget-factory.png
%{_datadir}/icons/hicolor/*/apps/gtk3-demo-symbolic.symbolic.png
%{_datadir}/icons/hicolor/*/apps/gtk3-widget-factory-symbolic.symbolic.png
%{_includedir}/gail-3.0/
%{_includedir}/gtk-3.0/
%{_libdir}/pkgconfig/gail-3.0.pc
%{_libdir}/pkgconfig/gdk-3.0.pc
%if %{with broadway}
%{_libdir}/pkgconfig/gdk-broadway-3.0.pc
%{_libdir}/pkgconfig/gtk+-broadway-3.0.pc
%endif
%{_libdir}/pkgconfig/gdk-wayland-3.0.pc
%{_libdir}/pkgconfig/gtk+-wayland-3.0.pc
%{_libdir}/pkgconfig/gdk-x11-3.0.pc
%{_libdir}/pkgconfig/gtk+-3.0.pc
%{_libdir}/pkgconfig/gtk+-unix-print-3.0.pc
%{_libdir}/pkgconfig/gtk+-x11-3.0.pc
%{_libdir}/libgailutil-3.so
%{_libdir}/libgdk-3.so
%{_libdir}/libgtk-3.so
%{_rpmmacrodir}/macros.gtk3

%files -n gettext-its-%{name}
%dir %{_datadir}/gettext/
%dir %{_datadir}/gettext/its/
%{_datadir}/gettext/its/gtkbuilder.its
%{_datadir}/gettext/its/gtkbuilder.loc

%files lang -f gtk30.lang -f gtk30-properties.lang
# english locale should be in the main package
%exclude %{_datadir}/locale/en
%endif

%if %{with doc}
%files -n gtk3-devel-doc
%doc HACKING README.commits
%doc %{_datadir}/gtk-doc/html/gail-libgail-util3/
%doc %{_datadir}/gtk-doc/html/gdk3/
%doc %{_datadir}/gtk-doc/html/gtk3/
%endif

%changelog
