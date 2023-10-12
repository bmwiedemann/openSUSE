#
# spec file for package zk-spaced
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


Name:           zk-spaced
Version:        1.0.0
Release:        0
Summary:        Space repetition memoization for zk
License:        MIT
URL:            https://github.com/matze/zk-spaced
Source0:        https://github.com/matze/zk-spaced/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  rust+cargo
BuildRequires:  zstd
Supplements:    (%{name} and zk)
Requires:       zk

%description
zk-spaced is a companion cli app to create space repetition memoization for zk.

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%{_bindir}/%{name}
%doc *.md
%license LICENSE

%changelog
