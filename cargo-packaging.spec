#
# spec file for package cargo-packaging
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


Name:           cargo-packaging
Version:        1.2.0+5
Release:        0
Summary:        Macros and tools to assist with cargo and rust packaging
License:        MPL-2.0
Group:          Development/Languages/Rust
URL:            https://github.com/Firstyear/cargo-packaging
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Requires:       cargo
Requires:       cargo-auditable
Requires:       zstd
BuildRequires:  cargo
BuildRequires:  zstd

Conflicts:      rust-packaging

%description
A set of macros and tools to assist with cargo and rust packaging, written in a manner
that follows upstream rust's best practices.

%prep
%autosetup -a1

%build
cargo build --offline --release

%install
install -D -p -m 0644 -t %{buildroot}%{_fileattrsdir} %{_builddir}/%{name}-%{version}/rust.attr
install -D -p -m 0644 -t %{buildroot}%{_rpmconfigdir}/macros.d %{_builddir}/%{name}-%{version}/macros.cargo

install -D -p -m 0755 -t %{buildroot}%{_rpmconfigdir} %{_builddir}/%{name}-%{version}/target/release/rust-rpm-prov

install -D -p -m 0755 -t %{buildroot}%{_sysconfdir}/zsh_completion.d %{_builddir}/%{name}-%{version}/target/release/build/completions/_rust-rpm-prov
install -D -p -m 0755 -t %{buildroot}%{_sysconfdir}/bash_completion.d %{_builddir}/%{name}-%{version}/target/release/build/completions/rust-rpm-prov.bash

%files

%{_fileattrsdir}/rust.attr
%{_rpmconfigdir}/macros.d/macros.cargo
%{_rpmconfigdir}/rust-rpm-prov

%dir %{_sysconfdir}/zsh_completion.d
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/zsh_completion.d/*
%{_sysconfdir}/bash_completion.d/*

%changelog
