#
# spec file for package wicked2nm
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

Name:           wicked2nm
Version:        1.4.1
Release:        0
Summary:        Migration tool from wicked to NetworkManager
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/wicked2nm
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_arches}

%description
A tool that parses wicked show-config xml and netconfig to generate
NetworkManager connections.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
install -Dm755 "target/release/wicked2nm" "%{buildroot}%{_bindir}/wicked2nm"
 
%check
%{cargo_test}

%files
%doc README.md
%license LICENSE
%{_bindir}/wicked2nm

%changelog

