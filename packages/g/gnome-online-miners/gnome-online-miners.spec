#
# spec file for package gnome-online-miners
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands
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


Name:           gnome-online-miners
Version:        3.34.0
Release:        0
Summary:        Crawls through your online content
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            https://wiki.gnome.org/Projects/GnomeOnlineMiners
Source:         https://download.gnome.org/sources/gnome-online-miners/3.34/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.35.1
BuildRequires:  pkgconfig(goa-1.0) >= 3.13.3
BuildRequires:  pkgconfig(grilo-0.3) >= 0.3
BuildRequires:  pkgconfig(libgdata) >= 0.15.2
BuildRequires:  pkgconfig(libgfbgraph-0.2) >= 0.2.2
BuildRequires:  pkgconfig(tracker-miner-2.0)
BuildRequires:  pkgconfig(tracker-sparql-2.0)
BuildRequires:  pkgconfig(zapojit-0.0) >= 0.0.2
# Provide the respective DBus services
Provides:       dbus(org.gnome.OnlineMiners.Flickr)
Provides:       dbus(org.gnome.OnlineMiners.GData)
Provides:       dbus(org.gnome.OnlineMiners.Owncloud)
Provides:       dbus(org.gnome.OnlineMiners.Zpj)

%description
GNOME Online Miners provides a set of crawlers that go through
your online content and index them locally in Tracker. It has miners for
Flickr, Google, OwnCloud and SkyDrive.

%prep
%setup -q

%build
%configure \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# openSUSE packages those files as doc
rm %{buildroot}%{_datadir}/doc/%{name}/{AUTHORS,COPYING,ChangeLog,NEWS,README}

%files
%license COPYING
%doc AUTHORS ChangeLog README NEWS
# Facebook miner
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Facebook.service
%{_libexecdir}/gom-facebook-miner
# Flickr miner
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Flickr.service
%{_libexecdir}/gom-flickr-miner
# GData miner (Google docs)
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.GData.service
%{_libexecdir}/gom-gdata-miner
# Media Server
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.MediaServer.service
%{_libexecdir}/gom-media-server-miner
# OwnCloud miner
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Owncloud.service
%{_libexecdir}/gom-owncloud-miner
# Zapojit miner (microsoft skydrive)
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Zpj.service
%{_libexecdir}/gom-zpj-miner
# Private library
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libgom-1.0.so

%changelog
