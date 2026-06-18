#
# spec file for package bshoshany-thread-pool
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


Name:           bshoshany-thread-pool
Version:        4.1.0
Release:        0
Summary:        Fast, lightweight C++17 thread pool library
License:        MIT
URL:            https://github.com/bshoshany/thread-pool
Source0:        https://github.com/bshoshany/thread-pool/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildArch:      noarch

%description
BS::thread_pool is a fast, lightweight, modern, and easy-to-use C++17
thread pool library. It provides a header-only implementation of a
thread pool for parallelizing tasks, plus a few accompanying utility
classes.

%package devel
Summary:        Development files for %{name}
Requires:       libstdc++-devel

%description devel
Header files for the BS::thread_pool C++17 thread pool library
(header-only): BS_thread_pool.hpp and the BS_thread_pool_utils.hpp
utility helpers.

%prep
%autosetup -p1 -n thread-pool-%{version}

%build
# header-only library: nothing to compile

%install
install -D -m 0644 include/BS_thread_pool.hpp %{buildroot}%{_includedir}/BS_thread_pool.hpp
install -D -m 0644 include/BS_thread_pool_utils.hpp %{buildroot}%{_includedir}/BS_thread_pool_utils.hpp

%check
# upstream's self-contained test program (no framework); deadlock/benchmark
# suites are off by default, so this only runs the deterministic checks
g++ %{optflags} -std=c++17 -pthread -Iinclude tests/BS_thread_pool_test.cpp -o bs_thread_pool_test
./bs_thread_pool_test tests

%files devel
%license LICENSE.txt
%doc README.md CHANGELOG.md
%{_includedir}/BS_thread_pool.hpp
%{_includedir}/BS_thread_pool_utils.hpp

%changelog
