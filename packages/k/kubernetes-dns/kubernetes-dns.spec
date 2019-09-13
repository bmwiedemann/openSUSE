#
# spec file for package kubernetes-dns
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define git_commit %{version}

Name:           kubernetes-dns
Version:        1.14.1
Release:        0
Summary:        DNS for Kubernetes
License:        Apache-2.0
Group:          Development/Languages/Other
Url:            https://github.com/kubernetes/dns
Source:         %{name}-%{version}.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) = 1.11
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{go_nostrip}
%{go_provides}
Provides:       kube-dns = %{version}

%description
This is the package for Kubernetes DNS.

%prep
%setup -q -n %{name}-%{version}
%{goprep} k8s.io/dns

%build
export GOPATH="%{_builddir}/go:$GOPATH"
GOBIN=$PWD/bin go install -tags '' -ldflags ' -X k8s.io/dns/pkg/version.Version=%{version}' k8s.io/dns/...

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/k8s/dns/dnsmasq-nanny
install -m755 bin/sidecar %{buildroot}/%{_bindir}/sidecar
install -m755 bin/kube-dns %{buildroot}/%{_bindir}/kube-dns
install -m755 bin/dnsmasq-nanny %{buildroot}/%{_bindir}/dnsmasq-nanny

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%dir %{_sysconfdir}/k8s
%dir %{_sysconfdir}/k8s/dns
%dir %{_sysconfdir}/k8s/dns/dnsmasq-nanny
%{_bindir}/sidecar
%{_bindir}/kube-dns
%{_bindir}/dnsmasq-nanny

%changelog
