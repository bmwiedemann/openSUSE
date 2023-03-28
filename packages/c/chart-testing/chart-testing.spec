#
# spec file for package chart-testing
#
# Copyright (c) 2023 SUSE LLC
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%define name_of_binary ct

Name:           chart-testing
Version:        3.8.0
Release:        0
Summary:        CLI tool for linting and testing Helm charts
Group:          Development/Languages/Other
License:        Apache-2.0
URL:            https://github.com/helm/chart-testing
Source:         chart-testing-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.16
Requires:       git-core
Requires:       helm
Requires:       python3-yamale
Requires:       python3-yamllint

%description
ct is the the tool for testing Helm charts. It is meant to be used for linting and testing pull requests. It automatically detects charts changed against the target branch.

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/helm/chart-testing/v3/ct/cmd.Version=%{version} \
   -X github.com/helm/chart-testing/v3/ct/cmd.BuildDate=$(date --iso-8601 -d @${SOURCE_DATE_EPOCH:-$(date +%%s)})" \
   -o bin/ct ct/main.go

%install
# Install the binary.
install -D -m 0755 bin/%{name_of_binary} "%{buildroot}/%{_bindir}/%{name_of_binary}"
install -d -m 0755 %{buildroot}/%{_sysconfdir}/%{name_of_binary}
install -d -m 0755 %{buildroot}/%{_docdir}/%{name}/
install -D -m 0644 etc/chart_schema.yaml %{buildroot}/%{_docdir}/%{name}/
install -D -m 0644 etc/lintconf.yaml %{buildroot}/%{_docdir}/%{name}/

%files
%doc README.md
%doc %{_docdir}/%{name}/chart_schema.yaml
%doc %{_docdir}/%{name}/lintconf.yaml
%license LICENSE
%{_bindir}/%{name_of_binary}
%config %{_sysconfdir}/%{name_of_binary}

%changelog
