#
# spec file for package tokei
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


Name:           tokei
Version:        13.0.0.alpha.0+git14
Release:        0
Summary:        Code statistics commandline tool
License:        (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND BSD-3-Clause AND MIT AND MPL-2.0 AND (Apache-2.0 OR MIT)
URL:            https://github.com/XAMPPRocky/tokei
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
Shows the number of files, total lines within those files and code, comments and blanks grouped by language.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%{_bindir}/tokei
%license LICENCE-APACHE LICENCE-MIT
%doc README.md CHANGELOG.md tokei.example.toml

%changelog
