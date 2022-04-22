#
# spec file for package fuzzel
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


Name:           fuzzel
Version:        1.7.0
Release:        0
Summary:        A Wayland-native application launcher, similar to rofi's drun mode
License:        MIT
Group:          System/X11/Utilities
URL:            https://codeberg.org/dnkl/fuzzel
Source:         https://codeberg.org/dnkl/fuzzel/archive/%{version}.tar.gz
BuildRequires:  meson >= 0.48.0
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

%build
export CFLAGS="%{optflags}"
%meson -Denable-cairo=enabled -Dpng-backend=libpng -Dsvg-backend=nanosvg

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

%files zsh-completion
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
