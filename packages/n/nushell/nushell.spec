#
# spec file for package nushell
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


Name:           nushell
Version:        0.95.0
Release:        0
Summary:        A new type of shell
License:        MIT
URL:            https://www.nushell.sh/
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  git
BuildRequires:  zstd
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(x11)
ExclusiveArch:  %{rust_tier1_arches}

%description
A modern shell written in Rust.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
%{cargo_install}
install -d %{buildroot}/%{_datadir}/%{name}
cp -r crates/nu-utils/src/sample_config %{buildroot}/%{_datadir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/nu
%{_datadir}/%{name}/

%changelog
