#
# spec file for package notary
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
# nodebuginfo


%define goipath github.com/theupdateframework/notary

Name:           notary
Version:        0.7.0
Release:        0
Summary:        Trusted collections handling: server and signer
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/theupdateframework/notary
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        server-config.postgres.json
Source3:        signer-config.postgres.json
Patch0:         0001-Hide-DB-credentials.patch
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.15

%description
The Notary project comprises a server and a client for running and
interacting with trusted collections.

%prep
%setup -q -n %{name}-%{version} -a 1
%patch0 -p1

%build
%goprep %{goipath}
export CGO_ENABLED=0
%define ldflags "-w -X %{goipath}/version.NotaryVersion=v%{version} -X  %{goipath}/version.GitCommit=%{release}"
%define buildtags "pkcs11"

%gobuild -mod vendor -ldflags %{ldflags} -tags %{buildtags} cmd/notary-server
%gobuild -mod vendor -ldflags %{ldflags} -tags %{buildtags} cmd/notary-signer

%install
%goinstall

install -Dm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/notary/server-config.postgres.json
install -Dm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/notary/signer-config.postgres.json

mkdir -p %{buildroot}%{_localstatedir}/lib/notary/migrations
mkdir -p %{buildroot}%{_localstatedir}/lib/notary/migrations/server/postgresql
mkdir -p %{buildroot}%{_localstatedir}/lib/notary/migrations/signer/postgresql
install -Dpm 0755 migrations/migrate.sh %{buildroot}%{_localstatedir}/lib/notary/migrations/migrate.sh
install -Dpm 0644 migrations/server/postgresql/* %{buildroot}%{_localstatedir}/lib/notary/migrations/server/postgresql/
install -Dpm 0644 migrations/signer/postgresql/* %{buildroot}%{_localstatedir}/lib/notary/migrations/signer/postgresql/

%files
%license LICENSE
%doc README.md
%{_bindir}/notary-server
%{_bindir}/notary-signer
%config %{_sysconfdir}/notary
%{_localstatedir}/lib/notary

%config(noreplace) %{_sysconfdir}/notary/server-config.postgres.json
%config(noreplace) %{_sysconfdir}/notary/signer-config.postgres.json

%changelog
