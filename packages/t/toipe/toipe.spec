#
# spec file for package toipe
#
# Copyright (c) 2023 SUSE LLC
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


Name:           toipe
Version:        0.4.1+g12
Release:        0
Summary:        Yet another typing test, but crab flavoured
License:        (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR MIT) AND (MIT OR Unlicense) AND MIT
URL:            https://github.com/Samyak2/toipe
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.46
BuildRequires:  zstd
ExclusiveArch:  %{rust_arches}

%description
A commandline tool that launches a typing test.
It looks best when used on a terminal with color and style support.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license LICENSE
%doc README.md
%{_bindir}/toipe
%{_bindir}/randomword

%changelog
