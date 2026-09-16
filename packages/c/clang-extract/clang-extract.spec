#
# spec file for package clang-extract
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if   0%{?sle_version} == 150700 || 0%{suse_version} == 1570
%define llvm_version    19
%else
%if   0%{?sle_version} == 150600 || 0%{suse_version} == 1560
%define llvm_version    17
%endif
%endif

Name:           clang-extract
Version:        0~20260915.950c2c9
Release:        0
Summary:        A tool to extract code content from source files
License:        Apache-2.0 WITH LLVM-exception AND NCSA
URL:            https://github.com/SUSE/clang-extract
Source:         %{name}-%{version}.tar.xz
BuildRequires:  clang%{?llvm_version}
BuildRequires:  clang%{?llvm_version}-devel
BuildRequires:  libelf-devel
BuildRequires:  libzstd-devel
BuildRequires:  llvm%{?llvm_version}
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  ninja
BuildRequires:  python3
BuildRequires:  zlib-devel

%description
A tool to extract code content from source files using the clang and LLVM infrastructure.

%prep
# Check if we have the python3 binary.
if [ ! -x %{_bindir}/python3 ]; then
  ln -s %{_bindir}/python%{python3_version} %{_bindir}/python%{python3_version}
fi

%autosetup -p1

%build
%meson --native-file ce-native.ini
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE.TXT
%doc README.md
%{_bindir}/ce-inline
%{_bindir}/clang-extract
%{_bindir}/ce-includetree

%changelog
