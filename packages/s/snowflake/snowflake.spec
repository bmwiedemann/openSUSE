#
# spec file for package snowflake
#
# Copyright (c) 2024 SUSE LLC
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


Name:           snowflake
Version:        2.11.0
Release:        0
Summary:        Pluggable Transport using WebRTC, inspired by Flashproxy.
License:        BSD-3-Clause
URL:            https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}.service
BuildRequires:  go >= 1.21

%description
Snowflake proxy to help censored users connect to the Tor network

%prep
%autosetup -p 1 -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/snowflake ./proxy

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_sbindir}/%{name}"

# Install the systemd unit file
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

%pre
%service_add_pre snowflake.service

%post
%service_add_post snowflake.service

%preun
%service_del_preun snowflake.service

%postun
%service_del_postun snowflake.service

%files
%doc README.md
%license LICENSE
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
