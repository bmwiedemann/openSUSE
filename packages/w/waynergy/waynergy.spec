#
# spec file for package waynergy
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2023-2024 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           waynergy
Version:        0.17+0
Release:        0
License:        MIT
Summary:        Synergy client for wayland compositors
URL:            https://github.com/r-c-f/waynergy
Source0:        %{name}-%{version}.tar.xz
Source99:       waynergy-kde-rpmlintrc
#PATCH-FIX-OPENSUSE waynergy-kde-fix-desktop.patch malcolmlewis@opensuse.org -- Remove key "TerminalOptions" in group "Desktop Entry" which is deprecated.
Patch0:         waynergy-kde-fix-desktop.patch
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig(libtls)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
Recommends:     wl-clipboard

%description
An implementation of a synergy client for wayland compositors. Based
on the upstream uSynergy library (heavily modified for more protocol
support and a bit of paranoia).

NOTE: See README.md for using uinput.

%package kde
Summary:        KDE desktop integration
Requires:       waynergy = %{version}
BuildArch:      noarch

%description kde
An implementation of a synergy client for wayland compositors. Based
on the upstream uSynergy library (heavily modified for more protocol
support and a bit of paranoia).

Contains waynergy.desktop must be installed, and the path must be
absolute or the required interface will not be offered.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_bindir}/waynergy
%{_bindir}/waynergy-clip-update
%{_bindir}/waynergy-mapper

%files kde
%{_datadir}/applications/waynergy.desktop

%changelog
