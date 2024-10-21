#
# spec file for package mandown
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


Name:           mandown
Version:        0.1.3
Release:        0
Summary:        A man page generator for markdown markup files
License:        Apache-2.0
Group:          Development/Tools/Doc Generators
URL:            https://gitlab.com/kornelski/mandown
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  c_compiler
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  zstd

%description
Mandown is a tool that generates man pages from markdown markup files.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license LICENSE
%doc README.md
%{_bindir}/mandown

%changelog
