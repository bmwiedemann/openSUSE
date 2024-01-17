#
# spec file for package klib
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


Name:           klib
Version:        1.0~git.20210716
Release:        0
BuildArch:      noarch
Summary:        C library with utility functions
License:        MIT
URL:            https://github.com/attractivechaos/klib
Source:         %{name}-%{version}.tar.xz

%description
Klib is a C library that provides data types like hashes, search
trees, AVL trees, sorting functions, a dynamic array type, a
singly-linked list and memory pool, various numeric routines and a
command-line argument parser.

%package devel
Summary:        Development files for klib
Requires:       %{name} = %{version}

%description devel
Klib is a C library that provides data types like hashes, search
trees, AVL trees, sorting functions, a dynamic array type, a
singly-linked list and memory pool, various numeric routines and a
command-line argument parser.

To use a component of this library, files need to be copied to the
source code tree where it is supposed to be used.

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}%{_includedir}
install -m 0644 *.h %{buildroot}%{_includedir}/
mkdir -p %{buildroot}%{_datadir}/%{name}/
install -m 0644 *.c %{buildroot}%{_datadir}/%{name}/

%files
%license LICENSE.txt 
%doc README.md

%files devel
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.c
%{_includedir}/*.h

%changelog
