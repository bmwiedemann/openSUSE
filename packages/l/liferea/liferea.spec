#
# spec file for package liferea
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           liferea
Version:        2.0
Release:        0
Summary:        Linux Feed Reader
License:        GPL-2.0-only
Group:          Productivity/Other
URL:            https://lzone.de/liferea/
Source0:        %{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE liferea-opensuse-feeds.patch -- Add openSUSE feeds to default feeds
Patch0:         liferea-opensuse-feeds.patch
BuildSystem:    meson
BuildRequires:  meson
BuildRequires:  intltool
BuildRequires:  pkgconfig(gobject-introspection-1.0)
ExcludeArch:    %{ix86}

%description
Liferea is an abbreviation for Linux Feed Reader. It is a news
aggregator for online news feeds. It supports a number of different
feed formats including RSS/RDF, CDF, Atom, OCS, and OPML. There are
many other news readers available, but these others are not available
for Linux or require many extra libraries to be installed. Liferea
tries to fill this gap by creating a fast, easy-to-use, easy-to-install
news aggregator for GTK and GNOME.

%lang_package

%generate_buildrequires
%meson_buildrequires

%install -a
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/liferea
%{_datadir}/applications/net.sourceforge.liferea.desktop
%{_datadir}/dbus-1/services/net.sourceforge.liferea.service
%{_datadir}/%{name}/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/net.sourceforge.liferea.appdata.xml
%{_datadir}/glib-2.0/schemas/net.sf.liferea.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.*
%{_libdir}/%{name}/
%doc %{_mandir}{,/*}/man1/liferea.1*

# We can't really move the localized manpages to the lang package, since they'd
# create a conflict between the lang subpackage and bundles
%files lang -f %{name}.lang

%changelog
