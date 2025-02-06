#
# spec file for package gnome-user-share
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gnome-user-share
Version:        47.2
Release:        0
Summary:        GNOME user file sharing
License:        GPL-2.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://gitlab.gnome.org/GNOME/gnome-user-share
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  fdupes
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0) >= 2.58
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(systemd)
Suggests:       apache2-prefork
Suggests:       apache2-worker

%description
gnome-user-share is a small package that binds together various free
software projects to bring easy to use user-level file sharing to the
masses.

The program is meant to run in the background when the user is logged
in, and when file sharing is enabled a webdav server is started that
shares the $HOME/Public folder. The share is then published to all
computers on the local network using mDNS/rendezvous, so that it shows
up in the Network location in GNOME.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dmodules_path=%{_libdir}/apache2/ \
	--libexecdir=%{_libexecdir}/gnome-user-share \
	-Dsystemduserunitdir=%{_userunitdir} \
	%{nil}
%meson_build

%install
%meson_install

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

%check
%meson_test

%files
%license COPYING
%doc README.md NEWS
%{_libexecdir}/gnome-user-share
%{_datadir}/gnome-user-share
%{_datadir}/applications/gnome-user-share-webdav.desktop
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/gnome-user-share.convert
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.file-sharing.gschema.xml
%{_userunitdir}/gnome-user-share-webdav.service

%files lang -f %{name}.lang

%changelog
