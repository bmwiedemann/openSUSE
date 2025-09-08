# spec file for package steam-powerbuttond
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

Name:           steam-powerbuttond
Version:        0+git20240501.6c89b0e
Release:        0%{?dist}
Summary:        Steam Deck power button daemon

License:        GPL-3.0
URL:            https://github.com/ShadowBlip/steam-powerbuttond
Source:         %{name}-%{version}.tar.xz

BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
Conflicts:      powerbuttond
BuildArch:      noarch

%description
This package provides a Steam Deck power button daemon.

%prep
%setup

sed -i 's|/usr/bin/env python|/usr/bin/python3|g' steam-powerbuttond
sed -i 's|/usr/local/bin|/usr/bin|g' steam-powerbuttond.service

%build

%install
mkdir -p %{buildroot}%{_unitdir}/
install -D -m 755 ./steam-powerbuttond %{buildroot}%{_bindir}/steam-powerbuttond
install -m 644 ./steam-powerbuttond.service %{buildroot}%{_unitdir}/steam-powerbuttond.service

%pre
%systemd_pre steam-powerbuttond.service

%post
%systemd_post steam-powerbuttond.service

%preun
%systemd_preun steam-powerbuttond.service

%postun
%systemd_postun_with_restart steam-powerbuttond.service

%files
%license LICENSE
%{_bindir}/steam-powerbuttond
%{_unitdir}/steam-powerbuttond.service

%changelog
