#
# spec file for package gnote
#
# Copyright (c) 2020 SUSE LLC
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


%define base_version 3.36

Name:           gnote
Version:        3.36.2
Release:        0
Summary:        A Port of Tomboy to C++
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://wiki.gnome.org/Apps/Gnote
Source0:        https://download.gnome.org/sources/gnote/%{base_version}/%{name}-%{version}.tar.xz
Source99:       gnote-rpmlintrc
# PATCH-FIX-UPSTREAM gnote-enabling-addin-for-opened-notes.patch bsc#1075342, glgo#GNOME/gnote!11 noteaddin: Fix newly enabled addin not working for opened.
Patch0:         gnote-enabling-addin-for-opened-notes.patch

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libboost_test-devel >= 1.5.1
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.62
BuildRequires:  pkgconfig(gspell-1) >= 1.6.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
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
Supplements:    packageand(%{name}:gnome-shell)

%description -n gnome-shell-search-provider-%{name}
It is the same note taking application, including most of the add-ins (more are
to come). Synchronization support is being worked on.

This package contains a search provider to enable GNOME Shell to get
search results from documents.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
desktop-file-edit --add-category TextEditor %{buildroot}%{_datadir}/applications/%{name}.desktop
%fdupes %{buildroot}%{_datadir}
%find_lang %{name} %{?no_lang_C}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gnote
%{_libdir}/gnote/
# Splitting does not make sense as it's just a lib for gnote itself (and it's plugins)
%{_libdir}/libgnote-%{base_version}.so*
%{_libdir}/libgnote.so
%{_datadir}/applications/gnote.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnote.gschema.xml
%{_datadir}/gnote/
%{_datadir}/icons/hicolor/*/apps/gnote.*
%{_mandir}/man1/gnote.1%{?ext_man}
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/gnote.appdata.xml

%files -n gnome-shell-search-provider-%{name}
%{_datadir}/dbus-1/services/org.gnome.Gnote.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/gnote-search-provider.ini

%files lang -f %{name}.lang

%changelog
