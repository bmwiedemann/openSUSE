#
# spec file for package kubetui
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


Name:           kubetui
Version:        1.5.2
Release:        0
Summary:        A terminal UI for Kubernetes
License:        MIT
URL:            https://github.com/sarub0b0/kubetui
Source0:        kubetui-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  zstd

%description

Kubetui is a terminal user interface (TUI) tool designed for monitoring Kubernetes resources.
It provides an easy-to-use interface for developers and operators to access important information about their applications and infrastructure.

%prep
%autosetup -a1
install -D -m 0644 %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
