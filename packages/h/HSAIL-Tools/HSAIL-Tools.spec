#
# spec file for package HSAIL-Tools
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           HSAIL-Tools
Version:        0+git20180830.6514deb
Release:        0
Summary:        Parse and (dis)assemble HSA Intermediate Language
License:        NCSA
URL:            https://github.com/HSAFoundation/HSAIL-Tools
Source:         %{name}-%{version}.tar.xz
Patch1:         warning.patch
# PATCH-FIX-UPSTREAM https://github.com/HSAFoundation/HSAIL-Tools/pull/54
Patch2:         reproducible.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libdwarf-devel
BuildRequires:  libelf-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  re2c
BuildRequires:  unzip

%description
HSAIL-Tools are used for parsing, assembling, and disassembling
HSAIL, the Heterogenous System Architecture Intermediate Language (a
virtual instruction set for parallel programs). This version of
libHSAIL supports the HSA PRM 1.02 (Final) specification.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# TODO: I know this is really ugly ;) Create a devel package.
find %{buildroot} "(" -name "*.h" -o -name "*.hpp" -o -name "*.a" ")" -delete

%files
%doc README.md
%{_bindir}/HSAILasm
%{_prefix}/lib/libhsail-amd.so
%{_prefix}/lib/libhsail.so

%changelog
