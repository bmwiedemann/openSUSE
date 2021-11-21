#
# spec file for package ritchie-cli
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


Name:           ritchie-cli
Version:        2.11.3
Release:        0
Summary:        Ritchie - One CLI to rule them all
License:        Apache-2.0
Group:          Productivity/Publishing/Other
URL:            https://ritchiecli.io/
Source0:        https://github.com/cabelo/ritchie-cli/archive/refs/tags/%{version}.tar.gz
BuildRequires:  golang(API) >= 1.14

%description
Ritchie is an open source framework that creates and tweaks a CLI for your team. It allows you to easily create, build and share formulas. This package contains the CLI core, which can execute formulas stored inside other repositories such as ritchie-formulas.

%prep
%setup -q

%build
go build -buildmode=pie -o dist/linux/rit -v cmd/main.go

%install
install -D -m 0755 ./dist/linux/rit %{buildroot}%{_bindir}/rit

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/rit

%changelog
