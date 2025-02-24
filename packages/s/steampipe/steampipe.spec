#
# spec file for package steampipe
#
# Copyright (c) 2025 SUSE LLC
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


Name:           steampipe
Version:        1.0.3
Release:        0
Summary:        Query various APIs and services via SQL language
License:         	AGPL-3.0-only
URL:            https://github.com/turbot/steampipe
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.22
%{go_nostrip}

%description
Steampipe is the zero-ETL way to query APIs and services. Use it to expose data sources to SQL.

%prep
%autosetup -D -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%install
install -Dm 755 %{name} %{buildroot}/%{_bindir}/%{name}

%check
go test ./...

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
