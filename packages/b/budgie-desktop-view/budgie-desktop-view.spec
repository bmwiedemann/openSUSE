#
# spec file for package budgie-desktop-view
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 Callum Farmer <gmbr3@opensuse.org>
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
Name:           budgie-desktop-view
Version:        1.1.1
Release:        0
Summary:        Official Budgie Desktop icons application / implementation
License:        Apache-2.0
Group:          System/GUI/Other
URL:            https://getsol.us/solus/experiences/
Source:         https://github.com/getsolus/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.xz
Source1:        https://github.com/getsolus/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  intltool
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-3.0)

%description
Budgie Desktop View is the official Budgie desktop icons application / implementation

%prep
%autosetup

%build
%meson -Dxdg-appdir=%{_distconfdir}/xdg/autostart
%meson_build

%install
%meson_install

%files
%license LICENSE.md
%{_bindir}/us.getsol.budgie-desktop-view
%{_distconfdir}/xdg/autostart/us.getsol.budgie-desktop-view-autostart.desktop
%{_datadir}/applications/us.getsol.budgie-desktop-view.desktop
%{_datadir}/glib-2.0/schemas/us.getsol.budgie-desktop-view.gschema.xml

%changelog
