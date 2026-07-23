#
# spec file for package ssl-cert-check
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global ver 906d34b9e2c495bbed82edcb19404a01f7196b8f
Name:           ssl-cert-check
Version:        5.0
Release:        0
Summary:        Shell script to send notifications when SSL certificates are about to expire
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            https://github.com/Matty9191/ssl-cert-check
Source0:        https://github.com/Matty9191/ssl-cert-check/archive/%{ver}.tar.gz
BuildRequires:  xz
Requires:       bash
Requires:       coreutils
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       openssl
Requires:       sed
Recommends:     mailx
Provides:       monitoring-plugins-ssl-cert-check = 3.29
Obsoletes:      monitoring-plugins-ssl-cert-check <= 3.29
BuildArch:      noarch

%description
ssl-cert-check is a Bourne shell script that can be used to report on expiring
SSL certificates. The script was designed to be run from cron and can e-mail
warnings or log alerts through nagios.

%prep
%setup -q -n %{name}-%{ver}

%build

%install
mkdir -p %{buildroot}/%{_bindir}
sed -e "s|/usr/bin/env bash|/bin/bash|g" ssl-cert-check > %{buildroot}/%{_bindir}/ssl-cert-check
chmod 0755 %{buildroot}/%{_bindir}/ssl-cert-check

%files
%if 0%{?suse_version} >= 1500
%license LICENSE*
%else
%license LICENSE*
%endif
%doc README*
%{_bindir}/ssl-cert-check

%changelog
