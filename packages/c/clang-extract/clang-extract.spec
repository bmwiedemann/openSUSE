#
# spec file for package clang-extract
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


Name:           clang-extract
Version:        0~20240703.0b3e33c
Release:        0
Summary:        A tool to extract code content from source files
License:        Apache-2.0 WITH LLVM-exception AND NCSA
URL:            https://github.com/SUSE/clang-extract
Source:         %{name}-%{version}.tar.xz
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  clang-tools
BuildRequires:  cmake
BuildRequires:  libelf-devel
BuildRequires:  llvm-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  python3-pexpect
BuildRequires:  python3-psutil
BuildRequires:  python3-pytest

%description
A tool to extract code content from source files using the clang and LLVM infrastructure.

%prep
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

%changelog
