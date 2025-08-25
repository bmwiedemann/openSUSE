#
# spec file for package shfmt
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


%define prj_name sh

Name:           shfmt
Version:        3.12.0
Release:        0
Summary:        A shell formatter with bash support
License:        BSD-3-Clause
URL:            https://github.com/mvdan/sh
Source0:        %{prj_name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  golang(API) >= 1.19

%description
A shell formatter. Supports POSIX Shell, Bash, and mksh.

%prep
%setup -q -a1 -n %{prj_name}-%{version}

%build
# Embedding version info via ldflags is necessary here due to upstream
# choice to always return (devel) in:
# https://github.com/mvdan/sh/blob/master/cmd/shfmt/main.go#L73 and
# https://github.com/mvdan/sh/blob/master/cmd/shfmt/main.go#L168-L176
# TODO: PR upstream to use runtime/debug.ReadBuildInfo available in go1.18+
go build \
   -mod=vendor \
   -tags extended \
   -buildmode=pie \
   -ldflags "-X main.version=%{version}" \
   ./cmd/shfmt

%check
# execute the binary as a basic check
./%{name} --help
# also check version since this application requires unusual packaging (ldflags)
if [ "$(./%{name} --version)" != "%{version}" ] ; then
    echo "Version information embedded in binary is not the value expected"
    exit 1
fi

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/shfmt

%changelog
