#
# spec file for package wayback
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


Name:           wayback
Version:        0.3
Release:        0
Summary:        Experimental X11 compatibility layer for Wayland
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://gitlab.freedesktop.org/wayback/wayback
Source:         https://gitlab.freedesktop.org/wayback/wayback/-/archive/%version/wayback-%version.tar.gz
Patch1:         0001-wayback-session-fix-sesscmd-handling.patch
Patch2:         0002-CI-Drop-Arch-Linux-build.patch
Patch3:         0003-CI-fedora-Force-repos-and-gpg-keys-to-be-updated.patch
Patch4:         0004-Wayback-is-now-in-Debian.patch
Patch5:         0005-common-wayback_log-add-support-for-setting-verbosity.patch
Patch6:         0006-wayback-compositor-add-support-for-setting-verbosity.patch
Patch7:         0007-Xwayback-properly-handle-and-parse-verbose-option.patch
Patch8:         0008-Xwayback-coding-style-fixes.patch
Patch9:         0009-build-allow-build-with-wlroots-0.20.patch
Patch10:        0010-meson-Drop-support-for-wlroots-0.18.patch
Patch11:        0011-meson-Simplify-wlroots-dependency-to-a-single-array.patch
Patch12:        0012-CI-add-build-jobs-to-build-against-wlroots-0.20.patch
Patch13:        0013-common-optparse-extract-optmatch-for-consistent-opti.patch
Patch14:        0014-Xwayback-use-optmatch-in-the-argument-forwarding-loo.patch
BuildRequires:  c++_compiler
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  wlroots-devel >= 0.20
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
Requires:       xwayland

%description
Wayback is an experimental X compatibility layer which allows for
running full X desktop environments using Wayland components. It is
essentially a stub compositor which provides just enough Wayland
capabilities to host a rootful Xwayland server (no other Wayland
applications).

# same echoed by https://lwn.net/Articles/1031332/

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
