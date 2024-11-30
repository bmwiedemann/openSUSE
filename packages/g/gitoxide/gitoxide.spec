#
# spec file for package gitoxide
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gitoxide
Version:        0.39.0
Release:        0
Summary:        An idiomatic & safe pure-Rust implementation of Git
License:        Apache-2.0 OR MIT
Group:          Development/Tools/Version Control
URL:            https://github.com/Byron/gitoxide
Source0:        https://github.com/Byron/gitoxide/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  rust >= 1.67.0
ExclusiveArch:  %{rust_arches}

%description
gitoxide is an implementation of git written in Rust for providing a pleasant
and unsurprising developer experience.

%prep
%autosetup -a 1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%doc README.md
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/gix
%{_bindir}/ein

%changelog
