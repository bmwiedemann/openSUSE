#
# spec file for package flatpak-xdg-utils
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


Name:           flatpak-xdg-utils
Summary:        Command-line tools for use inside Flatpak sandboxes
Version:        1.0.6
Release:        0
License:        LGPL-2.1-or-later
URL:            https://github.com/flatpak/flatpak-xdg-utils
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  c_compiler
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)

Requires:       flatpak-spawn

%description
This package contains a number of command-line utilities for use inside
Flatpak sandboxes. They work by talking to portals.

%package -n     flatpak-spawn
Summary:        Command-line frontend for the org.freedesktop.Flatpak service
License:        LGPL-2.1-or-later

%description -n flatpak-spawn
This package contains a number of command-line utilities for use inside
Flatpak sandboxes. They work by talking to portals.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
mv $RPM_BUILD_ROOT%{_bindir}/xdg-email $RPM_BUILD_ROOT%{_bindir}/flatpak-xdg-email
mv $RPM_BUILD_ROOT%{_bindir}/xdg-open $RPM_BUILD_ROOT%{_bindir}/flatpak-xdg-open

%files
%doc README.md
%license COPYING
%{_bindir}/flatpak-xdg-email
%{_bindir}/flatpak-xdg-open

%files -n flatpak-spawn
%license COPYING
%{_bindir}/flatpak-spawn

%changelog
