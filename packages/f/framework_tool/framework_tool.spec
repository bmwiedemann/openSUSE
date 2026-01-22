#
# spec file for package framework_tool
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


%define reponame framework-system
%define completion_dir_bash %{_datadir}/bash-completion/completions
%define completion_dir_zsh %{_datadir}/zsh/functions/Completion
Name:           framework_tool
Version:        0.5.0
Release:        0
Summary:        Rust tools to interact with the Framework Computer systems
License:        BSD-3-Clause
URL:            https://github.com/FrameworkComputer/framework-system
Source0:        https://github.com/FrameworkComputer/framework-system/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  pkg-config
BuildRequires:  systemd-devel
BuildRequires:  zsh
ExclusiveArch:  x86_64

%description
Rust tools to interact with the Framework Computer systems, especially with the built-in embedded controller

%prep
%autosetup -p1 -a1 -n %{reponame}-%{version}

%build
%cargo_build

%install
install -D -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0644 completions/bash/framework_tool %{buildroot}%{completion_dir_bash}/framework_tool.bash
install -D -m 0644 completions/zsh/_framework_tool %{buildroot}%{completion_dir_zsh}/framework_tool.zsh

%check
%cargo_test

%files
%license LICENSE.md
%doc README.md support-matrices.md EXAMPLES.md
%{_bindir}/%{name}
%{completion_dir_bash}/framework_tool.bash
%{completion_dir_zsh}/framework_tool.zsh

%changelog
