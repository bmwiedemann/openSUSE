#
# spec file for package foliate
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


%define oname com.github.johnfactotum.Foliate
Name:           foliate
Version:        3.2.0
Release:        0
Summary:        A GTK eBook reader
License:        GPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://johnfactotum.github.io/foliate/
Source:         %{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE foliate-fix-export-of-incorrect-dep-Adw.patch -- Dependencies are not exported correctly
Patch0:         foliate-fix-export-of-incorrect-dep-Adw.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gjs-1.0) >= 1.76
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.12
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4
BuildRequires:  pkgconfig(webkitgtk-6.0)
Requires:       gjs
BuildArch:      noarch

%description
A GTK eBook viewer, built with GJS and Epub.js.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

chmod a-x README.md COPYING
find %{buildroot}/%{_datadir} -type f -executable -exec chmod -x "{}" +
%fdupes %{buildroot}/%{_datadir}/%{oname}

%find_lang %{oname} --with-gnome

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/%{oname}
%{_datadir}/glib-2.0/schemas/
%{_datadir}/metainfo/%{oname}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/*

%files lang -f %{oname}.lang

%changelog
