#
# spec file for package pvetui
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


Name:           pvetui
Version:        1.2.1
Release:        0
Summary:        Terminal UI for Proxmox VE
License:        MIT
URL:            https://github.com/devnullvoid/pvetui
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.24 >= 1.24.2

%description
A Terminal User Interface For Proxmox Virtual Environment

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/devnullvoid/pvetui/internal/version.version=%{version} \
   -X github.com/devnullvoid/pvetui/internal/version.commit=${COMMIT_HASH} \
   -X github.com/devnullvoid/pvetui/internal/version.buildDate=${BUILD_DATE}" \
   -o bin/%{name} ./cmd/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check
%{buildroot}/%{_bindir}/%{name} --version
%{buildroot}/%{_bindir}/%{name} --version | grep %{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
