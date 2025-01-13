#
# spec file for package rqlite
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           rqlite
Version:        8.36.5
Release:        0
Summary:        Distributed relational database built on SQLite
License:        MIT
URL:            https://rqlite.io/
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  go >= 1.22.0
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sqlite3)

%description
rqlite is a relational database which combines SQLite's simplicity with the
power of a robust, fault-tolerant, distributed system. It's designed for easy
deployment and lightweight operation, offering a developer-friendly and
operator-centric solution for multiple platforms.

%prep
%autosetup -p1 -a1

%build
export GOFLAGS="$GOFLAGS -tags=libsqlite3"
go build -mod=vendor -buildmode=pie ./cmd/rqlite
go build -mod=vendor -buildmode=pie ./cmd/rqlited
go build -mod=vendor -buildmode=pie ./cmd/rqbench

%install
install -D -m0755 rqlite %{buildroot}%{_bindir}/rqlite
install -D -m0755 rqlited %{buildroot}%{_bindir}/rqlited
install -D -m0755 rqbench %{buildroot}%{_bindir}/rqbench

%files
%license LICENSE
%doc README.md
%{_bindir}/rqbench
%{_bindir}/rqlite
%{_bindir}/rqlited

%changelog
