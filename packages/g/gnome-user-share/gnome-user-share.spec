#
# spec file for package gnome-user-share
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


Name:           gnome-user-share
Version:        3.34.0
Release:        0
Summary:        GNOME user file sharing
License:        GPL-2.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            http://www.gnome.org/
Source0:        https://download.gnome.org/sources/gnome-user-share/3.34/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0) >= 2.58
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libnautilus-extension) >= 3.27.90
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(systemd)
Recommends:     %{name}-lang
Suggests:       apache2-mod_dnssd
Suggests:       apache2-prefork
Suggests:       apache2-worker
%glib2_gsettings_schema_requires

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
translation-update-upstream po %{name}

%build
%meson \
	-Dmodules_path=%{_libdir}/apache2/ \
	--libexecdir=%{_libexecdir}/gnome-user-share \
	-Dsystemduserunitdir=%{_userunitdir} \
	%{nil}
%meson_build

%install
%meson_install

find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file gnome-user-share-webdav Network FileTransfer
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

%files
%license COPYING
%doc README NEWS
%{_libexecdir}/gnome-user-share
%{_datadir}/gnome-user-share
%{_datadir}/applications/gnome-user-share-webdav.desktop
%{_libdir}/nautilus/extensions-3.0/libnautilus-share-extension.so
%{_datadir}/GConf/gsettings/gnome-user-share.convert
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.file-sharing.gschema.xml
%{_userunitdir}/gnome-user-share-webdav.service

%files lang -f %{name}.lang

%changelog
