#
# spec file for package binsider
#
# Copyright (c) 2025 mantarimay
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


%bcond_without test
Name:           binsider
Version:        0.3.0
Release:        0
Summary:        Analyze ELF binaries
License:        Apache-2.0 OR MIT
URL:            https://github.com/orhun/binsider
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
ExclusiveArch:  x86_64 aarch64

%description
Binsider can perform static and dynamic analysis, inspect strings, examine
linked libraries, and perform hexdumps, within a terminal user interface.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}

%if %{with test}
%check
%{cargo_test}
%endif

%files
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
