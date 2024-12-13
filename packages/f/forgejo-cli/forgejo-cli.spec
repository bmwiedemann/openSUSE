#
# spec file for package forgejo-cli
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


Name:           forgejo-cli
Version:        0.2.0
Release:        0
Summary:        CLI application for interacting with Forgejo
License:        Apache-2.0 OR MIT
URL:            https://codeberg.org/Cyborus/forgejo-cli
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.82.0
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

%description
%{summary}.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
install -Dm0755 ./target/release/fj %{buildroot}%{_bindir}/fj

%files
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{_bindir}/fj

%changelog
