#
# spec file for package btfdump
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


%define binary_name btf
Name:           btfdump
Version:        0.0.4~0
Release:        0
Summary:        BTF introspection tool
License:        BSD-2-Clause
URL:            https://github.com/anakryiko/btfdump
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
BPF Type Format information and data introspection tool. It dumps BTF types in various formats.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{binary_name} %{buildroot}%{_bindir}/%{binary_name}

%files
%license LICENSE
%{_bindir}/%{binary_name}

%changelog
