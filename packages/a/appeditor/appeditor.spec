#
# spec file for package appeditor
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           appeditor
Version:        1.1.0
Release:        0
Summary:        Application Entry Editor
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/donadigo/appeditor
Source:         https://github.com/donadigo/appeditor/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX_UPSTREAM -- Fix build with vala >= 0.46
Patch0:         appeditor-1.1.0-vala-0.46.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0)
Recommends:     %{name}-lang

%description
A program to edit application entries shown in the application menu,
and to edit their properties.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.donadigo.appeditor GTK Utility Settings
%find_lang com.github.donadigo.appeditor %{name}.lang
%fdupes %{buildroot}/%{_datadir}

%files
%doc README.md
%{_bindir}/com.github.donadigo.appeditor
%{_datadir}/applications/com.github.donadigo.appeditor.desktop
%dir %{_datadir}/contractor
%{_datadir}/contractor/com.github.donadigo.appeditor.contract
%{_datadir}/glib-2.0/schemas/com.github.donadigo.appeditor.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.donadigo.appeditor.??g
%{_datadir}/metainfo/com.github.donadigo.appeditor.appdata.xml

%files lang -f %{name}.lang

%changelog
