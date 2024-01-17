#
# spec file for package wondershaper
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


Name:           wondershaper
Version:        1.4.1+git.20211015
Release:        0
Summary:        A network QoS (Quality of Service) script
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://github.com/magnific0/wondershaper
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE wondershaper-fix-conf-path.patch -- Use /etc/wondershaper for wondershaper.conf place
Patch0:         wondershaper-fix-conf-path.patch
# PATCH-FIX-OPENSUSE wondershaper-systemd-hardening.patch -- Added hardening to systemd service(s) (bsc#1181400)
Patch1:         wondershaper-systemd-hardening.patch
BuildRequires:  systemd-rpm-macros
Requires:       iproute2
BuildArch:      noarch

%description
Many cablemodem and ADSL users experience horrifying latency while
uploading or downloading. They also notice that uploading hampers
downloading greatly. The wondershaper neatly addresses these issues,
allowing users of a router with a wondershaper to continue using SSH
over a loaded link happily.

%prep
%autosetup

# Fix E: env-script-interpreter (Badness: 9) 
sed -i 's|/usr/bin/env bash|/usr/bin/bash|' %{name}

%build

%install
install -pDm 755 %{name} %{buildroot}/%{_sbindir}/%{name}
install -pDm 644 %{name}.service %{buildroot}/%{_unitdir}/%{name}.service
install -pDm 644 %{name}.conf %{buildroot}/%{_sysconfdir}/%{name}/%{name}.conf

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc ChangeLog README.bhubert README.md VERSION
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/%{name}.conf

%changelog
