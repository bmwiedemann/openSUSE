#
# spec file for package sevctl
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


Name:           sevctl
Version:        0.4.3
Release:        0
Summary:        Administrative utility for AMD SEV
Group:          Development/Libraries/Rust
License:        Apache-2.0
URL:            https://github.com/virtee/sevctl
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  libopenssl-devel
BuildRequires:  rubygem(asciidoctor)
ExclusiveArch:  x86_64

%description
Administrative utility for AMD SEV

%files
%doc README.md
%{_bindir}/sevctl

%prep
%autosetup -a1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%changelog
