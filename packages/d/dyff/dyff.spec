#
# spec file for package dyff
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

Name:           dyff
Version:        1.8.0
Release:        0
Summary:        Diff tool for YAML files, and sometimes JSON
License:        MIT
URL:            https://github.com/homeport/dyff
Source:         dyff-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.19

%description
A diff tool for YAML files, and sometimes JSON.

dyff is inspired by the way the old BOSH v1 deployment output reported changes from one version to another by only showing the parts of a YAML file that change.

Each difference is referenced by its location in the YAML document by using either the Spruce dot-style syntax (some.path.in.the.file) or go-patch path syntax (/some/name=path/in/the/id=file). The output report aims to be as compact as possible to give a clear and simple overview of the change.

Similar to the standard diff tool, it follows the principle of describing the change by going from the from input file to the target to input file.

Input files can be local files (filesystem path), remote files (URI), or the standard input stream (using -).

All orders of keys in hashes are preserved during processing and output to the terminal, most notably in the sub-commands to convert YAML to JSON and vice versa.

%prep
%autosetup -p 1 -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/homeport/dyff/internal/cmd.version=%{version}" \
   -o bin/dyff ./cmd/dyff

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
