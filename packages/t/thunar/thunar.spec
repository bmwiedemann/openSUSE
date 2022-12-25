#
# spec file for package thunar
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


%define libname libthunarx-3-0
%bcond_with git
Name:           thunar
Version:        4.18.1
Release:        0
Summary:        File Manager for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            https://docs.xfce.org/xfce/thunar/start
Source:         https://archive.xfce.org/src/xfce/thunar/4.18/%{name}-%{version}.tar.bz2
Source100:      %{name}-rpmlintrc
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xfconf
BuildRequires:  pkgconfig(exo-2) >= 4.17.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.66.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.30.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libxfce4kbd-private-3) >= 4.17.2
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= 4.14.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.15.3
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.17.2
BuildRequires:  pkgconfig(libxfconf-0) >= 4.12.0
BuildRequires:  pkgconfig(pango) >= 1.38.0
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
# uses exo-desktop-item-edit, exo-open
Requires:       exo-tools
Recommends:     %{name}-lang = %{version}
Recommends:     catfish
Recommends:     gvfs
Recommends:     thunar-volman
Recommends:     tumbler
Provides:       thunar-doc = %{version}
Obsoletes:      thunar-doc <= 1.2.3

%description
Thunar is a file manager for the Xfce desktop environment. Its
functionality can be extended through plugins. Thunar can also be
extended by writing scripts to be placed in the context menu for
various file types.

%package -n %{libname}
Summary:        Thunar Extension Library
Group:          System/Libraries

%description  -n %{libname}
This package contains the Thunar extension library.

%package devel
Summary:        Development Files for Thunar
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}
Provides:       thunar-devel-doc = %{version}
Obsoletes:      thunar-devel-doc < %{version}

%description devel
This package provides the development files needed for developing extensions for
Thunar.

%package -n typelib-1_0-Thunarx-3_0
Summary:        Thunar Extension Library -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Thunarx-3_0
This package provides the GObject Introspection bindings for the Thunar extension library %{libname}.

%lang_package

%prep
%autosetup

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode \
    --with-helper-path-prefix=%{_libexecdir} \
    --docdir=%{_datadir}/xfce4/thunar \
    --enable-dbus \
    --enable-exif \
    --enable-startup-notification \
    --enable-pcre \
    --enable-gtk-doc \
    --disable-static
%else
%configure \
    --with-helper-path-prefix=%{_libexecdir} \
    --docdir=%{_datadir}/xfce4/thunar \
    --enable-dbus \
    --enable-exif \
    --enable-startup-notification \
    --enable-pcre \
    --enable-gtk-doc \
    --disable-static
%endif
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la \
    %{buildroot}%{_libdir}/thunarx-3/*.la \
    %{buildroot}%{_libdir}/xfce4/panel/plugins/*.la

# add a lowercase manpage symlink
( cd %{buildroot}%{_mandir}/man1/ && ln -sf Thunar.1* \
    $(printf "%%s\n" Thunar.1* | tr [:upper:] [:lower:]) )

# these files are placed under %%{_defaultdocdir}/%%{name} instead
rm -f %{buildroot}%{_datadir}/xfce4/thunar/README.*

# do not allow to Thunar to run as root via pkexec
rm -f %{buildroot}%{_datadir}/polkit-1/actions/org.xfce.thunar.policy

%suse_update_desktop_file -i thunar System Utility Core GTK FileManager
%suse_update_desktop_file -i thunar-bulk-rename System Utility Core GTK Filesystem
%suse_update_desktop_file thunar-settings

%find_lang thunar %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc README.md NEWS AUTHORS FAQ HACKING THANKS docs/README.*
%license COPYING
%dir %{_sysconfdir}/xdg/Thunar
%config %{_sysconfdir}/xdg/Thunar/uca.xml
%{_bindir}/thunar
%{_bindir}/Thunar
%{_bindir}/thunar-settings
%dir %{_libexecdir}/Thunar
%{_libexecdir}/Thunar/thunar-sendto-email
%{_userunitdir}/thunar.service
%{_libdir}/thunarx-3
%{_libdir}/xfce4/panel/plugins/libthunar-tpa.so
%{_datadir}/Thunar
%{_datadir}/metainfo/org.xfce.thunar.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.xfce.FileManager.service
%{_datadir}/dbus-1/services/org.xfce.Thunar.service
%{_datadir}/dbus-1/services/org.xfce.Thunar.FileManager1.service
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/icons/hicolor/*/*/*/*.png
%{_datadir}/xfce4/panel/plugins/thunar-tpa.desktop
%{_mandir}/man1/thunar.1*
%{_mandir}/man1/Thunar.1*

%files -n %{libname}
%{_libdir}/libthunarx-3.so.*

%files -n typelib-1_0-Thunarx-3_0
%{_libdir}/girepository-1.0/Thunarx-3.0.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/thunar
%doc %{_datadir}/gtk-doc/html/thunarx
%dir %{_includedir}/thunarx-3
%dir %{_includedir}/thunarx-3/thunarx
%{_includedir}/thunarx-3/thunarx/*.h
%{_libdir}/libthunarx-3.so
%{_libdir}/pkgconfig/thunarx-3.pc
%{_datadir}/gir-1.0/Thunarx-3.0.gir

%files lang -f thunar.lang

%changelog
