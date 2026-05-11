#
# spec file for package wild
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2026 Eyad Issa
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


Name:           wild
Version:        0.8.0
Release:        0
Summary:        A very fast linker for Linux
License:        Apache-2.0 OR MIT
URL:            https://github.com/wild-linker/wild
Source0:        https://github.com/wild-linker/wild/archive/%{version}/wild-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  binutils-devel
BuildRequires:  cargo
BuildRequires:  cargo-packaging
# For testing
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel-static
BuildRequires:  libstdc++-devel
ExclusiveArch:  %{rust_tier1_arches}

%description
Wild is a linker with the goal of being very fast for iterative
development.

The plan is to eventually make it incremental, however that isn't
yet implemented.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install -p wild}
# Add symlink
ln -s %{_bindir}/wild %{buildroot}%{_bindir}/ld.wild

%check
export WILD_TEST_IGNORE_FORMAT=1
%{cargo_test} --lib --bins

%files
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/wild
%{_bindir}/ld.wild

%changelog
