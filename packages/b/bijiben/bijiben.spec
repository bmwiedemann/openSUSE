#
# spec file for package bijiben
#
# Copyright (c) 2021 SUSE LLC
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


Name:           bijiben
Version:        40.1
Release:        0
Summary:        Note editor for GNOME
License:        CC-BY-SA-3.0 AND GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://wiki.gnome.org/Apps/Bijiben
Source0:        https://download.gnome.org/sources/bijiben/40/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.58
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19.3
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libecal-2.0) >= 3.33.92
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.33.92
BuildRequires:  pkgconfig(libhandy-1) >= 1.0.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.26.0

%description
Bijiben is a note editor designed to remain simple to use.

%package -n gnome-shell-search-provider-%{name}
Summary:        Note editor for GNOME -- Search Provider for GNOME Shell
License:        GPL-3.0-or-later
Group:          Productivity/Office/Other
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    packageand(%{name}:gnome-shell)

%description -n gnome-shell-search-provider-%{name}
Bijiben is a note editor designed to remain simple to use.

This package contains a search provider to enable GNOME Shell to get
search results from documents.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dstatic=false \
	-Dupdate-mimed=false \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file org.gnome.Notes DesktopUtility
%fdupes -s %{buildroot}%{_datadir}
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS NEWS README.md TODO
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Notes.desktop
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.gnome.Notes.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Notes*
%{_datadir}/mime/packages/org.gnome.Notes.xml
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/org.gnome.Notes.appdata.xml

%files -n gnome-shell-search-provider-%{name}
%{_datadir}/dbus-1/services/org.gnome.Notes.SearchProvider.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Notes-search-provider.ini
%{_libexecdir}/%{name}-shell-search-provider

%files lang -f %{name}.lang

%changelog
