#
# spec file for package golang-github-prometheus-promu
#
# Copyright (c) 2020 SUSE LLC
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


%{go_nostrip}

Name:           golang-github-prometheus-promu
Version:        0.5.0
Release:        0
Summary:        Prometheus Utility Tool
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/prometheus/promu
Source:         promu-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.11
BuildRequires:  golang-packaging
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{go_provides}

%description
The Prometheus Utility Tool is used by the Prometheus project to build other components.

%prep
%setup -q -n promu-%{version}
%setup -q -T -D -a 1 -n promu-%{version}

%build
%goprep github.com/prometheus/promu
export VERSION=%{version}
export CGO_ENABLED=0
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-s -w -X main.version=$VERSION" \
   -o promu ;

%install
install -D -m 0755 promu "%{buildroot}/%{_bindir}/promu"
%gosrc

%gofilelist

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/promu

%changelog
