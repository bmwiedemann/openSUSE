#
# spec file for package vegeta
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           vegeta
Version:        12.13.0
Release:        0
Summary:        HTTP load testing tool and library
License:        MIT
URL:            https://github.com/tsenart/vegeta
Source:         vegeta-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.22

%description
Vegeta is a versatile HTTP load testing tool built out of a need to drill HTTP
services with a constant request rate.

Features:

* Usable as a command line tool and a Go library.
* CLI designed with UNIX composability in mind.
* Avoids nasty Coordinated Omission.
* Extensive reporting functionality.
* Simple to use for distributed load testing.
* Easy to install and run (static binary, package managers, etc).

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.Version=%{version} -X main.Commit=${COMMIT_HASH} -X main.Date=$BUILD_DATE" \
   -o bin/vegeta

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
