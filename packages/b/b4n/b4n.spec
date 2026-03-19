#
# spec file for package b4n
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


Name:           b4n
Version:        0.4.3
Release:        0
Summary:        Terminal user interface (TUI) for Kubernetes API written in Rust
License:        MIT
URL:            https://github.com/fioletoven/b4n
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging

%description
b4n is a terminal user interface (TUI) for the Kubernetes API, created mainly
for learning the Rust programming language. It is heavily based on the k9s
project and built using the kube-rs and ratatui crates.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%check
%{cargo_test}
%{buildroot}%{_bindir}/%{name} --version
%{buildroot}%{_bindir}/%{name} --version | grep %{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/b4n

%changelog
