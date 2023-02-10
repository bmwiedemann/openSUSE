#
# spec file for package budgie-desktop-view
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?suse_version} < 1550
%define _distconfdir %{_sysconfdir}
%endif
%define org org.buddiesofbudgie
Name:           budgie-desktop-view
Version:        1.2.1+0
Release:        0
Summary:        Official Budgie Desktop icons application / implementation
License:        Apache-2.0
Group:          System/GUI/Other
URL:            https://github.com/BuddiesOfBudgie/budgie-desktop-view
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.64.0

%description
Budgie Desktop View is the official Budgie desktop icons application / implementation

%lang_package

%prep
%autosetup

%build
%meson -Dxdg-appdir=%{_sysconfdir}/xdg/autostart
%meson_build

%install
%meson_install
%find_lang %{name}

%files
%license LICENSE.md
%{_bindir}/%{org}.budgie-desktop-view
%{_sysconfdir}/xdg/autostart/%{org}.budgie-desktop-view-autostart.desktop
%{_datadir}/applications/%{org}.budgie-desktop-view.desktop
%{_datadir}/glib-2.0/schemas/%{org}.budgie-desktop-view.gschema.xml

%files lang -f %{name}.lang

%changelog
