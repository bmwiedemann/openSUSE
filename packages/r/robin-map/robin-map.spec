#
# spec file for package robin-map
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


Name:           robin-map
Version:        1.3.0
Release:        0
Summary:        C++ implementation of a fast hash map and hash set using robin hood hashing
License:        MIT
URL:            https://github.com/Tessil/robin-map
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildArch:      noarch

%description
The robin-map library is a C++ implementation of a fast hash map and hash set
using open-addressing and linear robin hood hashing with backward shift
deletion to resolve collisions.

*** This is a header only library. ***
The package you want is %{name}-devel.

%package devel
Summary:        %{summary}

%description devel
The robin-map library is a C++ implementation of a fast hash map and hash set
using open-addressing and linear robin hood hashing with backward shift
deletion to resolve collisions.

Four classes are provided: tsl::robin_map, tsl::robin_set, tsl::robin_pg_map
and tsl::robin_pg_set. The first two are faster and use a power of two growth
policy, the last two use a prime growth policy instead and are able to cope
better with a poor hash function. Use the prime version if there is a chance of
repeating patterns in the lower bits of your hash (e.g. you are storing
pointers with an identity hash function). See GrowthPolicy for details.

A benchmark of tsl::robin_map against other hash maps may be found here. This
page also gives some advices on which hash table structure you should try for
your use case (useful if you are a bit lost with the multiple hash tables
implementations in the tsl namespace).

%prep
%autosetup -p1
# rpmlint complains about the downloaded file's permissions
chmod 0644 %{SOURCE0}

%build
%cmake

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%dir %{_datadir}/cmake/tsl-robin-map
%{_datadir}/cmake/tsl-%{name}/*.cmake
%{_includedir}/tsl/

%changelog
