#
# spec file for package code-minimap
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


Name:           code-minimap
Version:        0.6.8
Release:        0
Summary:        A high performance code minimap render
License:        MIT OR Apache-2.0
URL:            https://github.com/wfxr/code-minimap
Source0:        https://github.com/wfxr/%{name}/archive/refs/tags/v%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
Code-minimap is a tool for generating text minimaps at high speed.

%prep
%autosetup -p1 -a1

%build
%cargo_build

%install
%cargo_install

%check
%cargo_test


%files
%license LICENSE-*
%{_bindir}/%{name}

%changelog
