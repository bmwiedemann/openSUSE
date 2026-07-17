#
# spec file for package unordered_dense
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

Name:           unordered_dense
Version:        4.8.1
Release:        0
Summary:        Hashmap and hashset based on robin-hood backward shift deletion 
Group:          Development/Libraries/C and C++
License:        MIT
URL:            https://github.com/martinus/unordered_dense
Source:         https://github.com/martinus/unordered_dense/archive/refs/tags/v4.8.1.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake

%description
A hashmap and hashset implementation for C++, based on robin-hood backward
shift deletion.

%package devel
Summary:        Hashmap and hashset based on robin-hood backward shift deletion

%description devel
The provided classes, `ankerl::unordered_dense::map` and
`ankerl::unordered_dense::set`, are an (almost) drop-in replacements
for `std::unordered_map` and `std::unordered_set`, respectively.
While they do not have as strong iterator / reference stability
guarantees, they are typically faster than libstdc++'s.

`ankerl::unordered_dense::segmented_map` and
`ankerl::unordered_dense::segmented_set` are offered. These have
lower peak memory usage and stable references (but unstable
iterators) on insert.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%_includedir/ankerl/
%_libdir/cmake/

%changelog
