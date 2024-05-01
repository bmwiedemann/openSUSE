#
# spec file for package gping
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


Name:           gping
Version:        1.16.1
Release:        0
Summary:        Ping, but with a graph
License:        MIT
URL:            https://github.com/orf/gping
Source:         %{url}/archive/%{name}-v%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
Comes with the following super-powers:

- Graph the ping time for multiple hosts
- Graph the execution time for commands via the --cmd flag
- Custom colours

%prep
%autosetup -p1 -a1 -n gping-gping-v%{version}

%build
cd gping
%cargo_build

%install
cd gping
%cargo_install

%files
%{_bindir}/gping

%license LICENSE
%doc readme.md

%changelog
