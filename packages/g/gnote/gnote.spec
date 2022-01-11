#
# spec file for package gnote
#
# Copyright (c) 2022 SUSE LLC
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


%define base_version 41

Name:           gnote
Version:        41.2
Release:        0
Summary:        A Port of Tomboy to C++
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://wiki.gnome.org/Apps/Gnote
Source0:        https://download.gnome.org/sources/gnote/41/%{name}-%{version}.tar.xz
Source99:       gnote-rpmlintrc

BuildRequires:  c++_compiler
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  libboost_test-devel >= 1.5.1
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.62
BuildRequires:  pkgconfig(gspell-1) >= 1.6.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.20
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.18
BuildRequires:  pkgconfig(libsecret-1) >= 0.8
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(uuid)

%description
It is the same note taking application, including most of the add-ins (more are
to come). Synchronization support is being worked on.

%package -n gnome-shell-search-provider-%{name}
Summary:        Note editor for GNOME -- Search Provider for GNOME Shell
Group:          Productivity/Office/Other
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    (%{name} and gnome-shell)

%description -n gnome-shell-search-provider-%{name}
It is the same note taking application, including most of the add-ins (more are
to come). Synchronization support is being worked on.

This package contains a search provider to enable GNOME Shell to get
search results from documents.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
desktop-file-edit --add-category TextEditor %{buildroot}%{_datadir}/applications/org.gnome.Gnote.desktop
%fdupes %{buildroot}%{_datadir}
%find_lang %{name} %{?no_lang_C}

%if %suse_version >= 1550
%ldconfig_scriptlets
%else
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%license COPYING
%doc AUTHORS NEWS README
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gnote
%{_libdir}/gnote/
# Splitting does not make sense as it's just a lib for gnote itself (and it's plugins)
%{_libdir}/libgnote-%{base_version}.so*
%{_datadir}/applications/org.gnome.Gnote.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnote.gschema.xml
%{_datadir}/gnote/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Gnote*
%{_mandir}/man1/gnote.1%{?ext_man}
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/org.gnome.Gnote.appdata.xml

%files -n gnome-shell-search-provider-%{name}
%{_datadir}/dbus-1/services/org.gnome.Gnote.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Gnote.search-provider.ini

%files lang -f %{name}.lang

%changelog
