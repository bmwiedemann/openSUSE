#
# spec file for package wmenu
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


Name:           wmenu
Version:        0.1.3
Release:        0
Summary:        A dynamic menu for Sway and wlroots-based Wayland compositors
License:        MIT
Group:          System/X11/Utilities
URL:            https://sr.ht/~adnano/wmenu
Source:         https://git.sr.ht/~adnano/wmenu/archive/%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

%description
An dynamic menu for Sway and wlroots based Wayland compositors (requires
wlr_layer_shell_v1 support).

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
