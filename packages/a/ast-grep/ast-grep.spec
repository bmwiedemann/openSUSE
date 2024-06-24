#
# spec file for package ast-grep
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


Name:           ast-grep
Version:        0.24.0+0
Release:        0
Summary:        A CLI tool for code structural search, lint and rewriting
License:        MIT
URL:            https://ast-grep.github.io/
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  gcc-c++

%description
ast-grep(sg) is a CLI tool for code structural search, lint, and rewriting.

%prep
%autosetup -p1 -a1
install -D -m 644 %{SOURCE2} .cargo/config

%build
%{cargo_build} --locked

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc CHANGELOG.md README.md

%changelog
