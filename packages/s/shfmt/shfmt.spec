#
# spec file for package shfmt
#
# Copyright (c) 2021 SUSE LLC
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

%define prj_name sh

Name:           shfmt
Version:        3.5.1
Release:        0
Summary:        A shell parser, formatter, and interpreter with bash support; includes shfmt
License:        BSD-3-Clause
URL:            https://github.com/mvdan/sh
Source0:        %{prj_name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  golang(API) >= 1.17

%description
A shell parser, formatter, and interpreter. Supports POSIX Shell, Bash, and mksh.

%prep
%setup -q -a1 -n %{prj_name}-%{version}

%build
go build \
   -mod=vendor \
   -tags extended \
   -buildmode=pie \
   ./cmd/shfmt

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/shfmt

%changelog
