#
# spec file for package lazysql
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           lazysql
Version:        0.7.0
Release:        0
Summary:        Terminal UI database management tool
License:        MIT
URL:            https://github.com/jorgerojas26/lazysql
Source0:        https://github.com/jorgerojas26/lazysql/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.23

%description
LazySQL is a terminal user interface for managing databases, inspired by
Lazygit. It supports PostgreSQL, MySQL, SQLite, MSSQL and ClickHouse and
lets you browse tables, edit rows and run queries from the keyboard.

Telemetry is off in this build: no collector endpoint is compiled in.

%prep
%autosetup -a1

%build
# No -X main.telemetryEndpoint: an empty endpoint disables telemetry and its
# prompt. main.distribution stays "source", as for any build from source.
export GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off
go build -mod=vendor -buildvcs=false -trimpath -buildmode=pie \
    -ldflags '-X main.version=%{version}' -o %{name} .

%install
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}

%check
export GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off
# Database integration tests skip themselves unless a server URL is set.
go test -mod=vendor -buildvcs=false ./...
# -version prints with Go's builtin println, which writes to stderr.
./%{name} -version 2>&1 | grep -F %{version}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}

%changelog
