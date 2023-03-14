#
# spec file for package liferea
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.14.1
Release:        0
Summary:        Linux Feed Reader
License:        GPL-2.0-only
Group:          Productivity/Other
URL:            https://lzone.de/liferea/
Source0:        https://github.com/lwindolf/liferea/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# PATCH-FEATURE-OPENSUSE liferea-opensuse-feeds.patch -- Add openSUSE feeds to default feeds
Patch0:         liferea-opensuse-feeds.patch
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  intltool >= 0.40.0
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.0.0
BuildRequires:  pkgconfig(libpeas-gtk-1.0) >= 1.0.0
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.28.2
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27
BuildRequires:  pkgconfig(libxslt) >= 1.1.19
BuildRequires:  pkgconfig(pango) >= 1.4.0
BuildRequires:  pkgconfig(sqlite3) >= 3.7.0
BuildRequires:  pkgconfig(webkit2gtk-4.0)
Requires:       dbus-1 >= 0.30
Requires:       python3-cairo
Requires:       python3-gobject-Gdk

%description
Liferea is an abbreviation for Linux Feed Reader. It is a news
aggregator for online news feeds. It supports a number of different
feed formats including RSS/RDF, CDF, Atom, OCS, and OPML. There are
many other news readers available, but these others are not available
for Linux or require many extra libraries to be installed. Liferea
tries to fill this gap by creating a fast, easy-to-use, easy-to-install
news aggregator for GTK and GNOME.

%lang_package

%prep
%setup -q -n %{name}-%{version}
%patch0

%build
%if 0%{?suse_version} >= 01550 || 0%{?sle_version} >= 150200
export WEBKIT_DISABLE_COMPOSITING_MODE=1
%endif
%configure --disable-static
%make_build

%install
%make_install
%suse_update_desktop_file net.sourceforge.liferea X-SuSE-RSS-News
%find_lang %{name} %{?no_lang_C}
rm doc/Makefile*
rm doc/html/Makefile*

%fdupes %{buildroot}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/liferea
%{_bindir}/liferea-add-feed
%{_datadir}/applications/net.sourceforge.liferea.desktop
%{_datadir}/dbus-1/services/net.sourceforge.liferea.service
%{_datadir}/%{name}/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/net.sourceforge.liferea.appdata.xml
%{_datadir}/GConf/gsettings/liferea.convert
%{_datadir}/glib-2.0/schemas/net.sf.liferea.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.*
%{_libdir}/%{name}/
%doc %{_mandir}{,/*}/man1/liferea.1*

# We can't really move the localized manpages to the lang package, since they'd
# create a conflict between the lang subpackage and bundles
%files lang -f %{name}.lang

%changelog
