# spec file for package steamos-powerbuttond
#
# Copyright (c) 2025 SUSE LLC
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

Name:           steamos-powerbuttond
Version:        3.3
Release:        0%{?dist}
Summary:        Steam Deck power button daemon

License:        BSD-2-Clause
URL:            https://gitlab.com/evlaV/powerbuttond
Source:         %{name}-%{version}.tar.xz
Patch0:         steamos-powerbuttond-service.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libudev)
Provides:       steam-powerbuttond = %{version}
Obsoletes:      steam-powerbuttond < 3.3

%description
This package provides a Steam Deck power button daemon.

%prep
%autosetup -p1

# patch the link order
sed -i 's|$(CC) $(LIB_LDFLAGS) $(LDFLAGS) $< -o $@|$(CC) $< -o $@ $(LDFLAGS) $(LIB_LDFLAGS)|' Makefile

%build
%make_build

%install
%make_install DESTDIR=%{buildroot}
rm -r %{buildroot}/%{_userunitdir}/gamescope-session.service.wants

%pre
%systemd_user_pre %{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service

%files
%license LICENSE
%dir %{_prefix}/lib/hwsupport
%{_prefix}/lib/hwsupport/%{name}
%{_userunitdir}/%{name}.service
%{_prefix}/lib/udev/rules.d/80-steamos-power-button.rules
%dir %{_prefix}/lib/udev/hwdb.d
%{_prefix}/lib/udev/hwdb.d/80-steamos-power-button.hwdb

%changelog
