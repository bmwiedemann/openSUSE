#
# spec file for package darkman
#
# Copyright (c) 2026 SUSE LLC
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


Name:           darkman
Version:        2.3.1
Release:        0
Summary:        Framework for dark-mode and light-mode transitions
# Legal-Review-Notice: ISC is upstream. Vendored modules add Apache-2.0
# (cobra, mousetrap, astral), BSD-2-Clause (godbus), BSD-3-Clause (pflag)
# and MIT (go-yaml, tint). No copyleft in vendor.tar.zst.
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
URL:            https://gitlab.com/whynothugo/darkman
Source:         https://gitlab.com/WhyNotHugo/darkman/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Source1:        vendor.tar.zst
BuildRequires:  c_compiler
BuildRequires:  desktop-file-utils
BuildRequires:  golang(API) >= 1.21
BuildRequires:  pkgconfig
BuildRequires:  zstd
BuildRequires:  pkgconfig(systemd)

%description
darkman is a tool that allows automating transitioning to dark mode
and sundown, and back to light mode at sunrise. It allows placing
drop-in scripts to be run automatically at those times.

%prep
%autosetup -p1 -a1 -n %{name}-v%{version}
# rpm requires a real interpreter in the shebang, not /usr/bin/env.
sed -i 's|^#!%{_bindir}/env sh$|#!/bin/sh|' examples/*.sh

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-X main.Version=%{version}" ./cmd/darkman
./darkman completion bash > darkman.bash
./darkman completion zsh > _darkman
./darkman completion fish > darkman.fish

%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}

install -Dm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm 0644 %{name}.conf.5 %{buildroot}%{_mandir}/man5/%{name}.conf.5

install -Dm 0644 contrib/darkman.service %{buildroot}%{_userunitdir}/darkman.service

install -Dm644 contrib/dbus/nl.whynothugo.darkman.service \
  %{buildroot}%{_datadir}/dbus-1/services/nl.whynothugo.darkman.service

install -Dm644 contrib/dbus/org.freedesktop.impl.portal.desktop.darkman.service \
  %{buildroot}%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.darkman.service

install -Dm644 contrib/portal/darkman.portal \
  %{buildroot}%{_datadir}/xdg-desktop-portal/portals/darkman.portal

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  --set-icon=preferences-desktop-display \
  --add-category=DesktopSettings \
  darkman.desktop

install -Dm644 darkman.bash %{buildroot}%{_datadir}/bash-completion/completions/darkman
install -Dm644 _darkman %{buildroot}%{_datadir}/zsh/site-functions/_darkman
install -Dm644 darkman.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/darkman.fish

install -d %{buildroot}%{_datadir}/darkman/examples
install -m 0755 examples/*.sh %{buildroot}%{_datadir}/darkman/examples/

%check
go test -mod=vendor ./...

%files
%license LICENCE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/%{name}.conf.5%{?ext_man}
%{_userunitdir}/darkman.service
%{_datadir}/applications/darkman.desktop
%{_datadir}/bash-completion/completions/darkman
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_darkman
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/darkman.fish
%dir %{_datadir}/darkman
%dir %{_datadir}/darkman/examples
%{_datadir}/darkman/examples/*

%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/nl.whynothugo.darkman.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.darkman.service

%dir %{_datadir}/xdg-desktop-portal
%dir %{_datadir}/xdg-desktop-portal/portals
%{_datadir}/xdg-desktop-portal/portals/darkman.portal

%changelog
