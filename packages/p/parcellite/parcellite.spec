#
# spec file for package parcellite
#
# Copyright (c) 2024 SUSE LLC
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


Name:           parcellite
Version:        1.2.4
Release:        0
Summary:        A lightweight GTK+ clipboard manager
License:        GPL-3.0-or-later
Group:          Productivity/Other
URL:            https://github.com/rickyrockrat/parcellite
Source:         https://github.com/rickyrockrat/parcellite/archive/refs/tags/%{version}.tar.gz
# PATCH-FIX-UPSTREAM marguerite@opensuse.org -- tweak default settings.
Patch0:         parcellite-1.1.7-defaults.patch
Patch1:         parcellite-1.1.9_no_kde_start.patch
Patch2:         parcellite-1.2.4.0-simple.patch
BuildRequires:  automake
BuildRequires:  gnome-icon-theme
BuildRequires:  intltool >= 0.23
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.10.0
# needed for auto-paste
Requires:       xdotool

%description
Parcellite is a stripped down, basic-features-only clipboard manager with a
small memory footprint for those who like simplicity.

In GNOME and Xfce the clipboard manager will be started automatically. For
other desktops or window managers you should also install a panel with a
system tray or notification area if you want to use this package.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build
sed -i -e '/^Icon/s/=.*/=parcellite/' data/parcellite.desktop

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 \
	%{_datadir}/icons/gnome/32x32/actions/edit-paste.png \
	%{buildroot}%{_datadir}/pixmaps/%{name}.png
%find_lang %{name}
%suse_update_desktop_file -r -G "Clipboard Manager" %{name} GTK GNOME Utility DesktopUtility
%suse_update_desktop_file -r -G "Clipboard Manager" %{name}-startup GTK GNOME Utility DesktopUtility TrayIcon

%post
%desktop_database_post

%postun
%desktop_database_postun

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-startup.desktop
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%{_mandir}/man1/*

%changelog
