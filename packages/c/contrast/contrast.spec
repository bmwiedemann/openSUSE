#
# spec file for package contrast
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


%define lname   org.gnome.design.Contrast
%define lurl    23b9cf42e16630f0eab2eeb1686eb25b
Name:           contrast
Version:        0.0.10
Release:        0
Summary:        Check difference between two colors
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/design/contrast
Source:         %{url}/uploads/%{lurl}/%{name}-%{version}.tar.xz
BuildRequires:  appstream-glib
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) 
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) 

%description
Check whether the contrast between two colors meet the WCAG requirements.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files
%license LICENSE*
%doc README*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{lname}.desktop
%{_datadir}/icons/hicolor/*/*/%{lname}*svg
%{_datadir}/metainfo/%{lname}.metainfo.xml

%files lang -f %{name}.lang

%changelog

