#
# spec file for package tofi
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


Name:           tofi
Version:        0.9.1
Release:        0
Summary:        Tiny dynamic menu for Wayland
License:        MIT
URL:            https://github.com/philj56/tofi
Source:         https://github.com/philj56/tofi/archive/refs/tags/v%{version}.tar.gz#$/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

%description
A simple dmenu / rofi replacement for wlroots-based Wayland
compositors such as Sway.

When configured correctly, tofi can get on screen within a single frame.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Bash command-line completion support for %{name}.

%prep
%autosetup

%build
%meson --sysconfdir=%{_distconfdir}
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE

%{_bindir}/tofi
%{_bindir}/tofi-drun
%{_bindir}/tofi-run
%dir %{_distconfdir}/xdg/tofi
%{_distconfdir}/xdg/tofi/config
%{_mandir}/man1/tofi*
%{_mandir}/man5/tofi.5*

%files bash-completion
%{_datadir}/bash-completion/*

%changelog
