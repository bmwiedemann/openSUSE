#
# spec file for package gnome-break-timer
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gnome-break-timer
Version:        1.1
Release:        0
Summary:        GNOME Break Timer
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/GnomeBreakTimer
Source:         http://s1.dylanmccall.com/gnome-break-timer/code/gnome-break-timer-1.1.tar.xz
# PATCH-FIX-UPSTREAM gnome-break-timer-vala-0.22.1.patch dimstar@opensuse.org -- Fix build with Vala 0.22.1
Patch0:         gnome-break-timer-vala-0.22.1.patch
BuildRequires:  intltool >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(cairo) >= 1.12.14
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.8.0
BuildRequires:  pkgconfig(gee-1.0) >= 0.6.2
BuildRequires:  pkgconfig(gio-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.30.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.8.0
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.16.0
BuildRequires:  pkgconfig(libcanberra) >= 0.28
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.28
BuildRequires:  pkgconfig(libnotify) >= 0.4.5
BuildRequires:  pkgconfig(x11) >= 1.4.99.1
BuildRequires:  pkgconfig(xi) >= 1.5.99.3
BuildRequires:  pkgconfig(xtst) >= 1.2.0
Recommends:     %{name}-lang

%description
Take a Break - GNOME Break Timer helps you remember about it.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
make -j1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Remove unndeded files
rm %{buildroot}%{_datadir}/gnome-break-timer/gir-1.0/Gd-1.0.gir
rm %{buildroot}%{_prefix}/doc/BrainBreak/*
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name}
%suse_update_desktop_file %{name}-service

%post
%glib2_gsettings_schema_post
%icon_theme_cache_post
%desktop_database_post

%postun
%glib2_gsettings_schema_postun
%icon_theme_cache_postun
%desktop_database_postun

%files
%license COPYING
%doc README README
%{_bindir}/%{name}
%{_bindir}/%{name}-service
%dir %{_datadir}/appdata
%{_datadir}/appdata/gnome-break-timer.appdata.xml
%{_datadir}/applications/gnome-break-timer-service.desktop
%{_datadir}/applications/gnome-break-timer.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.break-timer.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_libdir}/%{name}/
%config %{_sysconfdir}/xdg/autostart/gnome-break-timer-autostart.desktop

%files lang -f %{name}.lang

%changelog
