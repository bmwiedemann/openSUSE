#
# spec file for package wayback
#
# Copyright (c) 2025 SUSE LLC
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


Name:           wayback
Version:        0.1
Release:        0
Summary:        Experimental X11 compatibility layer for Wayland
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://gitlab.freedesktop.org/wayback/wayback
Source:         https://gitlab.freedesktop.org/wayback/wayback/-/archive/%version/wayback-%version.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  wlroots-devel >= 0.19
Requires:       xwayland

%description
Wayback is an experimental X compatibility layer which allows for
running full X desktop environments using Wayland components. It is
essentially a stub compositor which provides just enough Wayland
capabilities to host a rootful Xwayland server.

%prep
%autosetup -p1

%build
# includedir intentional, cf. bugzilla.opensuse.org/795968
%meson \
	--includedir="%_includedir/%name" -Dgenerate_manpages=disabled
%meson_build

%install
%meson_install

%files
%_bindir/Xwayback
%_bindir/wayback-session
%_libexecdir/wayback*
%license LICENSE

%changelog
