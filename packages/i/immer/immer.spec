#
# spec file for package immer
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

# Some tests fail on 32bit archs and TW's aarch64
%if 0%{?suse_version} > 1500
%ifarch aarch64
%define skip_tests 1
%endif
%endif
%ifarch %{ix86} %{arm}
%define skip_tests 1
%endif
%if !0%{?skip_tests}
%bcond_without tests
%endif
Name:           immer
Version:        0.8.1
Release:        0
Summary:        Persistent and immutable data structures written in C++
License:        BSL-1.0
URL:            https://sinusoid.es/immer/
Source0:        https://github.com/arximboldi/immer/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gc-devel
BuildRequires:  gcc-c++
# includes catch2/catch.hpp
BuildRequires:  cmake(Catch2) < 3.0
%if %{with tests}
BuildRequires:  cmake(fmt)
%endif

%description
immer is a library of persistent and immutable data structures written in C++.
These enable whole new kinds of architectures for interactive and concurrent
programs.

%package devel
Summary:        Persistent and immutable data structures written in C++

%description devel
immer is a library of persistent and immutable data structures written in C++.
These enable whole new kinds of architectures for interactive and concurrent
programs.

%prep
%autosetup -p1

# Causes a build error
rm -r test/experimental

%build
%cmake -DDISABLE_WERROR:BOOL=TRUE \
       -Dimmer_BUILD_DOCS:BOOL=FALSE \
       -Dimmer_BUILD_EXAMPLES:BOOL=FALSE \
       -Dimmer_BUILD_EXTRAS:BOOL=FALSE

%cmake_build

%install
%cmake_install

%check
%if %{with tests}
# %%ctest won't work
%{__cmake} --build %{__builddir} %{?_smp_mflags} -t check
%endif

%files devel
%license LICENSE
%doc README.rst
%{_includedir}/immer/
%{_libdir}/cmake/Immer/

%changelog
