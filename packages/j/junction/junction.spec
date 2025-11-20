#
# spec file for package junction
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


%define         appname re.sonny.Junction
Name:           junction
Version:        1.10
Release:        0
Summary:        Application/browser chooser
License:        GPL-3.0-only
URL:            https://github.com/sonnyp/Junction
Source0:        %{name}-%{version}.tar.zst
Source99:       junction-rpmlintrc
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  gjs
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  zstd
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
Requires:       /usr/bin/gjs

%description
Set Junction as the default application for a resource and let it do the rest.
Junction will pop up and offer multiple options to handle it.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
ln -rsf %{buildroot}%{_bindir}/%{appname} %{buildroot}%{_bindir}/%{name}

%check
# node_modules error out
%meson_test

%files
%license COPYING
%doc README.md notes.md
%{_bindir}/%{appname}
%{_bindir}/%{name}
%{_datadir}/%{appname}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/%{appname}.svg
%{_iconsdir}/hicolor/symbolic/apps/%{appname}-symbolic.svg

%changelog
