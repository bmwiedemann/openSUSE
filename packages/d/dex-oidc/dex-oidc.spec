#
# spec file for package dex-oidc
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


# Project name when using go tooling.
%define go_version 1.15

Name:           dex-oidc
Version:        2.28.1
Release:        0
Summary:        OpenID Connect Identity (OIDC) and OAuth 2.0 Provider with Pluggable Connectors
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/dexidp/dex
Source0:        dex-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = %{go_version}

Requires(post): %fillup_prereq
Conflicts:      dex
# caasp-dex was last used in openSUSE Leap15
Provides:       caasp-dex = %{version}
Obsoletes:      caasp-dex < %{version}
ExcludeArch:    %{ix86}
%{go_nostrip}
%{go_provides}

%description
Dex is an identity service that uses OpenID Connect to drive authentication for other apps.

Dex is NOT a user-management system, but acts as a portal to other identity providers through "connectors."
This lets dex defer authentication to LDAP servers, SAML providers, or established identity providers like
GitHub, Google, and Active Directory. Clients write their authentication logic once to talk to dex, then
dex handles the protocols for a given backend.

%prep
%setup -q -n dex-%{version} -a 1

%build
%define ldflags "-w -X github.com/dexidp/dex/version.Version=%{version}"

%{goprep} github.com/dexidp/dex
%{gobuild} -mod=vendor -ldflags %{ldflags} cmd/dex

%install
%{goinstall}
%{gofilelist}

# Install the web content
for file in $(find web -type f); do
  install -D -m 0644 $file %{buildroot}/%{_datadir}/%{name}/$file
done
%fdupes %{buildroot}%{_datadir}/%{name}

%files -f file.lst
%license LICENSE
%doc README.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/web
%dir %{_datadir}/%{name}/web/static
%dir %{_datadir}/%{name}/web/static/img
%dir %{_datadir}/%{name}/web/templates
%dir %{_datadir}/%{name}/web/themes
%{_datadir}/%{name}/web/*
%{_bindir}/dex

%changelog
