#
# spec file for package lldap-cli
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


Name:           lldap-cli
Version:        0.0.1~1724618445.6eb61ce
Release:        0
Summary:        A command line tool for managing LLDAP
License:        GPL-3.0
URL:            https://github.com/Zepmann/lldap-cli
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bash
Requires:       coreutils
Requires:       curl
Requires:       grep
Requires:       jq
Requires:       sed
Requires:       lldap-set-password

# lldap is only built for rust_tier1_arches,
# as this requires lldap-set-password it makes no sense
# to build it on other architectures
ExclusiveArch:  %{rust_tier1_arches}

%description
LLDAP-CLI is a command line interface for LLDAP.

LLDAP uses GraphQL to offer an HTTP-based API. This API is used by an included
web-based user interface. Unfortunately, LLDAP lacks a command-line interface,
which is a necessity for any serious administrator. LLDAP-CLI translates CLI
commands to GraphQL API calls.

%prep
%autosetup

%build
sed -i 's#env bash#bash#g' %{name}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc README.md
%license LICENSE

%changelog
