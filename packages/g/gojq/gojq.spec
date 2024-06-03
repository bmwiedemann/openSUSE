#
# spec file for package gojq
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gojq
Version:        0.12.16
Release:        0
Summary:        Pure Go implementation of jq
License:        MIT
URL:            https://github.com/itchyny/gojq
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        gojq.rpmlintrc
BuildRequires:  go >= 1.20
BuildRequires:  golang-packaging
BuildRequires:  zstd

%description
Pure Go implementation of jq.

%prep
%autosetup -p1 -a1

%build
%ifarch ppc64
BUILDMODE=''
%else
BUILDMODE='-buildmode=pie'
%endif
go build -a -v -x -mod=vendor $BUILDMODE ./cmd/gojq

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m0644 _%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%check
%gotest ./...

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
