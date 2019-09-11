#
# spec file for package gnome-do-plugins
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define __find_provides sh -c '/usr/lib/rpm/find-provides %{name} | grep -v mono || echo ""'
%define with_flickr 0

Name:           gnome-do-plugins
Version:        0.8.5
Release:        0
Url:            http://do.davebsd.com
Source:         https://launchpad.net/do-plugins/trunk/0.8.5/+download/gnome-do-plugins-0.8.5.tar.gz
# PATCH-FIX-UPSTREAM gnome-do-plugins-no-transmission.patch lp#1354678 dimstar@opensuse.org -- Do not build the Transmission plugin if configure did not find the dependencies
Patch0:         gnome-do-plugins-no-transmission.patch
Summary:        Plugins for GNOME Do
License:        GPL-3.0
Group:          Productivity/Other
# Needed by patch0
BuildRequires:  gnome-common
BuildRequires:  gnome-do >= 0.8.1
BuildRequires:  intltool
BuildRequires:  mono-data-sqlite
BuildRequires:  mono-devel
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
## Disabled since we do not want to depend on gst-0_10 anymore.
## BuildRequires:  pkgconfig(banshee-collection-indexer) >= 2.1
%if %{?with_flickr}
BuildRequires:  pkgconfig(flickrnet)
%endif
BuildRequires:  pkgconfig(gconf-sharp-2.0)
BuildRequires:  pkgconfig(gdata-sharp-acl)
BuildRequires:  pkgconfig(gdata-sharp-calendar)
BuildRequires:  pkgconfig(gdata-sharp-contacts)
BuildRequires:  pkgconfig(gdata-sharp-core)
BuildRequires:  pkgconfig(gdata-sharp-documents)
BuildRequires:  pkgconfig(gdata-sharp-youtube)
BuildRequires:  pkgconfig(glade-sharp-2.0)
BuildRequires:  pkgconfig(glib-sharp-2.0)
BuildRequires:  pkgconfig(gnome-desktop-sharp-2.0)
BuildRequires:  pkgconfig(gnome-keyring-sharp-1.0)
BuildRequires:  pkgconfig(gnome-sharp-2.0)
BuildRequires:  pkgconfig(gnome-vfs-sharp-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(mono-addins)
BuildRequires:  pkgconfig(mono-addins-gui)
BuildRequires:  pkgconfig(mono-addins-setup)
BuildRequires:  pkgconfig(ndesk-dbus-1.0)
BuildRequires:  pkgconfig(ndesk-dbus-glib-1.0)
BuildRequires:  pkgconfig(notify-sharp)
BuildRequires:  pkgconfig(wnck-sharp-1.0)
%if 0%{?suse_version} > 1140
BuildRequires:  pkgconfig(dbus-sharp-1.0)
BuildRequires:  pkgconfig(dbus-sharp-glib-1.0)
%endif
Requires:       %{name}-lang = %{version}
Requires:       gnome-do
Requires:       xdg-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GNOME Do allows you to quickly search for many objects present in your
GNOME desktop environment (applications, Evolution contacts, Firefox
bookmarks, files, artists and albums in Rhythmbox, Pidgin buddies) and
perform commonly used commands on those objects (Run, Open, Email,
Chat, Play, etc.).

This package contains various plugins for GNOME Do.


%lang_package
%prep
%setup -q
%patch0 -p1

%build
# Needed by patch0
autoreconf -fi
%configure
%__make %{?jobs: -j%jobs}

%install
%makeinstall
%find_lang %{name}

%files
%defattr(-, root, root)
%doc COPYING AUTHORS COPYRIGHT
%{_libdir}/gnome-do/plugins

%files lang -f %{name}.lang

%changelog
