#
# spec file for package golang-github-prometheus-promu
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


Name:           golang-github-prometheus-promu
Version:        0.14.0
Release:        0
Summary:        Prometheus Utility Tool
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/prometheus/promu
Source:         promu-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
ExcludeArch:    s390
%{go_provides}
%if 0%{?rhel}
# Fix ERROR: No build ID note found in
%undefine _missing_build_ids_terminate_build
BuildRequires:  golang >= 1.17
%else
BuildRequires:  golang(API) = 1.18
%endif

%description
The Prometheus Utility Tool is used by the Prometheus project to build other components.

%prep
%autosetup -a1 -p1 -n promu-%{version}

%build
%{goprep} github.com/prometheus/promu
export VERSION=%{version}
export CGO_ENABLED=0
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-s -w -X main.version=$VERSION" \
   -o promu ;

%install
install -D -m 0755 promu "%{buildroot}/%{_bindir}/promu"

%files
%doc README.md
%license LICENSE
%{_bindir}/promu

%changelog
