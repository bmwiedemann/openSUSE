#
# spec file for package wlogout
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Lorenz Holzbauer
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


Name:           wlogout
Version:        1.2.2
Release:        0
Summary:        A wayland based logout menu
License:        MIT
URL:            https://github.com/ArtsyMacaw/wlogout
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)

%description
A wayland based logout menu.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/zsh/
%{_datadir}/fish/
%{_datadir}/bash-completion/
%dir %{_sysconfdir}/%{name}

%license LICENSE

%doc README.md
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/%{name}.5%{?ext_man}

%config(noreplace) %{_sysconfdir}/%{name}/*

%changelog
