#
# spec file for package oo7
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


Name:           oo7
Version:        0.3.3
Release:        0
Summary:        James Bond went on a new mission as a Secret Service provider
License:        MIT
URL:            https://github.com/bilelmoussaoui/oo7
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
A CLI application to interact with the system keyring. Replacement of the secret-tool utility.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
install -d %{buildroot}%{_bindir}
install -Dpm0755 %{_builddir}/%{name}-%{version}/target/release/%{name}-{cli,portal} %{buildroot}%{_bindir}/

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/oo7-cli
%{_bindir}/oo7-portal

%changelog
