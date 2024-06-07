#
# spec file for package clipit
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


Name:           clipit
Version:        1.4.5
Release:        0
Summary:        A lightweight GTK+ clipboard manager
License:        GPL-3.0-or-later
Group:          Productivity/Other
URL:            https://github.com/shantzu/ClipIt/
Source:         https://github.com/downloads/shantzu/ClipIt/%{name}-%{version}.tar.gz
BuildRequires:  intltool >= 0.23
%if 0%{suse_version} >= 1550
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0)
Recommends:     xdotool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ClipIt is a lightweight, fully featured GTK+ clipboard manager.
It was forked from Parcellite, adding additional features and bugfixes to the project.

ClipIts main features are:
 – Save a history of your last copied items;
 – Search through the history;
 – Global hotkeys for most used functions;
 – Execute actions with clipboard items;
 – Exclude specific items from history.

%prep
%setup -q -n ClipIt-%{version}

%build
autoreconf -vif
%configure --with-gtk3
make %{?_smp_mflags}
sed -i -e '/^Icon/s/=.*/=clipit-trayicon/' data/clipit.desktop
rsvg-convert -h 32 -w 32 data/clipit-trayicon.svg -o data/clipit-trayicon.png

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 \
	data/%{name}-trayicon.png \
	%{buildroot}%{_datadir}/pixmaps/%{name}-trayicon.png
%find_lang %{name}
%suse_update_desktop_file -r -G "Clipboard Manager" %{name} GTK GNOME Utility DesktopUtility
%suse_update_desktop_file -r -G "Clipboard Manager" %{name}-startup GTK GNOME Utility DesktopUtility TrayIcon

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-startup.desktop
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-trayicon.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}-trayicon.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}-trayicon-offline.svg
%{_mandir}/man1/*

%changelog
