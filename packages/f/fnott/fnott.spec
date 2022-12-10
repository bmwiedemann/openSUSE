#
# spec file for package fnott
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


Name:           fnott
Version:        1.3.0
Release:        0
Summary:        Lightweight notification daemon for Wayland
License:        MIT
Group:          System/GUI/Other
URL:            https://codeberg.org/dnkl/fnott
Source0:        https://codeberg.org/dnkl/fnott/archive/%{version}.tar.gz
BuildRequires:  meson >= 0.58
%if 0%{?sle_version} >= 150400
BuildRequires:  gcc11
%else
BuildRequires:  gcc >= 8
%endif
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  scdoc
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fcft) < 4.0.0
BuildRequires:  pkgconfig(fcft) >= 3.0.0
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(tllist) >= 1.0.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)

%description
Lightweight notification daemon for Wayland.

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
%meson \
%if 0%{?sle_version} == 150400 && 0%{?is_opensuse}
  -Dc_std=c11 \
%endif
  -Db_lto=true
%meson_build

%install
%meson_install

%files
%{_bindir}/fnott
%{_bindir}/fnottctl

%{_mandir}/man1/fnott.1%{?ext_man}
%{_mandir}/man1/fnottctl.1%{?ext_man}
%{_mandir}/man5/fnott.ini.5%{?ext_man}

%dir %{_datadir}/doc/%{name}
%license %{_datadir}/doc/%{name}/LICENSE
%doc %{_datadir}/doc/%{name}/README.md
%doc CHANGELOG.md

%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/fnott.ini
%{_datadir}/applications/fnott.desktop

%files zsh-completion
%{_datadir}/zsh/site-functions/_fnott
%{_datadir}/zsh/site-functions/_fnottctl

%changelog
