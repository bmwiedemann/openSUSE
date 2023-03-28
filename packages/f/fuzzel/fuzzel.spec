#
# spec file for package fuzzel
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


Name:           fuzzel
Version:        1.9.0
Release:        0
Summary:        A Wayland-native application launcher, similar to rofi's drun mode
License:        MIT
Group:          System/X11/Utilities
URL:            https://codeberg.org/dnkl/fuzzel
Source:         https://codeberg.org/dnkl/fuzzel/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.58
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  scdoc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fcft) <  4.0.0
BuildRequires:  pkgconfig(fcft) >= 3.0.0
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(tllist) >= 1.0.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%description
A Wayland-native application launcher, similar to rofi's drun mode.

%prep
%autosetup -n %name

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       zsh

%description    zsh-completion
Zsh command-line completion support for %{name}

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%build
export CFLAGS="%{optflags}"
%if 0%{?sle_version} == 150400 && 0%{?is_opensuse}
# For whatever reason, meson >= 0.58 should already support the c18 standard.
# Setting it to none.
%meson -Denable-cairo=enabled -Dpng-backend=libpng -Dsvg-backend=nanosvg -Dc_std=none
%else
%meson -Denable-cairo=enabled -Dpng-backend=libpng -Dsvg-backend=nanosvg
%endif

%meson_build

%install
%meson_install

%files
%dir %{_datadir}/doc/%{name}
%license %{_datadir}/doc/%{name}/LICENSE
%doc %{_datadir}/doc/%{name}/README.md
%{_datadir}/doc/%{name}/CHANGELOG.md

%{_bindir}/%{name}

%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/%{name}.ini.5%{?ext_man}

%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/%{name}.ini

%files zsh-completion
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/fuzzel.fish

%changelog
