#
# spec file for package darkman
#
# Copyright (c) 2021 SUSE LLC
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
Version:        2.0.1
Release:        0
Summary:        Framework for dark-mode and light-mode transitions
License:        ISC
Group:          Productivity/Other
URL:            https://gitlab.com/whynothugo/darkman
Source:         https://gitlab.com/WhyNotHugo/darkman/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Source1:        vendor.tar.zst
Patch0:         0001-fix-dependencies.patch
BuildRequires:  golang-packaging
BuildRequires:  zstd
BuildRequires:  scdoc

%description
darkman is a tool that allows automating transitioning to dark mode
and sundown, and back to light mode at sunrise. It allows placing
drop-in scripts to be run automatically at those times.

%prep
%autosetup -p1 -a1 -n %{name}-v%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-X main.Version=%{version}" ./cmd/darkman

scdoc < darkman.1.scd > darkman.1

%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}
ln -s %{name} %{buildroot}%{_bindir}/%{name}ctl

install -Dm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

install -Dm 0644 %{name}.service %{buildroot}%{_prefix}/lib/systemd/user/darkman.service

install -Dm644 contrib/dbus/nl.whynothugo.darkman.service \
  %{buildroot}%{_datadir}/dbus-1/services/nl.whynothugo.darkman.service

install -Dm644 contrib/dbus/org.freedesktop.impl.portal.desktop.darkman.service \
  %{buildroot}%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.darkman.service

install -Dm644 contrib/portal/darkman.portal \
  %{buildroot}%{_datadir}/xdg-desktop-portal/portals/darkman.portal


%files
%license LICENCE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}ctl
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_prefix}/lib/systemd/user/darkman.service

%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/nl.whynothugo.darkman.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.darkman.service

%dir %{_datadir}/xdg-desktop-portal
%dir %{_datadir}/xdg-desktop-portal/portals
%{_datadir}/xdg-desktop-portal/portals/darkman.portal

%changelog
