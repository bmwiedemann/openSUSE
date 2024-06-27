#
# spec file for package broot
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


Name:           broot
Version:        1.39.0
Release:        0
Summary:        A better way to navigate directories
License:        GPL-2.0-only AND MIT AND MPL-2.0
URL:            https://dystroy.org/broot/
Source0:        https://github.com/Canop/broot/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        %{name}.changes
BuildRequires:  cargo-packaging

%description
A better way to navigate directories.
Tree-like commandline directory navigator written in Rust.

%prep
%setup -qa 1

%build
%cargo_build

%check
%cargo_test

%install
%cargo_install
rm -rf %{buildroot}/%{_builddir}/%{name}-%{version}/vendor/

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/broot

%changelog
