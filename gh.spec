#
# spec file for package gh
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


Name:           gh
Version:        1.3.1
Release:        0
Summary:        The official CLI for GitHub
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://cli.github.com/
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
%if 0%{?sle_version} <= 150200
BuildRequires:  (go >= 1.13 or go1.13)
%else
BuildRequires:  go >= 1.13
%endif
Requires:       git

%description
Official CLI client for GitHub written in Go

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build -mod=vendor -buildmode=pie -o bin/gh ./cmd/gh

%install

install -D -m 0755 bin/gh %{buildroot}%{_bindir}/gh

%files
%{_bindir}/gh

%changelog
