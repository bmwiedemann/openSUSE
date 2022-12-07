#
# spec file for package wayland-utils
#
# Copyright (c) 2022 SUSE LLC
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


Name:           wayland-utils
Version:        1.1.0
Release:        0
Summary:        Wayland diagnostic utilities
License:        MIT
Group:          System/X11/Utilities
URL:            https://wayland.freedesktop.org/
Source:         https://gitlab.freedesktop.org/wayland/%name/-/releases/%version/downloads/%name-%version.tar.xz
Source1:        https://gitlab.freedesktop.org/wayland/%name/-/releases/%version/downloads/%name-%version.tar.xz.sig
Source3:        %name.keyring
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(wayland-server) >= 1.17

%description
A collection of wayland utilities, presently just wayland-info.

wayland-info displays information about the protocols supported by a
Wayland compositor, and a subset of Wayland protocols it knows about,
namely Linux DMABUF, presentation time, tablet and XDG output
protocols.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/wayland*
%_mandir/man1/wayl*
%license COPYING

%changelog
