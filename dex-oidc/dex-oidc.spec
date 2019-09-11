#
# spec file for package dex-oidc
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dex-oidc
Version:        2.13.0
Release:        0
Summary:        OpenID Connect Identity (OIDC) and OAuth 2.0 Provider with Pluggable Connectors
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/dexidp/dex
Source:         https://github.com/dexidp/dex/archive/v%{version}.tar.gz
Patch1:         fix-default-web-path.patch
Patch2:         fix-unmarshal-web-config.patch
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  go >= 1.11.1
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.11
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
%setup -q -n dex-%{version}
%patch1
%patch2

%build
%{goprep} github.com/dexidp/dex
%{gobuild} -ldflags "-w -X github.com/dexidp/dex/version.Version=%{version}" cmd/dex
%{gobuild} -ldflags "-w -X github.com/dexidp/dex/version.Version=%{version}" cmd/example-app
%{gobuild} -ldflags "-w -X github.com/dexidp/dex/version.Version=%{version}" examples/grpc-client

%install
%{goinstall}
%{gofilelist}

# Install the web content
for file in $(find web -type f); do
  install -D -m 0644 $file %{buildroot}/%{_datadir}/%{name}/$file
done

%files -f file.lst
%license LICENSE
%doc README.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/web
%dir %{_datadir}/%{name}/web/static
%dir %{_datadir}/%{name}/web/static/img
%dir %{_datadir}/%{name}/web/templates
%dir %{_datadir}/%{name}/web/themes
%dir %{_datadir}/%{name}/web/themes/coreos
%dir %{_datadir}/%{name}/web/themes/tectonic
%{_datadir}/%{name}/web/*
%{_bindir}/dex
%{_bindir}/example-app
%{_bindir}/grpc-client

%changelog
