#
# spec file for package caligula
#
# Copyright (c) 2025 Emanuele De Cupis (balanza) <emanuele@decup.is> 
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


Name:           caligula
Version:        0.4.8~0
Release:        0%{?dist}
Summary:        A user-friendly, lightweight TUI for disk imaging
License:        GPL-3.0-only
URL:            https://github.com/ifd3f/caligula
Source0:        %{name}-%{version}.tar.zst
Source1:        registry.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
A user-friendly, lightweight TUI for disk imaging

%prep
%autosetup -p1 -a1

%build
export CARGO_HOME=$PWD/.cargo
%{cargo_build}

%install
export CARGO_HOME=$PWD/.cargo
%{cargo_install}
strip %{buildroot}%{_bindir}/%{name}

%check
export CARGO_HOME=$PWD/.cargo
%{cargo_test}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
