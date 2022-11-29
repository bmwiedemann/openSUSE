#
# spec file for package gokart
#
# Copyright (c) 2022 SUSE LLC
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


Name:           gokart
Version:        0.5.1
Release:        0
Summary:        Static analysis tool for securing Go code
License:        Apache-2.0
URL:            https://github.com/praetorian-inc/gokart
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.19
Requires:       go >= 1.19
ExcludeArch:    s390
ExcludeArch:    %{ix86}
# Make sure that the binary is not getting stripped.
%{go_nostrip}

%description
GoKart is a static analysis tool for Go that finds vulnerabilities using the
SSA (single static assignment) form of Go source code. It is capable of tracing
the source of variables and function arguments to determine whether input
sources are safe, which reduces the number of false positives compared to
other Go security scanners. For instance, a SQL query that is concatenated
with a variable might traditionally be flagged as SQL injection; however,
GoKart can figure out if the variable is actually a constant or constant
equivalent, in which case there is no vulnerability.

%prep
%setup -qa1

%build
CGO_ENABLED=0
go build -mod=vendor -buildmode=pie

%install
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 gokart %{buildroot}%{_bindir}/gokart

%files
%license LICENSE
%doc README.md SECURITY.md
%{_bindir}/gokart

%changelog
