#
# spec file for package oeis-tui
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           oeis-tui
Version:        1.0.0
Release:        0
Summary:        A CLI/TUI for the Encyclopedia of Integer Sequences (OEIS)
License:        MIT
URL:            https://github.com/hako/oeis-tui
Source0:        %{name}-%{version}.tar.zst
Source1:        registry.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
A command-line and terminal interface for browsing the On-Line Encyclopedia of
Integer Sequences (OEIS).

%prep
%autosetup -p1 -a1

%build
export CARGO_HOME=$PWD/.cargo
%{cargo_build}

%install
export CARGO_HOME=$PWD/.cargo
%{cargo_install}

# network access
# %%check
# export CARGO_HOME=$PWD/.cargo
# %%{cargo_test}

%files
%doc README.md
%{_bindir}/oeis

%changelog
