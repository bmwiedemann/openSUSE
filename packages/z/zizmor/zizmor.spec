#
# spec file for package zizmor
#
# Copyright (c) 2025 SUSE LLC
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


Name:           zizmor
Version:        1.3.0
Release:        0
Summary:        A static analysis tool for GitHub Actions
License:        MIT
URL:            https://github.com/woodruffw/zizmor
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.80
BuildRequires:  cargo-packaging
ExcludeArch:    %{ix86} armv7hl

%description
zizmor is a static analysis tool for GitHub Actions. It can find many common
security issues in typical GitHub Actions CI/CD setups.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%check
%{cargo_test}

%files
%doc README.md
%license LICENSE
%{_bindir}/zizmor

%changelog
