#
# spec file for package juliaup
#
# Copyright (c) 2022 SUSE LLC
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


Name:           juliaup
Version:        1.6.3
Release:        0
Summary:        Julia installer and version multiplexer
License:        (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND Apache-2.0 AND ISC AND MIT AND MPL-2.0 AND MIT
Group:          Development/Languages/Other
URL:            https://github.com/JuliaLang/juliaup
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Conflicts:      julia
BuildRequires:  cargo-packaging

%description
A cross-platform installer for the Julia programming language.

The installer also bundles a full Julia version manager called juliaup.
One can use juliaup to install specific Julia versions, it alerts users when new Julia versions are released and provides a convenient Julia release channel abstraction.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}
ln -sv "%{_bindir}/julialauncher" "%{buildroot}/%{_bindir}/julia"

%files
%license LICENSE
%doc README.md
%{_bindir}/julia
%{_bindir}/juliainstaller
%{_bindir}/julialauncher
%{_bindir}/juliaup

%changelog
