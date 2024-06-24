#
# spec file for package resources
#
# Copyright (c) 2024 mantarimay
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


%bcond_without test
%define appid net.nokyan.Resources
Name:           resources
Version:        1.5.0
Release:        0
Summary:        Monitor your system processes 
License:        GPL-3.0-or-later
URL:            https://github.com/nokyan/resources
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  appstream-glib
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5.0
Requires:       polkit
Requires:       dmidecode

%description
Resources is a simple yet powerful monitor for your system resources and
processes, written in Rust and using GTK 4 and libadwaita for its GUI.

%lang_package

%prep
%autosetup -a1

%build
%meson -Dprofile=default
%meson_build

%install
%meson_install

%find_lang %{name}

%check
%if %{with test}
%meson_test
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}*.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%exclude %{_datadir}/polkit-1/actions/%{appid}.policy
%{_libexecdir}/%{name}/

%files lang -f %{name}.lang

%changelog
