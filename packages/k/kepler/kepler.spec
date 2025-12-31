#
# spec file for package kepler
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           kepler
Version:        0.11.3
Release:        0
Summary:        Kubernetes-based Efficient Power Level Exporter
License:        Apache-2.0 AND (BSD-2-Clause OR GPL-2.0-only) AND GPL-2.0-only
Group:          System/Monitoring
URL:            https://github.com/sustainable-computing-io/kepler/
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        kepler.service

BuildRequires:  clang
BuildRequires:  llvm
BuildRequires:  llvm-devel
BuildRequires:  zlib-devel
BuildRequires:  golang(API) >= 1.24
Recommends:     cpuid
%{?systemd_ordering}

%description
Kubernetes-based Efficient Power Level Exporter

%prep
%setup -a1 -n kepler-%{version}

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build -o %{name} ./cmd/kepler

%install
install -d %{buildroot}%{_sysconfdir}/%{name}

install -D -m755 ./%{name}  %{buildroot}%{_bindir}/%{name}
install -D -m644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -m644 ./hack/config.yaml %{buildroot}%{_sysconfdir}/%{name}/config.yaml

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSES/Apache-2.0.txt
%license LICENSES/BSD-2-Clause.txt
%license LICENSES/GPL-2.0-only.txt
%dir /%{_sysconfdir}/%{name}
%config(noreplace) /%{_sysconfdir}/%{name}/config.yaml
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
