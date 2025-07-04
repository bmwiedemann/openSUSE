#
# spec file for package ninja
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

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define name_ext -test
%bcond_without test
%else
%define name_ext %{nil}
%bcond_with test
%endif

Name:           ninja%{name_ext}
Version:        1.13.0
Release:        0
Summary:        A small build system closest in spirit to Make
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://ninja-build.org/
Source0:        https://github.com/ninja-build/ninja/archive/v%{version}/ninja-%{version}.tar.gz
Source1:        macros.ninja
Patch1:         ninja-disable-maxprocs-test.patch
Patch2:         ninja-re2c-g.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if %{with test}
BuildRequires:  googletest-devel
%endif
BuildRequires:  python3-base
BuildRequires:  re2c

%description
Ninja is yet another build system. It takes as input the interdependencies
of files (typically source code and output executables) and orchestrates
building them, quickly.

%prep
%autosetup -p1 -n ninja-%{version}

%build
export CFLAGS="%{optflags}"
%if "%__isa_bits" == "32"
CFLAGS="$CFLAGS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"
%endif
export CXXFLAGS="$CFLAGS"
%if %{without test}
%cmake -DBUILD_TESTING=OFF
%else
%cmake
%endif
%cmake_build

%install
%if %{without test}
%cmake_install
install -D -p -m 0644 misc/zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_ninja
install -D -p -m 0644 misc/ninja.vim %{buildroot}%{_datadir}/vim/site/syntax/ninja.vim
install -D -p -m 0644 misc/bash-completion %{buildroot}%{_datadir}/bash-completion/completions/ninja
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/macros.ninja
%endif

%check
%if %{with test}
%ctest
%endif

%files
%if %{without test}
%license COPYING
%{_bindir}/ninja
%{_datadir}/bash-completion
%{_datadir}/vim
%{_datadir}/zsh
%{_rpmconfigdir}/macros.d/macros.ninja

%changelog
%endif