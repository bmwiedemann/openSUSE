#
# spec file for package parallel-hashmap
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


Name:           parallel-hashmap
Version:        2.0.0
Release:        0
Summary:        Header-only hashmap and btree containers for C++
License:        Apache-2.0
URL:            https://greg7mdp.github.io/parallel-hashmap/
Source0:        https://github.com/greg7mdp/parallel-hashmap/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  make
BuildArch:      noarch

%description
The hashmaps and btree provided here are built upon those open
sourced by Google in the Abseil library. The hashmaps use closed
hashing, where values are stored directly into a memory array,
avoiding memory indirections. By using parallel SSE2 instructions,
these hashmaps are able to look up items by checking 16 slots in
parallel, allowing the implementation to remain fast even when the
table is filled up to 87.5%% capacity.

%package devel
Summary:        %{summary}

%description devel
The hashmaps and btree provided here are built upon those open
sourced by Google in the Abseil library. The hashmaps use closed
hashing, where values are stored directly into a memory array,
avoiding memory indirections. By using parallel SSE2 instructions,
these hashmaps are able to look up items by checking 16 slots in
parallel, allowing the implementation to remain fast even when the
table is filled up to 87.5%% capacity.

%prep
%setup -q

%build
%cmake -DPHMAP_BUILD_TESTS=OFF -DPHMAP_BUILD_EXAMPLES=OFF
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/parallel_hashmap

%changelog
