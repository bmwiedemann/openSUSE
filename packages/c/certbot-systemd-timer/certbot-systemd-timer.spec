#
# spec file for package certbot-systemd-timer
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


%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           certbot-systemd-timer
Version:        0.0
Release:        0
Summary:        systemd timer unit to renew certbot certificates
License:        Apache-2.0
URL:            https://github.com/agross/systemd-certbot-renew
Source10:       certbot-renew-systemd.service
Source11:       certbot-renew-systemd.timer
Source12:       certbot-sysconfig-certbot
Source13:       README
Source14:       LICENSE.txt
Requires:       python3-certbot >= 0.21.1
Requires(post): %fillup_prereq
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       systemd
%{?systemd_ordering}

%description
Optional systemd timer, which takes care of certbot certificate renewals.

%prep
cp %{SOURCE13} %{SOURCE14} .

%build
:

%install
install -Dm 0644 %{SOURCE10} %{buildroot}%{_unitdir}/certbot-renew.service
install -Dm 0644 %{SOURCE11} %{buildroot}%{_unitdir}/certbot-renew.timer
install -Dm 0644 %{SOURCE12} %{buildroot}%{_fillupdir}/sysconfig.certbot
mkdir -p %{buildroot}%{_sbindir}

ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rccertbot-renew

%preun
%service_del_preun certbot-renew.service

%post
%service_add_post certbot-renew.service
%{fillup_only -n certbot}

%postun
%service_del_postun certbot-renew.service

%pre
%service_add_pre certbot-renew.service

%files
%doc README
%license LICENSE.txt
%{_fillupdir}/sysconfig.certbot
%{_unitdir}/certbot-renew.service
%{_unitdir}/certbot-renew.timer
%{_sbindir}/rccertbot-renew

%changelog
