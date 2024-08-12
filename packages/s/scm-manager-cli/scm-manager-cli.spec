#
# spec file for package scm-manager-cli
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%define executable_name scm

Name:           scm-manager-cli
Version:        1.0.1
Release:        0
Summary:        Command line interface for SCM-Manager
License:        MIT
URL:            https://github.com/scm-manager/cli
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.22

%description
Command line interface for SCM-Manager

%prep
%autosetup -p 1 -a 1

%build
# hash will be shortended by COMMIT_HASH:0:8 later
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/scm-manager/cli/pkg.version=%{version} \
   -X github.com/scm-manager/cli/pkg.commitHash=${COMMIT_HASH:0:8} \
   -X github.com/scm-manager/cli/pkg.buildTime=${BUILD_DATE}" \
   -o bin/%{executable_name} ./scm.go

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%changelog
