#
# spec file for package tealdeer
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


Name:           tealdeer
Version:        1.5.0+0
Release:        0
Summary:        An implementation of tldr in Rust
License:        Apache-2.0 OR MIT
Group:          Productivity/Other
URL:            https://github.com/dbrgn/tealdeer
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
# Instructions on how to generate vendor.tar.xz
Source3:        README.packager
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  libopenssl-devel
BuildRequires:  rust
BuildRequires:  rust-std
BuildRequires:  zlib-devel

%description
An implementation of tldr in Rust. It has example based and community-driven man pages.

%prep
%setup -qa1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%doc README.md
%license LICENSE-MIT LICENSE-APACHE
%{_bindir}/tldr

%changelog
