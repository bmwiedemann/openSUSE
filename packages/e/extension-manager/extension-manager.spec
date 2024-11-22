#
# spec file for package extension-manager
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


%define         appname com.mattjakeman.ExtensionManager
Name:           extension-manager
Version:        0.5.1
Release:        0
Summary:        A utility for browsing and installing GNOME Shell Extensions
License:        GPL-3.0-only
URL:            https://github.com/mjakeman/extension-manager
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libbacktrace-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(text-engine-0.1)

%description
A native tool for browsing, installing, and managing GNOME Shell Extensions.

%lang_package

%prep
%autosetup

%build
export CFLAGS="%{optflags} -Wno-error=return-type -Wno-return-mismatch -Wno-int-conversion -Wno-incompatible-pointer-types"
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_iconsdir}/hicolor/scalable/apps/%{appname}.svg
%{_iconsdir}/hicolor/symbolic/apps/%{appname}-symbolic.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml

%files lang -f %{name}.lang

%changelog
