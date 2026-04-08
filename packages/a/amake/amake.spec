#
# spec file for package amake
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           amake
Version:        0.1.0
Release:        0
Summary:        A task runner for AI CLI tools
# TODO: Run `cargo lock2rpmprovides --spdx` after vendoring to get the
# complete SPDX expression including all vendored crate licenses.
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://github.com/dottorblaster/amake
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
amake is a task runner for AI CLI tools. Think make, but for dispatching
prompts to things like Claude Code, Aider, GitHub Copilot, and others.

Tasks are defined in a TOML file (Amakefile), each with a prompt and
a tool adapter. amake figures out the right CLI invocation and runs it.
Tasks can depend on each other, pass captured output downstream via
template variables, and optionally run inside a clampdown sandbox for
filesystem and network isolation.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
