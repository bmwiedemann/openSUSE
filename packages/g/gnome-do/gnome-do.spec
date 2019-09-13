#
# spec file for package gnome-do
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnome-do
Version:        0.95.3
Release:        0
# FIXME: check if removal of locales in %install is still needed (last checked: 2010-12-11)
Url:            http://do.davebsd.com/
Source:         https://launchpad.net/do/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gnome-do-OnlyShowIn.patch lp#413575 dominique-obs@leuenberger.net -- Show gnome-do only in gnome desktop.
Patch0:         gnome-do-OnlyShowIn.patch
# PATCH-NEEDS-REBASE -- was PATCH-FIX-UPSTREAM gnome-do-quiet-autostart.patch lp#413596 vuntz@novell.com -- Do not show the dialog when autostarted
Patch1:         gnome-do-quiet-autostart.patch
# PATCH-FIX-UPSTREAM gnome-do-mono-3.8.patch lp#1375948  dimstar@opensuse.org -- Fix build with Mono 3.8
Patch2:         gnome-do-mono-3.8.patch
Summary:        A powerful, speedy, and sexy remote control for your GNOME Desktop
License:        GPL-3.0+
Group:          Productivity/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gconf2-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  mono-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(dbus-sharp-1.0)
BuildRequires:  pkgconfig(dbus-sharp-glib-1.0)
BuildRequires:  pkgconfig(gconf-sharp-2.0)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(gio-sharp-2.0)
BuildRequires:  pkgconfig(gkeyfile-sharp)
BuildRequires:  pkgconfig(glade-sharp-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glib-sharp-2.0)
BuildRequires:  pkgconfig(gnome-desktop-sharp-2.0)
BuildRequires:  pkgconfig(gnome-keyring-sharp-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(mono-addins)
BuildRequires:  pkgconfig(mono-addins-gui)
BuildRequires:  pkgconfig(mono-addins-setup)
BuildRequires:  pkgconfig(notify-sharp)
BuildRequires:  pkgconfig(rsvg2-sharp-2.0)
BuildRequires:  pkgconfig(wnck-sharp-1.0)
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%else
%define suse_update_desktop_file true
%endif
Recommends:     %{name}-lang
Recommends:     gnome-do-plugins
%gconf_schemas_prereq

%description
GNOME Do allows you to quickly search for many objects present in your
GNOME desktop environment (applications, Evolution contacts, Firefox
bookmarks, files, artists and albums in Rhythmbox, Pidgin buddies) and
perform commonly used commands on those objects (Run, Open, Email,
Chat, Play, etc.).

GNOME Do is inspired by Quicksilver (http://quicksilver.blacktree.com)
and GNOME Launch Box
(http://developer.imendio.com/projects/gnome-launch-box).


%lang_package
%prep
%setup -q
%patch0 -p1
## Patch needs rebase
#%%patch1 -p1
%patch2 -p1

%build
autoreconf -fi
%configure --disable-schemas-install
make

%install
%make_install
%if 0%{?suse_version} <= 1140
%{__rm} %{buildroot}%{_datadir}/locale/jv/LC_MESSAGES/*
%{__rm} %{buildroot}%{_datadir}/locale/lb/LC_MESSAGES/*
%{__rm} %{buildroot}%{_datadir}/locale/nap/LC_MESSAGES/*
%{__rm} %{buildroot}%{_datadir}/locale/sc/LC_MESSAGES/*
%{__rm} %{buildroot}%{_datadir}/locale/tet/LC_MESSAGES/*
%{__rm} %{buildroot}%{_datadir}/locale/tyv/LC_MESSAGES/*
# FIXME: nan is not a ISO 639-2 code, so it's not clear if it's valid as a locale
%{__rm} %{buildroot}%{_datadir}/locale/nan/LC_MESSAGES/*
%endif
%__rm -f %{buildroot}%{_libdir}/%{name}/libdo.la
## Disabled since the patch needs rebase.
# Keep the same autostart desktop filename as upstream (needed because of gnome-do-quiet-autostart.patch)
#mv %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
# We need to specify the whole path since we have two desktop files with the
# same filename
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}.desktop Utilities DesktopUtility
#%suse_update_desktop_file %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop Utilities DesktopUtility
%find_lang %{name} %{?no_lang_C}
%find_gconf_schemas

%pre -f %{name}.schemas_pre

%preun -f %{name}.schemas_preun

%posttrans -f %{name}.schemas_posttrans

%if 0%{?suse_version} > 1130

%post
%desktop_database_post
%icon_theme_cache_post
%endif

%if 0%{?suse_version} > 1130

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%if 0%{?fedora_version} || 0%{?rhel_version}
# Allows overrides of __find_provides in fedora distros... (already set to zero on newer suse distros)
%define _use_internal_dependency_generator 0
%endif
%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | /usr/lib/rpm/find-provides && printf "%s\\n" "${filelist[@]}" | /usr/bin/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | /usr/lib/rpm/find-requires && printf "%s\\n" "${filelist[@]}" | /usr/bin/mono-find-requires ; } | sort | uniq'

%files -f %{name}.schemas_list
%defattr(-, root, root)
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_libdir}/pkgconfig/do.*.pc

%files lang -f %{name}.lang

%changelog
