#
# spec file for package wait4x
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


Name:           wait4x
Version:        3.6.0
Release:        0
Summary:        Wait for a port or a service to enter the requested state
License:        Apache-2.0
URL:            https://github.com/wait4x/wait4x
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.24

%description
Wait4X is a lightweight, zero-dependency tool to wait for services to be ready.
Perfect for CI/CD, containers, and local development.

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   -ldflags="-X wait4x.dev/v3/internal/cmd.AppVersion=v%{version} \
   -X wait4x.dev/v3/internal/cmd.GitCommit=${COMMIT_HASH} \
   -X wait4x.dev/v3/internal/cmd.BuildTime=${BUILD_DATE}" \
   -o bin/wait4x cmd/wait4x/main.go

%install
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}
cd %{buildroot}/%{_bindir}/

%check
%{buildroot}/%{_bindir}/%{name} version
%{buildroot}/%{_bindir}/%{name} version | grep v%{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
