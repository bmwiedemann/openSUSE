#
# spec file for package sd
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


Name:           sd
Version:        0.7.6+g33
Release:        0
Summary:        Intuitive find & replace CLI
URL:            https://github.com/chmln/sd
License:        (Apache-2.0 OR MIT) AND (MIT OR Unlicense) AND BSD-3-Clause AND MIT AND (MIT OR Unlicense)
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging

%description
sd uses regex syntax that you already know from JavaScript and Python.
Forget about dealing with quirks of sed or awk - get productive immediately.

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config.toml

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/sd

%changelog
