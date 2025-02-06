#
# spec file for package joker
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


Name:           joker
Version:        1.4.0
Release:        0
Summary:        Small Clojure interpreter, linter and formatter written in Go
License:        EPL-1.0
URL:            https://joker-lang.org
Source0:        https://github.com/candid82/joker/archive/refs/tags/v%{version}.tar.gz#/joker-%{version}.tar.gz
Source1:        vendor.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/candid82/joker/issues/491
Patch0:         reproducible.patch
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?mageia}
BuildRequires:  go-rpm-macros
%else
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.18
%endif

%description
Joker is a small Clojure interpreter, linter and formatter written in Go.

%prep
%autosetup -p1
tar -zxf %{SOURCE1}

%build
GO111MODULE=on CGO_ENABLED=0 go generate ./...
GO111MODULE=on CGO_ENABLED=0 go build -mod=vendor -o %{name} -buildmode=pie \
	-ldflags "-s -w"

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%check
./all-tests.sh

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
