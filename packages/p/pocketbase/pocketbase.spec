#
# spec file for package pocketbase
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Eyad Issa <eyadlorenzo@gmail.com>
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


Name:           pocketbase
Version:        0.36.1
Release:        0
Summary:        Open Source realtime backend
License:        MIT
URL:            https://github.com/pocketbase/pocketbase
Source0:        https://github.com/pocketbase/pocketbase/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  golang-packaging
BuildRequires:  zstd
# 32-bit builds are not supported upstream
ExcludeArch:    %{ix86} %{arm32}

%description
PocketBase is an open source Go backend that includes:

- embedded database (SQLite) with realtime subscriptions
- built-in files and users management
- convenient Admin dashboard UI
- and simple REST-ish API

%prep
%autosetup -p1 -a1

%build
%ifarch %{x86_64} %{arm64} %{power64}
export CGO_ENABLED=0
%endif

go build \
   -v \
   -ldflags "-X github.com/pocketbase/pocketbase.Version=%{version}" \
   -mod=vendor \
   -buildmode=pie \
   ./examples/base

%check
go test -v ./...

%install
install -D -m0755 base %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}

%changelog
