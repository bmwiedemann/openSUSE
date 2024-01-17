#
# spec file for package steamtricks-data
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define ssletcdir %{_sysconfdir}/ssl
%define cabundle  /var/lib/ca-certificates/ca-bundle.pem
%define sslcerts  %{ssletcdir}/certs
%define crtrun    %{_prefix}/lib/ca-certificates/update.d/81etc_ssl_crt_steamtricks.run
Name:           ca-certificates-steamtricks
Version:        1
Release:        0
Summary:        Provides /etc/ssl/certs/ca-certificates.crt
License:        GPL-2.0
Group:          Amusements/Games/Other
Url:            https://github.com/steamtricks/steamtricks/issues/42
BuildRequires:  ca-certificates
Requires:       ca-certificates
Requires:       coreutils
Provides:       steamtricks-data-252950-Rocket_League
BuildArch:      noarch

%description
Provides /etc/ssl/certs/ca-certificates.crt as required by certain proprietary
software.

This package was created as part of a workaround by steamtricks.

%prep

%build

%install
install -D -m 755 /dev/null %{buildroot}%{crtrun}
(
cat <<-EOF
#!/bin/bash
if [ ! -f %{sslcerts}/ca-certificates.crt ] && [ -e %{sslcerts} ] ; then
  # compatability fix for proprietary software
  ln -sf %{cabundle} %{sslcerts}/ca-certificates.crt
fi
EOF
) > %{buildroot}%{crtrun}

%post
update-ca-certificates -f || true

%files
%defattr(-,root,root,-)
%{crtrun}

%changelog
